from fontforgeVF import delete, design_axes, export
import fontforge

def loadMenu(u, glyph):
    fontforge.postNotice("This is a mockup", "Not yet implemented!")


def loadEnable(u, glyph):
    return False


def instanceMenu(u, glyph):
    fontforge.postNotice("This is a mockup", "Not yet implemented!")


def instanceEnable(u, glyph):
    return False


def fontforge_plugin_init(**kw):
    fontforge.registerMenuItem(
        callback=loadMenu,
        enable=loadEnable,
        context="Font",
        submenu="_Variable Font",
        name="_Open a variable font..."
    )
    fontforge.registerMenuItem(
        callback=export.saveMenu,
        enable=export.saveEnable,
        context="Font",
        submenu="_Variable Font",
        name="_Generate a variable font..."
    )
    fontforge.registerMenuItem(
        callback=design_axes.designAxesMenu,
        enable=design_axes.designAxesEnable,
        context="Font",
        submenu="_Variable Font",
        name="Design _axes..."
    )
    fontforge.registerMenuItem(
        callback=instanceMenu,
        enable=instanceEnable,
        context="Font",
        submenu="_Variable Font",
        name="_Instance list..."
    )
    fontforge.registerMenuItem(
        callback=delete.deleteVFInfoMenu,
        enable=delete.deleteVFInfoEnable,
        context="Font",
        submenu="_Variable Font",
        name="_Delete VF info"
    )
