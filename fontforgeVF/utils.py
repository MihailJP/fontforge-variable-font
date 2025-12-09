import fontforge
import re


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
    if isinstance(val, str) and val.startswith('0x'):
        return int(val, 16)
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


def _checkVFAddrFragment(key: str) -> tuple:
    listitem = re.search(r'(\[\d+\])+$', key)
    k = re.sub(r'(\[\d+\])+$', '', key)
    k = intOrFloat(re.sub(r'^([-+]?\d*),(\d+([Ee][-+]?\d+)?)$', r'\1.\2', k))
    if listitem:
        listitem = list(map(int, listitem[0][1:-1].split('][')))
    else:
        listitem = []
    return (k, listitem)


def _checkVFAddr(key: str) -> list[tuple]:
    parts = []
    for k in key.split('.'):
        k, listitem = _checkVFAddrFragment(k)
        parts.append((dict, k))
        for i in listitem:
            parts.append((list, i))
    return parts


def getVFValue(font: fontforge.font, key: str, default=None):
    """Gets a value from VF info

    Gets a value from nested ``dict`` in ``font.persistent.VF``. If
    given key does not exist, uses default value.

    :param font: Fontforge font object
    :param key: Name of key. Use dots for nested ``dict`` like
    ``axes.wght``. Numeric keys are recognized and stored as numeric
    (``int`` or ``float``). If key is a ``float`` value, a comma
    (continental decimal separator) should be used since a dot
    (Anglo-American decimal separator) conflicts with hierarchical
    separator.
    :param default: Optional. Returns this value if ``key`` does not
    exist. Without this parameter defaults to ``None``.
    :return: the value for ``key``, or ``default`` if no such ``key``.
    """
    if not vfInfoExists(font):
        return default
    else:
        info = font.persistent["VF"]
        for part in _checkVFAddr(key):
            c, k = part
            if not isinstance(info, c):
                return default
            elif (c is dict) and (k not in info):
                return default
            elif (c is list) and k >= len(info):
                return default
            else:
                info = info[k]
        return info


def _makeSureKeyExists(container, key):
    if isinstance(container, list):
        while len(container) <= key:
            container.append(None)
    elif isinstance(container, dict):
        if key not in container:
            container[key] = None
    else:
        raise TypeError("unsupported type")


def setVFValue(font: fontforge.font, key: str, val):
    """Sets a value in VF info

    Sets a value in a nested ``dict`` in ``font.persistent.VF``. If
    given key does not exist, it is recursively created.

    :param font: Fontforge font object
    :param key: Name of key. Use dots for nested ``dict`` like
    ``axes.wght``. Numeric keys are recognized and stored as numeric
    (``int`` or ``float``). If key is a ``float`` value, a comma
    (continental decimal separator) should be used since a dot
    (Anglo-American decimal separator) conflicts with hierarchical
    separator.
    :param val: A value to set. this can be anything picklable.
    :raises ``RuntimeError``: user refused ``initPersistentDict``.
    """
    initPersistentDict(font)
    parent = font.persistent
    info = parent["VF"]
    prevk = "VF"
    for part in _checkVFAddr(key):
        c, k = part
        if not isinstance(info, c):
            parent[prevk] = c()
            _makeSureKeyExists(parent[prevk], k)
            info = parent[prevk]
        elif (c is dict) and (k not in info):
            _makeSureKeyExists(parent[prevk], k)
            info = parent[prevk]
        elif (c is list) and k >= len(info):
            _makeSureKeyExists(parent[prevk], k)
            info = parent[prevk]
        parent = info
        info = info[k]
        prevk = k
    parent[k] = val


def _deleteEmptyLists(d: dict):
    if isinstance(d, list):
        for i in range(len(d)):
            if isinstance(d[i], dict):
                deleteEmptyDicts(d[i])
                if len(d[i]) == 0:
                    d[i] = None
            elif isinstance(d[i], list):
                _deleteEmptyLists(d[i])
                if len(d[i]) == 0:
                    d[i] = None
        for i in range(len(d) - 1, -1, -1):
            if d[i] is None:
                d.pop()
            else:
                break


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
            elif isinstance(d[k], list):
                _deleteEmptyLists(d[k])
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
    (``int`` or ``float``). If key is a ``float`` value, a comma
    (continental decimal separator) should be used since a dot
    (Anglo-American decimal separator) conflicts with hierarchical
    separator.
    :return: ``True`` if the key was deleted, ``False`` otherwise.
    """
    if vfInfoExists(font):
        parent = font.persistent
        info = parent["VF"]
        for part in _checkVFAddr(key):
            c, k = part
            if not isinstance(info, c):
                deleteEmptyDicts(font.persistent["VF"])
                return False
            elif (c is dict) and (k not in info):
                deleteEmptyDicts(font.persistent["VF"])
                return False
            elif (c is list) and k >= len(info):
                deleteEmptyDicts(font.persistent["VF"])
                return False
            parent = info
            info = info[k]

        if (c is dict) and (k in parent):
            del parent[k]
            deleteEmptyDicts(font.persistent["VF"])
            return True
        elif (c is list) and (k < len(parent)) and (parent[k] is not None):
            parent[k] = None
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
    (``int`` or ``float``). If key is a ``float`` value, a comma
    (continental decimal separator) should be used since a dot
    (Anglo-American decimal separator) conflicts with hierarchical
    separator.
    :param val: A value to set. this can be anything picklable.
    :raises ``RuntimeError``: user refused ``initPersistentDict``.
    """
    if val is None:
        deleteVFValue(font, key)
    else:
        setVFValue(font, key, val)
