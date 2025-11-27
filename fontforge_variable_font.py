import fontforge

def mockup(u, glyph):
    fontforge.postNotice("This is a mockup", "Not yet implemented!")


def mockupEnable(u, glyph):
    return True


def fontforge_plugin_init(**kw):
    fontforge.registerMenuItem(
        callback=mockup,
        enable=mockupEnable,
        context="Font",
        name="_Variable Font"
    )
