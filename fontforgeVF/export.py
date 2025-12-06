from fontforgeVF import utils, language
from fontforgeVF.design_axes import designAxes, getAxisValue
import fontforge
import tempfile
from os import PathLike
from fontTools.designspaceLib import (
    DesignSpaceDocument,
    SourceDescriptor,
    AxisDescriptor,
    DiscreteAxisDescriptor,
    AxisLabelDescriptor,
)


__all__ = [
    "exportVariableFont",
]


def _getSourceFonts(defaultFont: fontforge.font, filterItalicRoman: bool | None = None) -> list[fontforge.font]:
    tmpIter = filter(lambda f: f.familyname == defaultFont.familyname, fontforge.fonts())
    if filterItalicRoman is None:
        return list(tmpIter)
    else:
        return list(filter(lambda f: getAxisValue(f, 'ital') == filterItalicRoman, tmpIter))


def _axisMinValue(defaultFont: fontforge.font, tag: str, filterItalicRoman: bool | None = None) -> int | float:
    return min(
        filter(
            lambda x: x is not None,
            map(
                lambda f: getAxisValue(f, tag),
                _getSourceFonts(defaultFont, filterItalicRoman)
            )
        )
    )


def _axisMaxValue(defaultFont: fontforge.font, tag: str, filterItalicRoman: bool | None = None) -> int | float:
    return max(
        filter(
            lambda x: x is not None,
            map(
                lambda f: getAxisValue(f, tag),
                _getSourceFonts(defaultFont, filterItalicRoman)
            )
        )
    )


def _getFontFamilyName(font: fontforge.font, lang: str = 'English (US)') -> str | None:
    name = font.familyname if lang == 'English (US)' else None
    nametype = 0
    for langname, strid, string in font.sfnt_names:
        if (langname, strid) == (lang, 'Family') and nametype < 1:
            name = string
            nametype = 1
        elif (langname, strid) == (lang, 'WWS Family') and nametype < 2:
            name = string
            nametype = 2
        elif (langname, strid) == (lang, 'Preferred Family') and nametype < 3:
            name = string
            nametype = 3
    return name


def _getFontSubFamilyName(font: fontforge.font, lang: str = 'English (US)') -> str | None:
    name = font.weight if lang == 'English (US)' else None
    nametype = 0
    for langname, strid, string in font.sfnt_names:
        if (langname, strid) == (lang, 'SubFamily') and nametype < 1:
            name = string
            nametype = 1
        elif (langname, strid) == (lang, 'WWS Subfamily') and nametype < 2:
            name = string
            nametype = 2
        elif (langname, strid) == (lang, 'Preferred Styles') and nametype < 3:
            name = string
            nametype = 3
    return name


def _isFixedPitch(font: fontforge.font) -> bool:
    return len(
        set(
            map(
                lambda x: x.width,
                filter(
                    lambda x: 0x20 <= x.unicode <= 0x7e, font.glyphs()
                )
            )
        )
    ) == 1


def _hasBothRomanAndItalic(font: fontforge.font) -> bool:
    if utils.getVFValue(font, 'axes.ital.active', False):
        if _axisMinValue(font, 'ital') == 0 and _axisMaxValue(font, 'ital') == 1:
            return True
    return False


class _ufoInfo:
    from fontTools.ufoLib import fontInfoAttributesVersion3
    from itertools import repeat
    _data = dict(zip(list(fontInfoAttributesVersion3), repeat(None)))

    def __getattr__(self, name):
        if name in self._data:
            return self._data[name]
        else:
            raise AttributeError("attribute '{0}' not found".format(name))

    def __setattr__(self, name, value):
        if name in self._data:
            self._data[name] = value
        else:
            raise AttributeError("attribute '{0}' not found".format(name))


def _aaltExists(font: fontforge.font) -> bool:
    tags = []
    for i in font.gsub_lookups:
        for j in font.getLookupInfo(i)[2]:
            tags.append(j[0])
    return 'aalt' in tags


def _allGSUBTags(font: fontforge.font) -> set[str]:
    tags = []
    for i in font.gsub_lookups:
        for j in font.getLookupInfo(i)[2]:
            tags.append(j[0])
    return set(tags) - set(['aalt'])  # do not include 'aalt' itself


def _outputUfo(font: fontforge.font, outputDir: str | PathLike, outputFile: str | PathLike, aalt: bool):
    from fontTools.ufoLib import UFOReaderWriter
    import re
    # import shutil  # for debug

    assert outputFile.endswith('.ufo')
    ufoPath = str(outputDir) + '/' + str(outputFile)
    changed = font.changed
    unlinkRmOvrlpSave = {}
    for glyph in font.glyphs():
        unlinkRmOvrlpSave[glyph.glyphname] = glyph.unlinkRmOvrlpSave
        glyph.unlinkRmOvrlpSave = False
    font.generate(ufoPath)
    for glyph in font.glyphs():
        glyph.unlinkRmOvrlpSave = unlinkRmOvrlpSave[glyph.glyphname]
    if not isinstance(font.temporary, dict):
        font.temporary = dict()
    font.temporary['ufo'] = ufoPath

    with UFOReaderWriter(ufoPath) as ufo:
        info = _ufoInfo()
        ufo.readInfo(info)
        if _isFixedPitch(font):
            ufo.postscriptIsFixedPitch = True
        ufo.styleMapFamilyName = _getFontFamilyName(font)
        ufo.styleMapStyleName = _getFontSubFamilyName(font)
        ufo.writeInfo(info)

        if _aaltExists(font) or _allGSUBTags(font):
            feat = ufo.readFeatures()
            existingAalt = ''
            aaltPattern = r'(?s)\bfeature\s+aalt\s*\{\n?(.*)\}\s*aalt\*;\s*'
            featPosPattern = r'(?=feature\s+\w{1,4}\s*\{)'
            removeFromAaltPattern = r'(?m)^\s*(script|language)\s+.*?;\s*'
            if result := re.search(aaltPattern, feat):
                existingAalt = re.sub(removeFromAaltPattern, "", result[1])
                feat = re.sub(aaltPattern, "", feat)
            aaltInclude = ''
            if aalt:
                aaltInclude = "".join(['  feature ' + x + ';\n' for x in list(_allGSUBTags(font))])
            newAalt = ''
            if aaltInclude or existingAalt:
                newAalt = "feature aalt {\n" + aaltInclude + existingAalt + "} aalt;\n\n"
            feat = re.sub(featPosPattern, newAalt, feat, count=1)
            ufo.writeFeatures(feat)

    font.changed = changed

    # For debug
    # shutil.copyfile(ufoPath + "/fontinfo.plist", "./fontinfo.plist")
    # shutil.copyfile(ufoPath + "/features.fea", "./features.fea")


def _designSpaceSources(font: fontforge.font, doc: DesignSpaceDocument, filterItalicRoman: bool | None = None):
    # print(_getSourceFonts(font))
    for f in _getSourceFonts(font, filterItalicRoman):
        s = SourceDescriptor()
        s.path = f.temporary['ufo']
        if f is font:
            s.copyLib = True
            s.copyInfo = True
            s.copyGroups = True
            s.copyFeatures = True
        s.name = f.fullname
        s.font = f
        s.location = {}
        for k, v in designAxes.items():
            active = 'axes.' + k + '.active'
            if utils.getVFValue(font, active, False) and utils.getVFValue(f, active, False):
                tag = utils.getVFValue(font, 'axes.' + k + '.tag', '????') \
                    if k.startswith('custom') else k
                name = utils.getVFValue(font, 'axes.' + k + '.name', v['name']) \
                    if k.startswith('custom') else v['name']
                s.location[name] = getAxisValue(f, tag)
        s.familyName = _getFontFamilyName(f)
        s.styleName = _getFontSubFamilyName(f)
        s.localisedFamilyName = {}
        for i in set([L[0] for L in f.sfnt_names]) - set(['English (US)']):
            s.localisedFamilyName[language.languageCodeReverseLookup(i)] = _getFontFamilyName(f, i)
        doc.addSource(s)


def _designSpaceAxes_labels(labels, a: AxisDescriptor | DiscreteAxisDescriptor):
    L = []
    for u, d in labels.items():
        if not (a.minimum <= u <= a.maximum):
            fontforge.logWarning('Ignored label {0} = {1} because out of range'.format(
                a.name, str(u)))
        elif 'name' not in d:
            fontforge.logWarning('Ignored label {0} = {1} because no name set'.format(
                a.name, str(u)))
        else:
            al = AxisLabelDescriptor(name=d['name'], userValue=u)
            if 'elidable' in d:
                al.elidable = d['elidable']
            if 'linkedValue' in d:
                al.linkedUserValue = d['linkedValue']
            if 'localNames' in d:
                for lang, name in d['localNames'].items():
                    al.labelNames[lang] = name
            L.append(al)
    return L


def _designSpaceAxes(font: fontforge.font, doc: DesignSpaceDocument, filterItalicRoman: bool | None = None):
    for k, v in designAxes.items():
        if utils.getVFValue(font, 'axes.' + k + '.active', False):
            a = DiscreteAxisDescriptor() if k == 'ital' else AxisDescriptor()
            a.tag = utils.getVFValue(font, 'axes.' + k + '.tag', '????') \
                if k.startswith('custom') else k
            if k == 'ital' and filterItalicRoman is not None:
                a.minimum = 1 if filterItalicRoman else _axisMinValue(font, a.tag)
                a.maximum = 0 if not filterItalicRoman else _axisMaxValue(font, a.tag)
            else:
                a.minimum = _axisMinValue(font, a.tag)
                a.maximum = _axisMaxValue(font, a.tag)
            a.default = getAxisValue(font, a.tag)
            a.name = utils.getVFValue(font, 'axes.' + k + '.name', v['name'])
            for L, n in utils.getVFValue(font, 'axes.' + k + '.localNames', {}).items():
                a.labelNames[L] = n
            if val := utils.getVFValue(font, 'axes.' + k + '.map'):
                a.map = val
            if val := utils.getVFValue(font, 'axes.' + k + '.order'):
                a.axisOrdering = val
            if labels := utils.getVFValue(font, 'axes.' + k + '.labels'):
                a.axisLabels = _designSpaceAxes_labels(labels, a)
            doc.addAxis(a)


def _makeDesignSpace(
    font: fontforge.font,
    outputDir: str | PathLike,
    outputFile: str | PathLike,
    filterItalicRoman: bool | None = None
):
    # import shutil  # for debug

    doc = DesignSpaceDocument()
    _designSpaceSources(font, doc, filterItalicRoman)
    _designSpaceAxes(font, doc, filterItalicRoman)
    doc.write(str(outputDir) + '/' + str(outputFile))

    # For debug
    # shutil.copyfile(str(outputDir) + '/' + str(outputFile), "./" + str(outputFile))


def _doExportVF(
    font: fontforge.font,
    tmpdir,
    filename: str | PathLike,
    italicFilename: str | PathLike | None = None,
    options: list = [],
    need2files: bool = False
):
    from subprocess import run, CalledProcessError
    from sys import stderr

    try:
        result = run(['fontmake'] + options + [
            '-m', tmpdir + '/vf.designspace',
            '-o', 'variable', '--output-path', str(filename)],
            check=True, text=True, capture_output=fontforge.hasUserInterface())
        if fontforge.hasUserInterface():
            stderr.write(result.stderr)
        if need2files and italicFilename:
            result = run(['fontmake'] + options + [
                '-m', tmpdir + '/vf2.designspace',
                '-o', 'variable', '--output-path', str(italicFilename)],
                check=True, text=True, capture_output=fontforge.hasUserInterface())
            if fontforge.hasUserInterface():
                stderr.write(result.stderr)
    except CalledProcessError as e:
        if fontforge.hasUserInterface():
            fontforge.logWarning(e.stderr)
            fontforge.postError(
                "Failed to export",
                "fontmake failed with return code {0}".format(e.returncode)
            )
        else:
            raise
    else:
        if fontforge.hasUserInterface():
            fontforge.postNotice(
                "Finished",
                "fontmake finished to output variable fonts"
            )


def exportVariableFont(
    font: fontforge.font,
    filename: str | PathLike,
    italicFilename: str | PathLike | None = None,
    decomposeNestedRefs: bool = False,
    addAalt: bool = False
):
    """Exports variable font

    Before this function being called, make sure all masters are open and
    parameters of design axes and instances are set, and also family name
    is consistent. VF-specific metadata must be stored in
    ``font.persistent['VF']``. Other metadata can be set as usual.

    This function uses 'fonttools' module and calls 'fontmake' tool as
    the backend to export the variable font.

    In order to build a variable font, SFD must be converted into UFO and
    create a designspace document. This function will do this first, and
    then required modification. The required files will be created in a
    temporary directory, and deleted after everything is done. So users
    won't see intermediate files.

    Fontforge may export with ``postscriptIsFixedPitch`` flag clear when
    it should be set. The plugin checks if monospaced font is intended and
    fix the flag. Unlike Fontforge itself, only U+0020 to U+007E will be
    checked their width, because combining marks may have zero width even
    for monospaced fonts.

    In a feature file, 'aalt' feature is specially treated. Fontforge may
    export incompatible 'aalt' feature (concretely 'script' or 'language'
    instructions must not be included unlike other features.) This
    function fix this first.

    :param font: Main font which font-family-wide parameters are set.
  . Fontforge font object.
    :param filename: Output file name. Must end with '.ttf'.
    :param italicFilename: Secondary output file name for italic. Must
    end with '.ttf'. Required if the font family has both roman and
    italic styles
    :param decomposeNestedRefs: Optional. Nested references are known to
    cause problems in certain environments; if ``True``, resulting font
    will decompose such references. Defaults to ``False``.
    :param addAalt: Adds 'aalt' feature. Defaults to ``False``.
    :raises ``CalledProcessError``: 'fontmake' ended abnormally. For
    example, it is an error if inconsistent number of points or contours
    among masters.
    """
    assert str(filename).endswith('.ttf')
    need2files = False
    if _hasBothRomanAndItalic(font):
        need2files = True
        assert (italicFilename is None) or (str(italicFilename).endswith('.ttf'))
    with tempfile.TemporaryDirectory() as tmpdir:
        s = 0
        for f in _getSourceFonts(font):
            s += 1
            _outputUfo(f, tmpdir, 'source' + str(s) + '.ufo', addAalt)
        if need2files:
            _makeDesignSpace(font, tmpdir, 'vf.designspace', False)
            if italicFilename:
                _makeDesignSpace(font, tmpdir, 'vf2.designspace', True)
        else:
            _makeDesignSpace(font, tmpdir, 'vf.designspace')
        options = []
        if decomposeNestedRefs:
            options.append('-f')
        _doExportVF(font, tmpdir, filename, italicFilename, options, need2files)


def _exportVariableFont(font: fontforge.font, dialogResult: dict[str, str]):
    decomposeNestedRefs = False
    addAalt = False
    secondaryFile = None
    if 'options' in dialogResult:
        for opt in dialogResult['options']:
            if opt == 'nestedRefs':
                decomposeNestedRefs = True
            if opt == 'aalt':
                addAalt = True
    if 'file2' in dialogResult:
        secondaryFile = dialogResult['file2']
    exportVariableFont(font, dialogResult['file'], secondaryFile, decomposeNestedRefs, addAalt)


def _saveMenuDialog(font: fontforge.font) -> dict | None:
    if _hasBothRomanAndItalic(font):
        questions = [
            {
                'type': 'savepath', 'question': 'Roman VF:', 'tag': 'file',
                'default':
                    font.default_base_filename + '.ttf' if font.default_base_filename
                    else '.'.join(font.path.split('.')[:-1]) + '.ttf',
                'filter': '*.ttf',
            },
            {
                'type': 'savepath', 'question': 'Italic VF:', 'tag': 'file2',
                'default':
                    font.default_base_filename + '-Italic.ttf' if font.default_base_filename
                    else '.'.join(font.path.split('.')[:-1]) + '-Italic.ttf',
                'filter': '*.ttf',
            },
        ]
    else:
        questions = [
            {
                'type': 'savepath', 'question': 'Save as:', 'tag': 'file',
                'default':
                    font.default_base_filename + '.ttf' if font.default_base_filename
                    else '.'.join(font.path.split('.')[:-1]) + '.ttf',
                'filter': '*.ttf',
            },
        ]
    questions += [
        {
            'type': 'choice', 'question': 'Options:', 'tag': 'options',
            'checks': True, 'multiple': True,
            'answers': [
                {'name': 'Remove nested refs', 'tag': 'nestedRefs'},
                {'name': "Add 'aalt' feature", 'tag': 'aalt'},
            ],
        },
    ]
    return fontforge.askMulti("Save variable font", questions)


def saveMenu(u, glyph):
    if result := _saveMenuDialog(fontforge.activeFont()):
        _exportVariableFont(fontforge.activeFont(), result)


def saveEnable(u, glyph):
    return utils.vfInfoExists(fontforge.activeFont())
