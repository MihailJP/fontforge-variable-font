from fontforgeVF import (
    delete,
    design_axes,
    export,
    instance,
    load
)
import fontforge


def fontforge_plugin_init(**kw):
    fontforge.registerMenuItem(
        callback=load.loadMenu,
        enable=None,
        context="Font",
        submenu=["_Variable Font", '_Open a variable font'],
        name="By named _instance...",
        data=0
    )
    fontforge.registerMenuItem(
        callback=load.loadMenu,
        enable=None,
        context="Font",
        submenu=["_Variable Font", '_Open a variable font'],
        name="By _parameter...",
        data=1
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
        enable=None,
        context="Font",
        submenu="_Variable Font",
        name="Design _axes..."
    )
    fontforge.registerMenuItem(
        callback=instance.instanceMenu,
        enable=None,
        context="Font",
        submenu="_Variable Font",
        name="Named _instances..."
    )
    fontforge.registerMenuItem(
        callback=delete.deleteVFInfoMenu,
        enable=delete.deleteVFInfoEnable,
        context="Font",
        submenu="_Variable Font",
        name="_Delete VF info"
    )
