import pytest
import fontforge


@pytest.mark.parametrize(('param', 'expectedVal', 'expectedType'), [
    (125, 125, int),
    (12.5, 12.5, float),
    ("125", 125, int),
    ("12.5", 12.5, float),
    ("-125", -125, int),
    ("-12.5", -12.5, float),
    ("1E2", 100.0, float),
    ("spam", "spam", str),
])
def test_intOrFloat(param, expectedVal, expectedType):
    from fontforgeVF.utils import intOrFloat
    assert isinstance(intOrFloat(param), expectedType)
    assert intOrFloat(param) == expectedVal


@pytest.mark.parametrize(('persistent'), [
    (None,),
    ("spam",),
    ({},),
])
def test_initPersistentDict(persistent):
    from fontforgeVF.utils import initPersistentDict
    font = fontforge.font()
    font.persistent = persistent
    initPersistentDict(font)
    assert isinstance(font.persistent, dict)
    assert 'VF' in font.persistent
    assert isinstance(font.persistent['VF'], dict)
    font.close()


@pytest.mark.parametrize(('persistent', 'expected'), [
    (None, False),
    ("spam", False),
    ({}, False),
    ({'VF': {}}, True),
])
def test_vfInfoExists(persistent, expected):
    from fontforgeVF.utils import vfInfoExists
    font = fontforge.font()
    font.persistent = persistent
    assert vfInfoExists(font) == expected
    font.close()


@pytest.mark.parametrize(('persistent', 'key', 'default', 'expected'), [
    (None, 'spam.ham', None, None),
    (None, 'spam.ham', 150, 150),
    ({'VF': {}}, 'spam.ham', None, None),
    ({'VF': {'spam': {}}}, 'spam.ham', None, None),
    ({'VF': {'spam': 300}}, 'spam.ham', None, None),
    ({'VF': {'spam': {'ham': 300}}}, 'spam.ham', None, 300),
    ({'VF': {'spam': {10: 300}}}, 'spam.10', None, 300),
    ({'VF': {'spam': {2.5: 300}}}, 'spam.2\ufdd05', None, 300),
])
def test_getVFValue(persistent, key, default, expected):
    from fontforgeVF.utils import getVFValue
    font = fontforge.font()
    font.persistent = persistent
    assert getVFValue(font, key, default) == expected
    font.close()


@pytest.mark.parametrize(('persistent', 'key', 'val', 'expectedPersistent'), [
    (None, 'spam.ham', 300, {'VF': {'spam': {'ham': 300}}}),
    ({'VF': {}}, 'spam.ham', 300, {'VF': {'spam': {'ham': 300}}}),
    ({'VF': {'spam': {}}}, 'spam.ham', 300, {'VF': {'spam': {'ham': 300}}}),
    ({'VF': {'spam': 300}}, 'spam.ham', 300, {'VF': {'spam': {'ham': 300}}}),
    ({'VF': {'spam': {'ham': 300}}}, 'spam.ham', 300, {'VF': {'spam': {'ham': 300}}}),
    ({'VF': {'spam': {'eggs': 600}}}, 'spam.ham', 300, {'VF': {'spam': {'eggs': 600, 'ham': 300}}}),
])
def test_setVFValue(persistent, key, val, expectedPersistent):
    from fontforgeVF.utils import setVFValue
    font = fontforge.font()
    font.persistent = persistent
    setVFValue(font, key, val)
    assert font.persistent == expectedPersistent
    font.close()


@pytest.mark.parametrize(('param', 'expected'), [
    (None, None),
    ('spam', 'spam'),
    ({'ham': {}}, {}),
    ({'ham': {'spam': {}}}, {}),
    ({'ham': {'spam': 300}}, {'ham': {'spam': 300}}),
    ({'ham': {'spam': {'ham': 300}}}, {'ham': {'spam': {'ham': 300}}}),
    ({'ham': {'spam': {'ham': 300}, 'eggs': {}}}, {'ham': {'spam': {'ham': 300}}}),
    ({'ham': {'spam': {'ham': {}}, 'eggs': {}}}, {}),
])
def test_deleteEmptyDicts(param, expected):
    from fontforgeVF.utils import deleteEmptyDicts
    deleteEmptyDicts(param)
    assert param == expected


@pytest.mark.parametrize(('persistent', 'key', 'expected', 'expectedPersistent'), [
    (None, 'spam.ham', False, None),
    ('spam', 'spam.ham', False, 'spam'),
    ({'VF': {}}, 'spam.ham', False, {'VF': {}}),
    ({'VF': {'spam': {}}}, 'spam.ham', False, {'VF': {}}),
    ({'VF': {'spam': 300}}, 'spam.ham', False, {'VF': {'spam': 300}}),
    ({'VF': {'spam': {'ham': 300}}}, 'spam.ham', True, {'VF': {}}),
    ({'VF': {'spam': {'ham': 300}, 'eggs': 600}}, 'spam.ham', True, {'VF': {'eggs': 600}}),
    ({'VF': {'spam': {'ham': 300, 'eggs': 600}}}, 'spam.ham', True, {'VF': {'spam': {'eggs': 600}}}),
    ({'VF': {'spam': {'ham': {}}, 'eggs': {}}}, 'spam.ham', True, {'VF': {}}),
])
def test_deleteVFValue(persistent, key, expected, expectedPersistent):
    from fontforgeVF.utils import deleteVFValue
    font = fontforge.font()
    font.persistent = persistent
    assert deleteVFValue(font, key) == expected
    assert font.persistent == expectedPersistent
    font.close()


@pytest.mark.parametrize(('persistent', 'key', 'val', 'expectedPersistent'), [
    (None, 'spam.ham', 300, {'VF': {'spam': {'ham': 300}}}),
    ({'VF': {}}, 'spam.ham', 300, {'VF': {'spam': {'ham': 300}}}),
    ({'VF': {'spam': {}}}, 'spam.ham', 300, {'VF': {'spam': {'ham': 300}}}),
    ({'VF': {'spam': 300}}, 'spam.ham', 300, {'VF': {'spam': {'ham': 300}}}),
    ({'VF': {'spam': {'ham': 300}}}, 'spam.ham', 300, {'VF': {'spam': {'ham': 300}}}),
    ({'VF': {'spam': {'eggs': 600}}}, 'spam.ham', 300, {'VF': {'spam': {'eggs': 600, 'ham': 300}}}),
    (None, 'spam.ham', None, None),
    ('spam', 'spam.ham', None, 'spam'),
    ({'VF': {}}, 'spam.ham', None, {'VF': {}}),
    ({'VF': {'spam': {}}}, 'spam.ham', None, {'VF': {}}),
    ({'VF': {'spam': 300}}, 'spam.ham', None, {'VF': {'spam': 300}}),
    ({'VF': {'spam': {'ham': 300}}}, 'spam.ham', None, {'VF': {}}),
    ({'VF': {'spam': {'ham': 300}, 'eggs': 600}}, 'spam.ham', None, {'VF': {'eggs': 600}}),
    ({'VF': {'spam': {'ham': 300, 'eggs': 600}}}, 'spam.ham', None, {'VF': {'spam': {'eggs': 600}}}),
    ({'VF': {'spam': {'ham': {}}, 'eggs': {}}}, 'spam.ham', None, {'VF': {}}),
])
def test_setOrDeleteVFValue(persistent, key, val, expectedPersistent):
    from fontforgeVF.utils import setOrDeleteVFValue
    font = fontforge.font()
    font.persistent = persistent
    setOrDeleteVFValue(font, key, val)
    assert font.persistent == expectedPersistent
    font.close()
