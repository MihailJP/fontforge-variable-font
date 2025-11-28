import fontforge

def initPersistentDict(font: fontforge.font) -> bool:
    """Make sure `font.persistent` is a `dict`

    If `font.persistent` is a `dict`, does nothing. Otherwise sets it to
    an empty `dict`.

    In case there is already non-`dict` `font.persistent`, if UI is
    active, asks the user before deletes it. If not running interactively,
    it will be deleted without warning.

    Returns `False` if the user refuses to delete existing
    `font.persistent`, `True` otherwise.
    """
    if font.persistent is None:
        font.persistent = {}
    elif not isinstance(font.persistent, dict):
        fontforge.logWarning("Non-dict `font.persistent` will be lost")
        if fontforge.hasUserInterface():
            if fontforge.ask("Data loss warning", "In active font, `font.persistent` exists but is other than a dict.\nThis will be overwritten if you continue.", ("_OK", "_Cancel"), 0, 1) == 1:
                return False
        font.persistent = {}
    # Do nothing if font.persistent is a dict
    return True
