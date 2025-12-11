from fontforgeVF import utils, language
import fontforge


__all__ = [
    "getAxisValue",
]


def _getWidthFromOS2Width(font: fontforge.font) -> int | float:
    return [50, 62.5, 75, 87.5, 100, 112.5, 125, 150, 200][font.os2_width - 1]


designAxes = {  # noqa: E241
    "ital":    {"name": "Italic",       "auto": lambda font: font.italicangle < 0},
    "opsz":    {"name": "Optical Size", "auto": lambda font: font.design_size},
    "slnt":    {"name": "Slant",        "auto": lambda font: font.italicangle},
    "wdth":    {"name": "Width",        "auto": lambda font: _getWidthFromOS2Width(font)},
    "wght":    {"name": "Weight",       "auto": lambda font: font.os2_weight},
    "custom1": {"name": "Custom 1",     "auto": None},
    "custom2": {"name": "Custom 2",     "auto": None},
    "custom3": {"name": "Custom 3",     "auto": None},
}


def _searchCustomAxis(font: fontforge.font, tag: str) -> str | None:
    if tag in designAxes:  # predefined tag
        return tag
    else:
        for k, v in designAxes.items():
            if k.startswith('custom') and utils.getVFValue(font, 'axes.' + k + '.tag', '').rstrip() == tag.rstrip():
                return k
        return None


def getAxisValue(font: fontforge.font, tag: str) -> int | float | None:
    """Gets a value from a design axis"""
    internalTag = _searchCustomAxis(font, tag)
    if internalTag is None:
        return None
    elif not utils.getVFValue(font, 'axes.' + internalTag + '.active'):
        return None
    elif utils.getVFValue(font, 'axes.' + internalTag + '.useDefault'):
        if internalTag == 'ital':
            return int(designAxes[internalTag]['auto'](font))
        else:
            return designAxes[internalTag]['auto'](font)
    else:
        return utils.getVFValue(font, 'axes.' + internalTag + '.value')


def _loadLabels(tag: str, lang=None):
    font = fontforge.activeFont()
    addr = 'axes.' + tag + '.labels'
    if label := utils.getVFValue(font, addr):
        text = ''
        assert isinstance(label, dict)
        for k, v in label.items():
            labelAddr = addr + '.' + str(k).replace('.', ',')  # escape decimal point
            if lang:
                text += str(k) + ',' + \
                    utils.getVFValue(font, labelAddr + '.localNames.' + hex(lang), '') + \
                    ', '
            else:
                text += str(k) + ',' + \
                    ('1' if utils.getVFValue(font, labelAddr + '.elidable', False) else '0') + \
                    ',' + str(utils.getVFValue(font, labelAddr + '.linkedValue', '')) + \
                    ',' + utils.getVFValue(font, labelAddr + '.name', '') + \
                    ', '
        return text[:-2]
    elif utils.vfInfoExists(font):
        return ''
    elif lang:
        return ''
    elif tag == 'wdth':
        return '50,,,Ultra Condensed, ' \
            '62.5,,,Extra Condensed, ' \
            '75,,,Condensed, ' \
            '87.5,,,Semi-Condensed, ' \
            '100,1,,Medium, ' \
            '112.5,,,Semi-Expanded, ' \
            '125,,,Expanded, ' \
            '150,,,Extra Expanded, ' \
            '200,,,Ultra Expanded'
    elif tag == 'wght':
        return '100,,,Thin, 200,,,Extra Light, 300,,,Light, ' \
            '400,0,700,Regular, 500,,,Medium, 600,,,Semi-Bold, ' \
            '700,,,Bold, 800,,,Extra Bold, 900,,,Black'
    elif tag == 'ital':
        return '0,1,1,Roman, 1,0,0,Italic'
    else:
        return ''


# Load values and make dialog components
def _prepareQuestions_languages(questions):
    font = fontforge.activeFont()
    languages = set()
    for k, v in designAxes.items():
        languages |= set(utils.getVFValue(font, 'axes.' + k + '.localNames', {}).keys())
    languages = tuple(languages)
    localNameCategory = len(questions)
    localNameRange = range(1, max(((len(languages) + 7) // 4) * 4, 8)+1)
    for i in localNameRange:
        defaultCode = languages[i-1] if i <= len(languages) else ''
        languageList = [
            {'name': '', 'tag': '', 'default': defaultCode == ''}
        ]
        for langId, langCode, langName in sorted(language.languageCodeIterator(), key=lambda x: x[2]):
            languageList.append({'name': langName, 'tag': hex(langId), 'default': langId == defaultCode})
        questions.append({
            'category': 'Localized names ' + (
                language.languageCodeLookup(languages[i-1]) if i <= len(languages) else str(i)
            ),
            'questions': [
                {
                    'type': 'choice',
                    'question': 'Language:',
                    'tag': 'lang' + str(i),
                    'answers': languageList,
                },
            ],
        })
    return languages, localNameCategory, localNameRange


def _prepareQuestions_values(questions, k, v):
    font = fontforge.activeFont()
    tagStat = 1 if utils.getVFValue(font, 'axes.' + k + '.active', False) else 0
    if tagStat == 1 and not k.startswith('custom') and utils.getVFValue(font, 'axes.' + k + '.useDefault', False):
        tagStat = 2
    defaultTagVal = v["auto"](font) if v["auto"] else 0
    tagVal = utils.getVFValue(font, 'axes.' + k + '.value', defaultTagVal) if tagStat == 1 else defaultTagVal
    questions[0]["questions"].append({
        'type': 'choice',
        'question': v["name"] + ':',
        'tag': k,
        'checks': True,
        'answers': [
            {'name': 'Unset', 'tag': 'unset', 'default': tagStat == 0},
            {'name': 'Set', 'tag': 'custom', 'default': tagStat == 1},
        ] + ([
            {'name': 'Default (' + str(v["auto"](font)) + ')', 'tag': 'auto', 'default': tagStat == 2},
        ] if v["auto"] else []),
    })
    if k == 'ital':
        questions[0]["questions"].append({
            'type': 'choice',
            'question': '',
            'tag': k + 'val',
            'checks': True,
            'answers': [
                {'name': 'No', 'tag': 'false', 'default': not tagVal},
                {'name': 'Yes', 'tag': 'true', 'default': tagVal},
            ],
        })
    else:
        questions[0]["questions"].append({
            'type': 'string',
            'question': '',
            'tag': k + 'val',
            'default': str(tagVal),
        })


def _prepareQuestions_map(questions, k, v):
    font = fontforge.activeFont()
    questions[2]["questions"].append({
        'type': 'string',
        'question': v["name"] + ':',
        'tag': k + 'map',
        'default': ', '.join(list(map(
            lambda x: str(x[0]) + ',' + str(x[1]),
            utils.getVFValue(font, 'axes.' + k + '.map', [])
        ))),
    })


def _prepareQuestions_order(questions, k, v):
    font = fontforge.activeFont()
    questions[3]["questions"].append({
        'type': 'string',
        'question': v["name"] + ':',
        'tag': k + 'order',
        'default': str(utils.getVFValue(font, 'axes.' + k + '.order', '')),
    })


def _prepareQuestions_names(questions, k, v):
    font = fontforge.activeFont()
    questions[4]["questions"].append({
        'type': 'string',
        'question': v["name"] + ':',
        'tag': k + 'name',
        'default': utils.getVFValue(
            font,
            'axes.' + k + '.name',
            '' if utils.vfInfoExists(font) or k.startswith('custom') else v["name"]
        ),
    })
    questions[4]["questions"].append({
        'type': 'string',
        'question': '\tLabels:',
        'tag': k + 'labels',
        'default': _loadLabels(k),
    })


def _prepareQuestions_localNames(questions, k, v, languages, localNameRange, localNameCategory):
    font = fontforge.activeFont()
    for i in localNameRange:
        questions[localNameCategory + i - 1]["questions"].append({
            'type': 'string',
            'question': v["name"] + ':',
            'tag': k + 'name' + str(i),
            'default': utils.getVFValue(
                font, 'axes.' + k + '.localNames.' + hex(languages[i-1]), ''
            ) if i <= len(languages) else '',
        })
        questions[localNameCategory + i - 1]["questions"].append({
            'type': 'string',
            'question': '\tLabels:',
            'tag': k + 'labels' + str(i),
            'default': _loadLabels(k, languages[i-1]) if i <= len(languages) else '',
        })


def _prepareQuestions_custom(questions, k, v):
    if k.startswith('custom'):
        questions[1]["questions"].append({
            'type': 'string',
            'question': v["name"] + ' tag:',
            'tag': k + 'tag',
            'default': '',
        })


def _prepareQuestions():
    questions = [
        {'category': 'This master', 'questions': []},
        {'category': 'Custom axes', 'questions': []},
        {'category': 'Axis map',    'questions': []},
        {'category': 'Axis order',  'questions': []},
        {'category': 'Axis names',  'questions': []},
    ]

    languages, localNameCategory, localNameRange = _prepareQuestions_languages(questions)
    for k, v in designAxes.items():
        _prepareQuestions_values(questions, k, v)
        _prepareQuestions_map(questions, k, v)
        _prepareQuestions_order(questions, k, v)
        _prepareQuestions_names(questions, k, v)
        _prepareQuestions_localNames(questions, k, v, languages, localNameRange, localNameCategory)
        _prepareQuestions_custom(questions, k, v)
    return questions


# Save result
def _saveResult_values(result, k, v):
    font = fontforge.activeFont()
    utils.setVFValue(font, 'axes.' + k + '.active', result[k] != 'unset')
    if not k.startswith('custom') and result[k] != 'unset':
        utils.setVFValue(font, 'axes.' + k + '.useDefault', result[k] == 'auto')
    else:
        utils.deleteVFValue(font, 'axes.' + k + '.useDefault')
    if result[k] == 'custom':
        utils.setVFValue(
            font, 'axes.' + k + '.value',
            result[k + 'val'] == 'true' if k == 'ital' else utils.intOrFloat(result[k + 'val']))
    else:
        utils.deleteVFValue(font, 'axes.' + k + '.value')
    if k.startswith('custom'):
        utils.setOrDeleteVFValue(font, 'axes.' + k + '.tag', result[k + 'tag'])


def _saveResult_labels(result, k, v):
    font = fontforge.activeFont()
    utils.setOrDeleteVFValue(font, 'axes.' + k + '.order', int(result[k + 'order']) if result[k + 'order'] else None)
    utils.deleteVFValue(font, 'axes.' + k + '.labels')
    if result[k + 'labels']:
        for val, el, lv, name in list(map(
            lambda x: (x[0][0].strip(), x[0][1].strip(), x[1][0].strip(), x[1][1].strip()),
            zip(_x := zip(_x := iter(result[k + 'labels'].split(',')), _x), _x)
        )):
            val = val.replace('.', ',')  # escape decimal point
            valAddr = 'axes.' + k + '.labels.' + val
            utils.setOrDeleteVFValue(font, valAddr + '.elidable',
                                     None if el == '' else bool(utils.intOrFloat(el)))
            utils.setOrDeleteVFValue(font, valAddr + '.linkedValue',
                                     None if lv == '' else utils.intOrFloat(lv))
            utils.setOrDeleteVFValue(font, valAddr + '.name',
                                     None if name == '' else name)
            utils.deleteVFValue(font, 'axes.' + k + '.labels.' + val + '.localNames')
    for i in list(map(lambda x: x.replace('lang', ''), filter(lambda x: x.startswith('lang'), result))):
        if result['lang' + i] and result[k + 'labels' + i]:
            for val, name in list(zip(_x := iter(result[k + 'labels' + i].split(',')), _x)):
                val = val.replace('.', ',')  # escape decimal point
                utils.setOrDeleteVFValue(
                    font, 'axes.' + k + '.labels.' + val + '.localNames.' + result['lang' + i],
                    None if name == '' else name)


def _saveResult_localNames(result, k, v):
    font = fontforge.activeFont()
    utils.setOrDeleteVFValue(font, 'axes.' + k + '.name', result[k + 'name'])
    utils.deleteVFValue(font, 'axes.' + k + '.localNames')
    for i in list(map(lambda x: x.replace('lang', ''), filter(lambda x: x.startswith('lang'), result))):
        if result['lang' + i]:
            utils.setOrDeleteVFValue(
                font, 'axes.' + k + '.localNames.' + result['lang' + i],
                result[k + 'name' + i])


def _saveResult(result):
    for k, v in designAxes.items():
        _saveResult_values(result, k, v)
        _saveResult_labels(result, k, v)
        _saveResult_localNames(result, k, v)

    # Debug output
    # print(result)
    # print(font.persistent)


# Show dialog
def designAxesMenu(u, glyph):
    """Menu entry to interactively set design axes for active font

    Opens a dialog to set design axes of active font. Requires UI.

    This master
    -----------

    This section is needed for all masters.

    For active font as one of VF masters, sets position in each design
    axis of VF master. Leave unset for unused axes. Registered axes can
    use default values which refers font properties.

    * Italic: default value is whether ``font.italicangle`` is negative.
      This axis is boolean: you choose the master is for italic or not.
      Seldom used together with slant axis.
    * Optical size: can default to ``font.design_size``. Set in points.
      Must be positive.
    * Slant: can default to ``font.italicangle``. 0 if upright, negative
      if oblique. This value is hardly positive (left-slanted.)
    * Width: can default using ``font.os2_width``. 100 if normal width,
      less if condensed, greater if expanded. Must be positive.
    * Weight: can default to ``font.os2_weight``. 400 if regular weight,
      700 if bold. The minimum is 1 (hairline thin) and the maximum is
      999 (extreme bold.)
    * Custom axes: there is a room for 3 user-defined axes. No default
      values.

    Custom axes
    -----------

    This section is needed for default master (choose one master as
    default.)

    Sets the tag for each custom axis. A tag must be up to 4-letter
    alphanumeric. Will be padded with implicit trailing spaces. Leave
    them blank if not used.

    Axis order
    ----------

    This section is needed for default master (choose one master as
    default.)

    Sets the order of design axes.

    Axis map
    --------

    This section is needed for default master (choose one master as
    default.)

    Maps user position to design position.

    Input must be comma-separated values and even number of elements.
    Each pair consists of user and design positions in this order.

    Axis name
    ---------

    This section is needed for default master (choose one master as
    default.)

    Names the design axes. For predefined axes can use default name.
    Custom axes must be named if used.

    * Axis name: name of axis itself.
    * Labels: comma-separated list which consists of multiple of 4 of
      elements. Leading and trailing spaces will be trimmed. Every
      group of 4 elements:

      * Axis value
      * Whether label name is elidable (1 if so, 0 if not)
      * Linked value if exist
      * Name

    Localized names
    ---------------

    This section is needed for default master (choose one master as
    default.)

    Design axes can have translated names. Each page for each language.
    Set language code before you use. Choose a language from the list.

    By default there is a room for 8 languages, but this will be
    extended if already more than 4 languages are defined.

    * Axis name: name of axis itself.
    * Labels: comma-separated list which consists of even number of
      elements. Leading and trailing spaces will be trimmed. Every
      pair of elements:

      * Axis value
      * Name
    """
    result = fontforge.askMulti("Design axes", _prepareQuestions())
    if result:
        _saveResult(result)


def designAxesEnable(u, glyph):
    return True
