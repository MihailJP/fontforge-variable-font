import fontforge
from fontforgeVF.utils import intOrFloat
from os import PathLike
from fontTools import ttLib
import faulthandler


__all__ = [
    "openVariableFont",
]


def _checkAxisValue(ttf: ttLib.TTFont, axisValues: dict[str, int | float]):
    fail = []
    for axis in ttf['fvar'].axes:
        if axis.axisTag in axisValues:
            if not (axis.minValue <= axisValues[axis.axisTag] <= axis.maxValue):
                fail.append(axis.axisTag)
    if fail:
        raise ValueError(', '.join(["'" + a + "'" for a in fail]) + ' out of range')


def _searchInstance(ttf: ttLib.TTFont, axisValues: dict[str, int | float]):
    for i in ttf['fvar'].instances:
        if i.coordinates == axisValues:
            return i
    return None


def _loadInstanceNames(varfont: ttLib.TTFont, partial: ttLib.TTFont, postscriptNameID: int, subfamilyNameID: int):
    for n in varfont['name'].names:
        if n.nameID == postscriptNameID:
            partial['name'].setName(str(n), 6, n.platformID, n.platEncID, n.langID)
        if n.nameID == subfamilyNameID:
            partial['name'].setName(
                str(varfont['name'].getName(1, n.platformID, n.platEncID, n.langID)) +
                ' ' + str(n),
                4, n.platformID, n.platEncID, n.langID
            )


def _addNames(ttf: ttLib.TTFont, data: dict, nameID: int):
    data['name'] = ''
    data['localNames'] = {}
    for name in filter(
        lambda x: x.nameID == nameID and x.platformID == 3 and x.platEncID == 1,
        ttf['name'].names
    ):
        if name.langID == 0x409:
            data['name'] = str(name)
        else:
            data['localNames'][name.langID] = str(name)
    if len(data['localNames']) == 0:
        del data['localNames']


def _denormalize(minimum, default, maximum, value):
    if value < 0:
        return value * (default - minimum) + default
    elif value > 0:
        return value * (maximum - default) + default
    else:
        return default


def _getVFData_fvar_axes(ttf: ttLib.TTFont, axisValues: dict[str, int | float], vfData: dict):
    for axis in ttf['fvar'].axes:
        tag = axis.axisTag
        axisData = {'active': True}
        if tag in axisValues:
            axisData['useDefault'] = False
            axisData['value'] = axisValues[tag]
            if tag == 'ital':
                axisData['value'] = bool(axisValues[tag])
        else:
            axisData['useDefault'] = True
        axisData['minimum'] = axis.minValue
        axisData['default'] = axis.defaultValue
        axisData['maximum'] = axis.maxValue
        _addNames(ttf, axisData, axis.axisNameID)
        vfData['axes'][tag] = axisData
        vfData['axes'][tag]['labels'] = {}


def _getVFData_fvar_instances(ttf: ttLib.TTFont, vfData: dict):
    for instance in ttf['fvar'].instances:
        instanceData = {}
        psName = {}
        _addNames(ttf, instanceData, instance.subfamilyNameID)
        _addNames(ttf, psName, instance.postscriptNameID)
        instanceData['psName'] = psName['name']
        instanceData |= instance.coordinates
        vfData['instances'].append(instanceData)


def _getVFData_avar(ttf: ttLib.TTFont, vfData: dict):
    if 'avar' in ttf:
        for axis, segments in ttf['avar'].segments.items():
            minimum = vfData['axes'][axis]['minimum']
            default = vfData['axes'][axis]['default']
            maximum = vfData['axes'][axis]['maximum']
            vfData['axes'][axis]['map'] = [
                (
                    _denormalize(minimum, default, maximum, k),
                    _denormalize(minimum, default, maximum, v)
                ) for k, v in ttf['avar'].segments[axis].items()
            ]


def _getVFData_STAT(ttf: ttLib.TTFont, vfData: dict):
    for axis in ttf['STAT'].table.DesignAxisRecord.Axis:
        if axis.AxisTag not in vfData['axes']:
            vfData['axes'][axis.AxisTag] = {
                'active': True,
                'useDefault': True,
                'labels': {},
            }
        vfData['axes'][axis.AxisTag]['order'] = axis.AxisOrdering

    if ttf['STAT'].table.AxisValueArray:
        for label in ttf['STAT'].table.AxisValueArray.AxisValue:
            labelData = {}
            tag = ttf['STAT'].table.DesignAxisRecord.Axis[label.AxisIndex].AxisTag
            value = label.Value
            _addNames(ttf, labelData, label.ValueNameID)
            labelData['elidable'] = bool(label.Flags & 2)
            if label.Format == 3:
                labelData['linkedValue'] = label.LinkedValue
            vfData['axes'][tag]['labels'][value] = labelData


def _getVFData_customTags(ttf: ttLib.TTFont, vfData: dict):
    from fontforgeVF.design_axes import designAxes

    customAxes = list(filter(lambda x: x not in designAxes.keys(), vfData['axes'].keys()))
    for i, a in enumerate(customAxes):
        if i < 3:
            vfData['axes']['custom' + str(i + 1)] = vfData['axes'][a]
            vfData['axes']['custom' + str(i + 1)]['tag'] = a
            for instance in range(len(vfData['instances'])):
                if a in vfData['instances'][instance]:
                    vfData['instances'][instance]['custom' + str(i + 1)] = vfData['instances'][instance][a]
        else:
            fontforge.logWarning("Too many custom axes: '" + a + "' ignored")


def _getVFData(ttf: ttLib.TTFont, axisValues: dict[str, int | float]) -> dict:
    vfData = {
        'axes': {},
        'instances': [],
    }
    _getVFData_fvar_axes(ttf, axisValues, vfData)
    _getVFData_fvar_instances(ttf, vfData)
    _getVFData_avar(ttf, vfData)
    _getVFData_STAT(ttf, vfData)
    _getVFData_customTags(ttf, vfData)
    return vfData


def _instantiate(
    inputFilename: str | PathLike,
    axisValues: dict[str, int | float],
    outputFilename: str | PathLike
) -> ttLib.TTFont:
    # Separate process because instancer may crash
    from subprocess import run

    run(
        [
            'fonttools', 'varLib.instancer',
            '-o', outputFilename,
            '--static',
            inputFilename,
        ] + [str(k) + '=' + str(v) for k, v in axisValues.items()],
        check=True, text=True)
    return ttLib.TTFont(outputFilename)


def _doOpenVariableFont(
    filename: str | PathLike,
    axisValues: dict[str, int | float],
    varfont: ttLib.TTFont
) -> fontforge.font:
    from fontforgeVF.utils import initPersistentDict
    from pathlib import Path
    import tempfile

    axes = [a.axisTag for a in filter(lambda x: x.minValue < x.maxValue, varfont["fvar"].axes)]
    if extra := set(axisValues.keys()) - set(axes):  # extra axes set
        fontforge.logWarning(', '.join(["'" + a + "'" for a in list(extra)]) + ' ignored')
        for tag in list(extra):
            del axisValues[tag]
    if unset := set(axes) - set(axisValues.keys()):  # unset axes
        fontforge.logWarning(', '.join(["'" + a + "'" for a in list(unset)]) + ' not set (default value used)')
        for tag in list(unset):
            axisValues[tag] = [a.defaultValue for a in filter(lambda x: x.axisTag == tag, varfont["fvar"].axes)][0]
    _checkAxisValue(varfont, axisValues)  # out of range
    vfData = _getVFData(varfont, axisValues)
    with tempfile.TemporaryDirectory() as tmpdir:
        stem = (
            Path(filename).stem + '_' +
            '_'.join([str(k) + str(v) for k, v in axisValues.items()])
        )
        if i := _searchInstance(varfont, axisValues):
            n = str(varfont['name'].getName(i.postscriptNameID, 3, 1, 0x409))
            if n:
                stem = n
        instancePath = tmpdir + '/' + stem + '.ttf'
        with _instantiate(filename, axisValues, instancePath) as partial:
            if i := _searchInstance(varfont, axisValues):
                _loadInstanceNames(varfont, partial, i.postscriptNameID, i.subfamilyNameID)
            partial.save(instancePath)
        font = fontforge.open(instancePath)
        initPersistentDict(font)
        font.persistent['VF'] = vfData
        return font


def openVariableFont(
    filename: str | PathLike,
    axisValuesOrInstance: int | str | dict[str, int | float]
) -> fontforge.font:
    """Opens an instance of variable font

    Fontforge cannot treat variable fonts themselves, so they must be
    instantiated.

    :param filename: Variable font file to read. Must end with '.ttf'.
    :param axisValuesOrInstance: If ``int``, an index of the named
    instance list (0 for the first instance). If ``str``, the name of
    an instance. If ``dict``, axis tags as its keys and axis positions
    as their values.
    :raises ``IndexError``: When ``axisValuesOrInstance`` is an
    ``int``, the index of the instance list is out of range.
    :raises ``ValueError``: When ``axisValuesOrInstance`` is a
    ``dict``, at least one value of design axes is out of range
    """
    with ttLib.TTFont(filename) as ttf:
        if 'fvar' not in ttf:
            return fontforge.open(filename)
        elif isinstance(axisValuesOrInstance, dict):
            if list(filter(lambda x: x.minValue != x.maxValue, ttf['fvar'].axes)):
                return _doOpenVariableFont(filename, axisValuesOrInstance, ttf)
            else:
                return fontforge.open(filename)
        elif isinstance(axisValuesOrInstance, int):
            return _doOpenVariableFont(
                filename,
                ttf['fvar'].instances[axisValuesOrInstance].coordinates,
                ttf
            )
        elif isinstance(axisValuesOrInstance, str):
            return _doOpenVariableFont(
                filename,
                list(filter(
                    lambda x: str(ttf['name'].getName(x.subfamilyNameID, 3, 1, 0x409)) == axisValuesOrInstance,
                    ttf['fvar'].instances
                ))[0].coordinates,
                ttf
            )
        else:
            raise TypeError('incompatible type for axisValuesOrInstance')


def _setParameterDialog(filename: str | PathLike, ttf: ttLib.TTFont):
    assert 'fvar' in ttf
    questions = []
    for axis in ttf['fvar'].axes:
        if axis.minValue < axis.maxValue:
            questions.append(
                {
                    'type': 'string',
                    'question': str(ttf['name'].getName(axis.axisNameID, 3, 1, 0x409)) + ' (' +
                    str(axis.minValue) + '\u2013' +
                    str(axis.maxValue) + ')',
                    'tag': axis.axisTag,
                    'default': str(axis.defaultValue),
                },
            )

    if result := fontforge.askMulti('Please specify an instance to open', questions):
        for key in result:
            result[key] = intOrFloat(result[key])
        _doOpenVariableFont(filename, result, ttf)


def _chooseInstanceDialog(filename: str | PathLike, ttf: ttLib.TTFont):
    assert 'fvar' in ttf
    result = fontforge.askChoices(
        'Choose instance(s) to open',
        'Instances in this font',
        [str(ttf['name'].getName(i.subfamilyNameID, 3, 1, 0x409)) for i in ttf['fvar'].instances],
        multiple=True
    )
    for i in [i[1] for i in list(filter(lambda x: x[0], zip(result, ttf['fvar'].instances)))]:
        _doOpenVariableFont(filename, i.coordinates, ttf)


def _selectInstanceDialog(filename: str | PathLike, ttf: ttLib.TTFont, dialogType):
    assert 'fvar' in ttf
    if dialogType == 0:
        _chooseInstanceDialog(filename, ttf)
    else:
        _setParameterDialog(filename, ttf)


def loadMenu(u, glyph):
    """Shows a dialog to open a variable font

    Shows a dialog to select a font. If a variable font is selected,
    then another dialog is shown to set values of design axes. If a
    non-variable font is selected, simply opens that font.
    """
    faulthandler.enable()
    if filename := fontforge.openFilename('Open a variable font', '', '*.ttf'):
        with ttLib.TTFont(filename) as ttf:
            if 'fvar' not in ttf:
                fontforge.logWarning(filename + " does not have 'fvar' table")
                fontforge.open(filename)
            elif list(filter(lambda x: x.minValue != x.maxValue, ttf['fvar'].axes)):
                _selectInstanceDialog(filename, ttf, u)
            else:
                fontforge.logWarning(filename + " has 'fvar' table but all axes are fixed")
                fontforge.open(filename)
    faulthandler.disable()


def loadEnable(u, glyph):
    return True
