"""FontForge plugin to create a variable font"""

from .delete import deleteVFInfo
from .design_axes import getAxisValue
from .export import exportVariableFont
from .language import languageCodeIterator, languageCodeLookup, languageCodeReverseLookup, getLanguageList
from .load import openVariableFont
from .utils import (
    intOrFloat,
    initPersistentDict,
    vfInfoExists,
    getVFValue,
    setVFValue,
    deleteEmptyDicts,
    deleteVFValue,
    setOrDeleteVFValue,
    checkExtensionTtfOrWoff2,
)


__all__ = [
    # delete
    "deleteVFInfo",

    # design_axes
    "getAxisValue",

    # export
    "exportVariableFont",

    # language
    'languageCodeIterator',
    'languageCodeLookup',
    'languageCodeReverseLookup',
    'getLanguageList',

    # load
    "openVariableFont",

    # utils
    "intOrFloat",
    "initPersistentDict",
    "vfInfoExists",
    "getVFValue",
    "setVFValue",
    "deleteEmptyDicts",
    "deleteVFValue",
    "setOrDeleteVFValue",
    "checkExtensionTtfOrWoff2",
]
