import fontforge


__all__ = [
    "intOrFloat",
    "initPersistentDict",
    "vfInfoExists",
    "getVFValue",
    "setVFValue",
    "deleteEmptyDicts",
    "deleteVFValue",
    "setOrDeleteVFValue",
]


def intOrFloat(val):
    """Convert to ``int`` or ``float`` if possible

    If parameter represents an integer, returns it converted to ``int``
    type. Applies to not only ``int`` type, but also ``float`` type
    with zero fractional part or ``str`` looking like an integer. If
    parameter represents a fractional, returns in ``float`` type.
    Otherwise, returns the parameter as is.
    """
    f = 0.0
    i = 0
    try:
        f = float(val)
    except ValueError:
        return val
    try:
        i = int(val)
    except ValueError:
        return f
    if f == i:
        return i
    else:
        return f


def initPersistentDict(font: fontforge.font):
    """Make sure ``font.persistent`` is a ``dict``

    If ``font.persistent`` is a ``dict``, does nothing. Otherwise sets
    it to an empty ``dict``.

    In case there is already non-``dict`` ``font.persistent``, if UI is
    active, asks the user before deletes it. If not running
    interactively, it will be deleted without warning.

    :raises ``RuntimeError``: user refused to delete existing
    ``font.persistent``.
    """
    if font.persistent is None:
        font.persistent = {}
    elif not isinstance(font.persistent, dict):
        fontforge.logWarning("Non-dict `font.persistent` will be lost")
        if fontforge.hasUserInterface():
            if fontforge.ask(
                "Data loss warning",
                "In active font, `font.persistent` exists but is other than a dict.\n"
                "This will be overwritten if you continue.",
                ("_OK", "_Cancel"), 0, 1
            ) == 1:
                raise RuntimeError("user refused to delete existing `font.persistent`")
        font.persistent = {}
    if 'VF' not in font.persistent:
        font.persistent['VF'] = {}
    elif not isinstance(font.persistent['VF'], dict):
        font.persistent['VF'] = {}


def vfInfoExists(font: fontforge.font) -> bool:
    """Check if VF info exists

    Check if ``font.persistent`` is a ``dict`` and ``VF`` key is in it.

    :return: ``True`` if VF info exists, ``False`` if not.
    """
    if font.persistent is None:
        return False
    elif not isinstance(font.persistent, dict):
        return False
    elif 'VF' not in font.persistent:
        return False
    else:
        return True


def getVFValue(font: fontforge.font, key: str, default=None):
    """Gets a value from VF info

    Gets a value from nested ``dict`` in ``font.persistent.VF``. If
    given key does not exist, uses default value.

    :param font: Fontforge font object
    :param key: Name of key. Use dots for nested ``dict`` like
    ``axes.wght``. Numeric keys are recognized and stored as numeric
    (``int`` or ``float``). If key name itself contains a dot, escape
    it to ``\\ufdd0``.
    :param default: Optional. Returns this value if ``key`` does not
    exist. Without this parameter defaults to ``None``.
    :return: the value for ``key``, or ``default`` if no such ``key``.
    """
    if not vfInfoExists(font):
        return default
    else:
        info = font.persistent["VF"]
        for k in key.split('.'):
            k = intOrFloat(k.replace('\ufdd0', '.'))
            if not isinstance(info, dict):
                return default
            elif k not in info:
                return default
            else:
                info = info[k]
        return info


def setVFValue(font: fontforge.font, key: str, val):
    """Sets a value in VF info

    Sets a value in a nested ``dict`` in ``font.persistent.VF``. If
    given key does not exist, it is recursively created.

    :param font: Fontforge font object
    :param key: Name of key. Use dots for nested ``dict`` like
    ``axes.wght``. Numeric keys are recognized and stored as numeric
    (``int`` or ``float``). If key name itself contains a dot, escape
    it to ``\\ufdd0``.
    :param val: A value to set. this can be anything picklable.
    :raises ``RuntimeError``: user refused ``initPersistentDict``.
    """
    initPersistentDict(font)
    info = font.persistent["VF"]
    for k in key.split('.')[:-1]:
        k = intOrFloat(k.replace('\ufdd0', '.'))
        if k not in info:
            info[k] = dict()
        elif not isinstance(info[k], dict):
            info[k] = dict()
        info = info[k]
    info[key.split('.')[-1]] = val


def deleteEmptyDicts(d: dict):
    """Recursively deletes empty ``dict``s in ``dict``"""
    if isinstance(d, dict):
        keys = list(d.keys())
        for k in keys:
            k = intOrFloat(k)
            if isinstance(d[k], dict):
                deleteEmptyDicts(d[k])
                if len(d[k]) == 0:
                    del d[k]


def deleteVFValue(font: fontforge.font, key: str) -> bool:
    """Deletes a key and the associated value from VF info

    Sets a value in a nested ``dict`` in ``font.persistent.VF``. If
    given key does not exist, it does nothing. Resulting empty ``dict``
    will also deleted recursively.

    :param font: Fontforge font object
    :param key: Name of key. Use dots for nested ``dict`` like
    ``axes.wght``. Numeric keys are recognized and stored as numeric
    (``int`` or ``float``). If key name itself contains a dot, escape
    it to ``\\ufdd0``.
    :return: ``True`` if the key was deleted, ``False`` otherwise.
    """
    if vfInfoExists(font):
        info = font.persistent["VF"]
        for k in key.split('.')[:-1]:
            k = intOrFloat(k.replace('\ufdd0', '.'))
            if k not in info:
                return False
            elif not isinstance(info[k], dict):
                return False
            info = info[k]
        if key.split('.')[-1] in info:
            del info[key.split('.')[-1]]
            deleteEmptyDicts(font.persistent["VF"])
            return True
        else:
            deleteEmptyDicts(font.persistent["VF"])
            return False
    else:
        return False


def setOrDeleteVFValue(font: fontforge.font, key: str, val):
    """Sets or deletes a value in VF info

    If ``val`` is ``None``, calls ``deleteVFValue``. Otherwise, calls
    ``setVFValue``.

    :param font: Fontforge font object
    :param key: Name of key. Use dots for nested ``dict`` like
    ``axes.wght``. Numeric keys are recognized and stored as numeric
    (``int`` or ``float``). If key name itself contains a dot, escape
    it to ``\\ufdd0``.
    :param val: A value to set. this can be anything picklable.
    :raises ``RuntimeError``: user refused ``initPersistentDict``.
    """
    if val is None:
        deleteVFValue(font, key)
    else:
        setVFValue(font, key, val)
