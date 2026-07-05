from fontforge_plugin_helper import Translations

from .ja import translation_ja

tr = Translations()


def setTranslation():
    tr.setTranslations('ja', translation_ja)
