import fontforge

from . import utils


def deleteVFInfo(font: fontforge.font) -> bool:
    """Deletes VF info

    Deletes ``VF`` key from ``font.persistent`` if it is a ``dict``.
    Otherwise does nothing. If such case that the ``dict`` will be
    empty, ``font.persistent`` will be set to ``None``.

    :return: ``True`` if the key was deleted, ``False`` otherwise.
    """
    if utils.vfInfoExists(font):
        assert isinstance(font.persistent, dict)
        del font.persistent['VF']
        if len(font.persistent) == 0:
            font.persistent = None
        return True
    else:
        return False


def deleteVFInfoMenu(u, font: fontforge.font):
    """Menu emtry to delete VF info from UI

    This menu is enabled if active font has VF info.
    """
    deleteVFInfo(font)


def deleteVFInfoEnable(u, font: fontforge.font):
    return utils.vfInfoExists(font)
