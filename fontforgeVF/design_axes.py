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


def designAxesMenu(u, glyph):
    """Menu entry to interactively set design axes for active font

    Opens a dialog to set design axes of active font. Requires UI.

    This master
    -----------

    This section is needed for all masters.

    For active font as one of VF masters, sets position in each design
    axis of VF master. Leave unset for unused axes. Registered axes can
    use default values which refers font properties.

    * Italic: default value is whether `font.italicangle` is negative.
      This axis is boolean: you choose the master is for italic or not.
      Seldom used together with slant axis.
    * Optical size: can default to `font.design_size`. Set in points.
      Must be positive.
    * Slant: can default to `font.italicangle`. 0 if upright, negative if
      oblique. This value is hardly positive (left-slanted.)
    * Width: can default using `font.os2_width`. 100 if normal width, less
      if condensed, greater if expanded. Must be positive.
    * Weight: can default to `font.os2_weight`. 400 if regular weight, 700
      if bold. The minimum is 1 (hairline thin) and the maximum is 999
      (extreme bold.)
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
        questions[0]["questions"].append({
            'type': 'choice',
            'question': v["name"] + ':',
            'tag': k,
            'checks': True,
            'answers': [
                { 'name': 'Unset', 'tag': 'unset', 'default': True },
                { 'name': 'Set', 'tag': 'custom' },
            ] + ([
                { 'name': 'Default (' + str(v["auto"](fontforge.activeFont())) + ')', 'tag': 'auto' },
            ] if v["auto"] else []),
        })
        if k == 'ital':
            questions[0]["questions"].append({
                'type': 'choice',
                'question': '',
                'tag': k + 'val',
                'checks': True,
                'answers': [
                    { 'name': 'No', 'tag': 'false', 'default': not v["auto"](fontforge.activeFont()) },
                    { 'name': 'Yes', 'tag': 'true', 'default': v["auto"](fontforge.activeFont()) },
                ],
            })
        else:
            questions[0]["questions"].append({
                'type': 'string',
                'question': '',
                'tag': k + 'val',
                'default': str(v["auto"](fontforge.activeFont())) if v["auto"] else '0',
            })

        if k.startswith('custom'):
            questions[1]["questions"].append({
                'type': 'string',
                'question': v["name"] + ' tag:',
                'tag': k + 'tag',
                'default': '',
            })

    result = fontforge.askMulti("Design axes", questions)
    #print(result)


def designAxesEnable(u, glyph):
    return True
