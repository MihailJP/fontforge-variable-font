import pytest
import fontforge
from fontforgeVF.utils import setVFValue


def test_getSourceFonts():
    from fontforgeVF.export import _getSourceFonts
    try:
        font1 = fontforge.font()
        font1.familyname = "TestFamily"
        font2 = fontforge.font()
        font2.familyname = "TestFamily"
        font3 = fontforge.font()
        font3.familyname = "AnotherFamily"
        result = _getSourceFonts(font1)
        assert font1 in result
        assert font2 in result
        assert font3 not in result
    finally:
        font1.close()
        font2.close()
        font3.close()


def _axisMinMaxTestFonts():
    font1 = fontforge.font()
    font1.familyname = "TestFamily"
    font1.os2_weight = 400
    setVFValue(font1, 'axes.wght.active', True)
    setVFValue(font1, 'axes.wght.useDefault', True)
    font2 = fontforge.font()
    font2.familyname = "TestFamily"
    setVFValue(font2, 'axes.wght.active', True)
    setVFValue(font2, 'axes.wght.useDefault', False)
    setVFValue(font2, 'axes.wght.value', 700)
    return font1, font2


def test_axisMinValue():
    from fontforgeVF.export import _axisMinValue
    try:
        font1, font2 = _axisMinMaxTestFonts()
        assert _axisMinValue(font1, 'wght') == 400
    finally:
        font1.close()
        font2.close()


def test_axisMaxValue():
    from fontforgeVF.export import _axisMaxValue
    try:
        font1, font2 = _axisMinMaxTestFonts()
        assert _axisMaxValue(font1, 'wght') == 700
    finally:
        font1.close()
        font2.close()


@pytest.mark.parametrize(('pattern', 'lang', 'expected'), [
    (0, 'English (US)', 'PostScript Family'),
    (1, 'English (US)', 'Family'),
    (2, 'English (US)', 'WWS Family'),
    (3, 'English (US)', 'WWS Family'),
    (4, 'English (US)', 'Preferred Family'),
    (5, 'English (US)', 'Preferred Family'),
    (6, 'English (US)', 'Preferred Family'),
    (7, 'English (US)', 'Preferred Family'),
    (0, 'Japanese', None),
    (1, 'Japanese', 'ファミリ名'),
    (2, 'Japanese', 'WWSファミリ名'),
    (3, 'Japanese', 'WWSファミリ名'),
    (4, 'Japanese', '優先ファミリ名'),
    (5, 'Japanese', '優先ファミリ名'),
    (6, 'Japanese', '優先ファミリ名'),
    (7, 'Japanese', '優先ファミリ名'),
])
def test_getFontFamilyName(pattern, lang, expected):
    from fontforgeVF.export import _getFontFamilyName
    try:
        font = fontforge.font()
        font.familyname = "PostScript Family"
        sfnt_names = []
        if pattern & 1:
            sfnt_names += (
                ('English (US)', 'Family', 'Family'),
                ('Japanese', 'Family', 'ファミリ名'),
            )
        if pattern & 2:
            sfnt_names += (
                ('English (US)', 'WWS Family', 'WWS Family'),
                ('Japanese', 'WWS Family', 'WWSファミリ名'),
            )
        if pattern & 4:
            sfnt_names += (
                ('English (US)', 'Preferred Family', 'Preferred Family'),
                ('Japanese', 'Preferred Family', '優先ファミリ名'),
            )
        font.sfnt_names = tuple(sfnt_names)
        assert _getFontFamilyName(font, lang) == expected
    finally:
        font.close()


@pytest.mark.parametrize(('pattern', 'lang', 'expected'), [
    (0, 'English (US)', 'PostScript Weight'),
    (1, 'English (US)', 'SubFamily'),
    (2, 'English (US)', 'WWS Subfamily'),
    (3, 'English (US)', 'WWS Subfamily'),
    (4, 'English (US)', 'Preferred Styles'),
    (5, 'English (US)', 'Preferred Styles'),
    (6, 'English (US)', 'Preferred Styles'),
    (7, 'English (US)', 'Preferred Styles'),
    (0, 'Japanese', None),
    (1, 'Japanese', 'サブファミリ名'),
    (2, 'Japanese', 'WWSサブファミリ名'),
    (3, 'Japanese', 'WWSサブファミリ名'),
    (4, 'Japanese', '優先スタイル名'),
    (5, 'Japanese', '優先スタイル名'),
    (6, 'Japanese', '優先スタイル名'),
    (7, 'Japanese', '優先スタイル名'),
])
def test_getFontSubFamilyName(pattern, lang, expected):
    from fontforgeVF.export import _getFontSubFamilyName
    try:
        font = fontforge.font()
        font.weight = "PostScript Weight"
        sfnt_names = []
        if pattern & 1:
            sfnt_names += (
                ('English (US)', 'SubFamily', 'SubFamily'),
                ('Japanese', 'SubFamily', 'サブファミリ名'),
            )
        if pattern & 2:
            sfnt_names += (
                ('English (US)', 'WWS Subfamily', 'WWS Subfamily'),
                ('Japanese', 'WWS Subfamily', 'WWSサブファミリ名'),
            )
        if pattern & 4:
            sfnt_names += (
                ('English (US)', 'Preferred Styles', 'Preferred Styles'),
                ('Japanese', 'Preferred Styles', '優先スタイル名'),
            )
        font.sfnt_names = tuple(sfnt_names)
        assert _getFontSubFamilyName(font, lang) == expected
    finally:
        font.close()


@pytest.mark.parametrize(('width_I', 'width_W', 'expected'), [
    (400, 1000, False),
    (600, 600, True),
])
def test_isFixedPitch(width_I, width_W, expected):
    from fontforgeVF.export import _isFixedPitch
    try:
        font = fontforge.font()
        font.createMappedChar('I')
        font.createMappedChar('W')
        font['I'].width = width_I
        font['W'].width = width_W
        assert _isFixedPitch(font) == expected
    finally:
        font.close()
