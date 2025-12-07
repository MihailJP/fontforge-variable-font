from fontforgeVF import (
    delete,
    design_axes,
    export,
    load
)
import fontforge


def fontforge_plugin_init(**kw):
    fontforge.registerMenuItem(
        callback=load.loadMenu,
        enable=load.loadEnable,
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
        callback=delete.deleteVFInfoMenu,
        enable=delete.deleteVFInfoEnable,
        context="Font",
        submenu="_Variable Font",
        name="_Delete VF info"
    )
