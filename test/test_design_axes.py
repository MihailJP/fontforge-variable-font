import pytest
import fontforge


def axisTestFont(useDefault):
    from fontforgeVF.utils import setVFValue
    font = fontforge.font()
    setVFValue(font, 'axes.ital.active', True)
    setVFValue(font, 'axes.ital.useDefault', useDefault)
    setVFValue(font, 'axes.ital.value', True)
    font.design_size = 12
    setVFValue(font, 'axes.opsz.active', True)
    setVFValue(font, 'axes.opsz.useDefault', useDefault)
    setVFValue(font, 'axes.opsz.value', 48)
    font.italicangle = 0
    setVFValue(font, 'axes.slnt.active', True)
    setVFValue(font, 'axes.slnt.useDefault', useDefault)
    setVFValue(font, 'axes.slnt.value', -15)
    font.os2_width = 5  # medium
    setVFValue(font, 'axes.wdth.active', True)
    setVFValue(font, 'axes.wdth.useDefault', useDefault)
    setVFValue(font, 'axes.wdth.value', 150)
    font.os2_weight = 400
    setVFValue(font, 'axes.wght.active', True)
    setVFValue(font, 'axes.wght.useDefault', useDefault)
    setVFValue(font, 'axes.wght.value', 700)
    setVFValue(font, 'axes.custom1.active', True)
    setVFValue(font, 'axes.custom1.tag', 'spam')
    setVFValue(font, 'axes.custom1.value', 10)
    setVFValue(font, 'axes.custom2.active', True)
    setVFValue(font, 'axes.custom2.tag', 'ham ')
    setVFValue(font, 'axes.custom2.value', 20)
    return font


@pytest.mark.parametrize(('tag', 'expected'), [
    ('ital', 'ital'),
    ('opsz', 'opsz'),
    ('slnt', 'slnt'),
    ('wdth', 'wdth'),
    ('wght', 'wght'),
    ('spam', 'custom1'),
    ('ham', 'custom2'),
    ('ham ', 'custom2'),
    ('eggs', None),
])
def test_searchCustomAxis(tag, expected):
    from fontforgeVF.design_axes import _searchCustomAxis
    try:
        font = axisTestFont(True)
        assert _searchCustomAxis(font, tag) == expected
    finally:
        font.close()


@pytest.mark.parametrize(('tag', 'useDefault', 'expected'), [
    ('ital', False, True),
    ('ital', True, False),
    ('opsz', False, 48),
    ('opsz', True, 12),
    ('slnt', False, -15),
    ('slnt', True, 0),
    ('wdth', False, 150),
    ('wdth', True, 100),
    ('wght', False, 700),
    ('wght', True, 400),
    ('spam', False, 10),
    ('ham', False, 20),
    ('ham ', False, 20),
    ('eggs', False, None),
])
def test_getAxisValue(tag, useDefault, expected):
    from fontforgeVF.design_axes import getAxisValue
    try:
        font = axisTestFont(useDefault)
        assert getAxisValue(font, tag) == expected
    finally:
        font.close()
