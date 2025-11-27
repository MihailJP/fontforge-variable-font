import fontforge

def hello(u, glyph):
    fontforge.postNotice("FontForge Plugin Template", "Hello, world!")


def helloEnable(u, glyph):
    return True


def fontforge_plugin_init(**kw):
    fontforge.registerMenuItem(
        callback=hello,
        enable=helloEnable,
        context=("Font", "Glyph"),
        name="Hello"
    )
