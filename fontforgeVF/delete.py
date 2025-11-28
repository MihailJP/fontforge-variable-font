from fontforgeVF import utils
import fontforge

def deleteVFInfo(font: fontforge.font) -> bool:
    """Deletes VF info

    Deletes `VF` key from `font.persistent` if it is a `dict`. Otherwise
    does nothing. If such case that the `dict` will be empty,
    `font.persistent` will be set to `None`.

    Returns `True` if the key was deleted, `False` otherwise.
    """
    if utils.vfInfoExists(font):
        del font.persistent['VF']
        if len(font.persistent) == 0:
            font.persistent = None
        return True
    else:
        return False


def deleteVFInfoMenu(u, glyph):
    """Menu emtry to delete VF info from UI

    This menu is enabled if active font has VF info.
    """
    deleteVFInfo(fontforge.activeFont())


def deleteVFInfoEnable(u, glyph):
    return utils.vfInfoExists(fontforge.activeFont())
