import pytest


@pytest.mark.parametrize(('winLang', 'langCode', 'langName', 'exist'), [
    (0x409, 'en-US', 'English (US)', True),
    (0x411, 'ja-JP', 'Japanese', True),
    (0x40a, 'es-ES_tradnl', 'Spanish (Traditional)', True),
    (0xc0a, 'es-ES', 'Spanish (Modern)', True),
    (0x40a, 'es-ES_tradnl', 'Spanish (Spain)', False),
    (0x40a, 'es-ES', 'Spanish (Spain)', False),
    (0xc0a, 'es-ES', 'Spanish (Spain)', False),
])
def test_languageCodeIterator(winLang, langCode, langName, exist):
    from fontforgeVF.language import languageCodeIterator
    assert ((winLang, langCode, langName) in languageCodeIterator()) == exist
