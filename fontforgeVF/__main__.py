import fontforge

from fontforge_plugin_helper import addSystemHook

from . import (
    delete,
    design_axes,
    export,
    instance,
    load,
)
from .translation import tr, setTranslation


def fontforge_plugin_init(**kw):
    setTranslation()
    fontforge.registerMenuItem(
        callback=load.loadMenu,
        enable=None,
        context="Font",
        submenu=[tr.get('_Variable Font'), tr.get('_Open a variable font')],
        name=tr.get('By named _instance...'),
        data=0
    )
    fontforge.registerMenuItem(
        callback=load.loadMenu,
        enable=None,
        context="Font",
        submenu=[tr.get('_Variable Font'), tr.get('_Open a variable font')],
        name=tr.get('By _parameter...'),
        data=1
    )
    fontforge.registerMenuItem(
        callback=export.saveMenu,
        enable=export.saveEnable,
        context="Font",
        submenu=tr.get('_Variable Font'),
        name=tr.get('_Generate a variable font...')
    )

    fontforge.registerMenuItem(
        divider=True,
        context="Font",
        submenu=tr.get('_Variable Font'),
    )

    fontforge.registerMenuItem(
        callback=design_axes.designAxesMenu,
        enable=None,
        context="Font",
        submenu=tr.get('_Variable Font'),
        name=tr.get('Design _axes...')
    )
    fontforge.registerMenuItem(
        callback=instance.instanceMenu,
        enable=None,
        context="Font",
        submenu=tr.get('_Variable Font'),
        name=tr.get('Named _instances...')
    )
    fontforge.registerMenuItem(
        callback=delete.deleteVFInfoMenu,
        enable=delete.deleteVFInfoEnable,
        context="Font",
        submenu=tr.get('_Variable Font'),
        name=tr.get('_Delete VF info')
    )

    if fontforge.hasUserInterface:
        addSystemHook('loadFontHook', load.loadHook)
        addSystemHook('newFontHook', load.newFontHook)
