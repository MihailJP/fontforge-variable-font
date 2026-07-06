from fontforge_plugin_helper import Translations

from .fr import translation_fr
from .ja import translation_ja
from .zh_CN import translation_zh_CN
from .zh_TW import translation_zh_TW

tr = Translations()


def setTranslation():
    tr.setTranslations('fr', translation_fr)
    tr.setTranslations('ja', translation_ja)
    tr.setTranslations('zh_CN', translation_zh_CN)
    tr.setTranslations('zh', translation_zh_TW)
