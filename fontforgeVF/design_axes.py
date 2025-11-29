from fontforgeVF import utils
import fontforge

designAxes = {
    "ital":    {"name": "Italic",       "auto": lambda font: font.italicangle < 0},
    "opsz":    {"name": "Optical Size", "auto": lambda font: font.design_size},
    "slnt":    {"name": "Slant",        "auto": lambda font: font.italicangle},
    "wdth":    {"name": "Width",        "auto": lambda font: [50, 62.5, 75, 87.5, 100, 112.5, 125, 150, 200][font.os2_width - 1]},
    "wght":    {"name": "Weight",       "auto": lambda font: font.os2_weight},
    "custom1": {"name": "Custom 1",     "auto": None},
    "custom2": {"name": "Custom 2",     "auto": None},
    "custom3": {"name": "Custom 3",     "auto": None},
}


def _prepareQuestions():
    font = fontforge.activeFont()
    questions =  [
        {
            'category': 'This master',
            'questions': [],
        },
        {
            'category': 'Custom axes',
            'questions': [],
        },
    ]
    for k, v in designAxes.items():
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
                { 'name': 'Unset', 'tag': 'unset', 'default': tagStat == 0 },
                { 'name': 'Set', 'tag': 'custom', 'default': tagStat == 1 },
            ] + ([
                { 'name': 'Default (' + str(v["auto"](font)) + ')', 'tag': 'auto', 'default': tagStat == 2 },
            ] if v["auto"] else []),
        })
        if k == 'ital':
            questions[0]["questions"].append({
                'type': 'choice',
                'question': '',
                'tag': k + 'val',
                'checks': True,
                'answers': [
                    { 'name': 'No', 'tag': 'false', 'default': not tagVal },
                    { 'name': 'Yes', 'tag': 'true', 'default': tagVal },
                ],
            })
        else:
            questions[0]["questions"].append({
                'type': 'string',
                'question': '',
                'tag': k + 'val',
                'default': str(tagVal),
            })

        if k.startswith('custom'):
            questions[1]["questions"].append({
                'type': 'string',
                'question': v["name"] + ' tag:',
                'tag': k + 'tag',
                'default': '',
            })
    return questions


def _saveResult(result):
    font = fontforge.activeFont()
    for k, v in designAxes.items():
        utils.setVFValue(font, 'axes.' + k + '.active', result[k] != 'unset')
        if not k.startswith('custom') and result[k] != 'unset':
            utils.setVFValue(font, 'axes.' + k + '.useDefault', result[k] == 'auto')
        else:
            utils.deleteVFValue(font, 'axes.' + k + '.useDefault')
        if result[k] == 'custom':
            utils.setVFValue(font, 'axes.' + k + '.value', result[k + 'val'] == 'true' if k == 'ital' else utils.intOrFloat(result[k + 'val']))
        else:
            utils.deleteVFValue(font, 'axes.' + k + '.value')
        if k.startswith('custom'):
            utils.setOrDeleteVFValue(font, 'axes.' + k + '.tag', result[k + 'tag'])
    #print(result)
    #print(font.persistent)


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
    """
    result = fontforge.askMulti("Design axes", _prepareQuestions())
    if result:
        _saveResult(result)


def designAxesEnable(u, glyph):
    return True
