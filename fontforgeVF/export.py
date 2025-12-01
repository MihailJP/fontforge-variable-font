from fontforgeVF import utils, language
from fontforgeVF.design_axes import designAxes, getAxisValue
import fontforge
import tempfile
from subprocess import run, CalledProcessError
from fontTools.designspaceLib import \
    DesignSpaceDocument, SourceDescriptor, \
    AxisDescriptor, DiscreteAxisDescriptor, AxisLabelDescriptor

def _getSourceFonts(defaultFont: fontforge.font) -> list[fontforge.font]:
    return list(filter(lambda f: f.familyname == defaultFont.familyname, fontforge.fonts()))


def _axisMinValue(defaultFont: fontforge.font, tag: str) -> int | float:
    return min(filter(lambda x: x is not None,
        map(lambda f: getAxisValue(f, tag), _getSourceFonts(defaultFont))))


def _axisMaxValue(defaultFont: fontforge.font, tag: str) -> int | float:
    return max(filter(lambda x: x is not None,
        map(lambda f: getAxisValue(f, tag), _getSourceFonts(defaultFont))))


def _getFontFamilyName(font: fontforge.font, lang: str = 'English (US)') -> str | None:
    name = font.familyname if lang == 'English (US)' else None
    nametype = 0
    for language, strid, string in font.sfnt_names:
        if (language, strid) == (lang, 'Family') and nametype < 1:
            name = string
            nametype = 1
        elif (language, strid) == (lang, 'WWS Family') and nametype < 2:
            name = string
            nametype = 2
        elif (language, strid) == (lang, 'Preferred Family') and nametype < 3:
            name = string
            nametype = 3
    return name

            
def _getFontSubFamilyName(font: fontforge.font, lang: str = 'English (US)') -> str | None:
    name = font.weight if lang == 'English (US)' else None
    nametype = 0
    for language, strid, string in font.sfnt_names:
        if (language, strid) == (lang, 'SubFamily') and nametype < 1:
            name = string
            nametype = 1
        elif (language, strid) == (lang, 'WWS Subfamily') and nametype < 2:
            name = string
            nametype = 2
        elif (language, strid) == (lang, 'Preferred Styles') and nametype < 3:
            name = string
            nametype = 3
    return name


def _outputUfo(font: fontforge.font, outputDir: str, outputFile: str):
    assert(outputFile.endswith('.ufo'))
    font.generate(outputDir + '/' + outputFile)
    if not isinstance(font.temporary, dict):
        font.temporary = dict()
    font.temporary['ufo'] = outputDir + '/' + outputFile


def _designSpaceSources(font: fontforge.font, doc: DesignSpaceDocument):
    for f in _getSourceFonts(font):
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
        for i in set([l[0] for l in f.sfnt_names]) - set(['English (US)']):
            s.localisedFamilyName[language.languageCodeReverseLookup(i)] = _getFontFamilyName(f, i)
        doc.addSource(s)


def _designSpaceAxes(font: fontforge.font, doc: DesignSpaceDocument):
    for k, v in designAxes.items():
        if utils.getVFValue(font, 'axes.' + k + '.active', False):
            a = DiscreteAxisDescriptor() if k == 'ital' else AxisDescriptor()
            a.tag = utils.getVFValue(font, 'axes.' + k + '.tag', '????') \
                if k.startswith('custom') else k
            a.minimum = _axisMinValue(font, a.tag)
            a.maximum = _axisMaxValue(font, a.tag)
            a.default = getAxisValue(font, a.tag)
            a.name = utils.getVFValue(font, 'axes.' + k + '.name', v['name'])
            for l, n in utils.getVFValue(font, 'axes.' + k + '.localNames', {}).items():
                a.labelNames[l] = n
            if val := utils.getVFValue(font, 'axes.' + k + '.map'):
                a.map = val
            if val := utils.getVFValue(font, 'axes.' + k + '.order'):
                a.axisOrdering = val
            if labels := utils.getVFValue(font, 'axes.' + k + '.labels'):
                l = []
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
                        l.append(al)
                a.axisLabels = l
            doc.addAxis(a)


def _makeDesignSpace(font: fontforge.font, outputDir: str, outputFile: str):
    doc = DesignSpaceDocument()
    _designSpaceSources(font, doc)
    _designSpaceAxes(font, doc)
    doc.write(outputDir + '/' + outputFile)


def exportVariableFont(font: fontforge.font, dialogResult: dict[str, str]):
    """Exports variable font"""
    assert(dialogResult['file'].endswith('.ttf'))
    with tempfile.TemporaryDirectory() as tmpdir:
        s = 0
        for f in _getSourceFonts(font):
            s += 1
            _outputUfo(font, tmpdir, 'source' + str(s) + '.ufo')
        _makeDesignSpace(font, tmpdir, 'vf.designspace')
        options = []
        if 'options' in dialogResult:
            for opt in dialogResult['options']:
                if opt == 'nestedRefs':
                    options.append('-f')
        try:
            run(['fontmake'] + options + [
                '-m', tmpdir + '/vf.designspace',
                '-o', 'variable', '--output-path', dialogResult['file']],
                check=True, text=True, capture_output=True)
        except CalledProcessError as e:
            fontforge.logWarning(e.stderr)
            fontforge.postError("Failed to export",
                "fontmake failed with return code {0}".format(e.returncode))


def _saveMenuDialog(font: fontforge.font) -> dict | None:
    questions = [
        {
            'type': 'savepath', 'question': 'Save as:', 'tag': 'file',
            'default': font.default_base_filename + '.ttf' if font.default_base_filename else \
                '.'.join(font.path.split('.')[:-1]) + '.ttf',
            'filter': '*.ttf',
        },
        {
            'type': 'choice', 'question': 'Options:', 'tag': 'options',
            'checks': True, 'multiple': True,
            'answers': [
                {'name': 'Remove nested refs', 'tag': 'nestedRefs'},
            ],
        },
    ]
    return fontforge.askMulti("Save variable font", questions)


def saveMenu(u, glyph):
    if result := _saveMenuDialog(fontforge.activeFont()):
        exportVariableFont(fontforge.activeFont(), result)


def saveEnable(u, glyph):
    return True
