import pytest


@pytest.mark.parametrize(('winLang', 'langCode', 'langName', 'useTableInFontTools', 'exist'), [
    (0x409, 'en-US', 'English (US)', False, True),
    (0x411, 'ja-JP', 'Japanese', False, True),
    (0x40a, 'es-ES_tradnl', 'Spanish (Traditional)', False, True),
    (0xc0a, 'es-ES', 'Spanish (Modern)', False, True),
    (0x40a, 'es-ES_tradnl', 'Spanish (Spain)', False, False),
    (0x40a, 'es-ES', 'Spanish (Spain)', False, False),
    (0xc0a, 'es-ES', 'Spanish (Spain)', False, False),
    (0x409, 'en', 'English (US)', True, True),
    (0x411, 'ja', 'Japanese', True, True),
    (0x40a, 'es', 'Spanish (Traditional)', True, False),
    (0xc0a, 'es', 'Spanish (Modern)', True, False),
    (0x40a, 'es', 'Spanish (Spain)', True, False),
    (0x40a, 'es', 'Spanish (Spain)', True, False),
    (0xc0a, 'es', 'Spanish (Spain)', True, True),
])
def test_languageCodeIterator(winLang, langCode, langName, useTableInFontTools, exist):
    from fontforgeVF.language import languageCodeIterator
    assert ((winLang, langCode, langName) in languageCodeIterator(useTableInFontTools)) == exist
