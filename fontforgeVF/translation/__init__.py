from fontforge_plugin_helper import Translations

from .de import translation_de
from .es import translation_es
from .fr import translation_fr
from .ja import translation_ja
from .zh_CN import translation_zh_CN
from .zh_TW import translation_zh_TW

tr = Translations()


def setTranslation():
    tr.setTranslations('de', translation_de)
    tr.setTranslations('es', translation_es)
    tr.setTranslations('fr', translation_fr)
    tr.setTranslations('ja', translation_ja)
    tr.setTranslations('zh_CN', translation_zh_CN)
    tr.setTranslations('zh', translation_zh_TW)
