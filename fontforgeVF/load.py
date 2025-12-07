import fontforge
from fontforgeVF.utils import intOrFloat
from os import PathLike
from fontTools import ttLib


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


def _doOpenVariableFont(filename: str | PathLike, axisValues: dict[str, int | float], varfont: ttLib.TTFont) -> fontforge.font:
    from fontTools.varLib import instancer
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
    partial = instancer.instantiateVariableFont(varfont, axisValues)
    with tempfile.TemporaryDirectory() as tmpdir:
        instancePath = (
            tmpdir + '/' + Path(filename).stem + '_' +
            '_'.join([str(k) + str(v) for k, v in axisValues.items()]) +
            '.ttf'
        )
        partial.save(instancePath)
        return fontforge.open(instancePath)


def openVariableFont(filename: str | PathLike, axisValues: dict[str, int | float]) -> fontforge.font:
    """Opens an instance of variable font

    Fontforge cannot treat variable fonts themselves, so they must be
    instantiated.

    :param filename: Variable font file to read. Must end with '.ttf'.
    :param axisValues:``dict`` of axis positions, with axis tag as its
    key.
    :raises ``ValueError``: At least one value of ``axisValues`` is out
    of range.
    """
    with ttLib.TTFont(filename) as ttf:
        if 'fvar' not in ttf:
            return fontforge.open(filename)
        elif list(filter(lambda x: x.minValue != x.maxValue, ttf['fvar'].axes)):
            return _doOpenVariableFont(filename, axisValues, ttf)
        else:
            return fontforge.open(filename)


def _selectInstanceDialog(filename: str | PathLike, ttf: ttLib.TTFont):
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
        openVariableFont(filename, result)


def loadMenu(u, glyph):
    """Shows a dialog to open a variable font

    Shows a dialog to select a font. If a variable font is selected,
    then another dialog is shown to set values of design axes. If a
    non-variable font is selected, simply opens that font.
    """
    if filename := fontforge.openFilename('Open a variable font', '', '*.ttf'):
        with ttLib.TTFont(filename) as ttf:
            if 'fvar' not in ttf:
                fontforge.logWarning(filename + " does not have 'fvar' table")
                fontforge.open(filename)
            elif list(filter(lambda x: x.minValue != x.maxValue, ttf['fvar'].axes)):
                _selectInstanceDialog(filename, ttf)
            else:
                fontforge.logWarning(filename + " has 'fvar' table but all axes are fixed")
                fontforge.open(filename)


def loadEnable(u, glyph):
    return True
