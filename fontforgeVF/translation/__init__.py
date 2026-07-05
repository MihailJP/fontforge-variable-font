from fontforge_plugin_helper import Translations

from .fr import translation_fr
from .ja import translation_ja

tr = Translations()


def setTranslation():
    tr.setTranslations('fr', translation_fr)
    tr.setTranslations('ja', translation_ja)
