from fontTools.ttLib.tables._n_a_m_e import _WINDOWS_LANGUAGES


__all__ = [
    'languageCodeIterator',
    'languageCodeReverseLookup',
]

languageData = {
    1: {
        'name': 'Arabic',
        'code': 'ar',
        1: {'name': ('. (Saudi Arabia)',), 'code': 'ar-SA'},
        2: {'name': ('. (Iraq)',), 'code': 'ar-IQ'},
        3: {'name': ('. (Egypt)',), 'code': 'ar-EG'},
        4: {'name': ('. (Libya)',), 'code': 'ar-LY'},
        5: {'name': ('. (Algeria)',), 'code': 'ar-DZ'},
        6: {'name': ('. (Morocco)',), 'code': 'ar-MA'},
        7: {'name': ('. (Tunisia)',), 'code': 'ar-TN'},
        8: {'name': ('. (Oman)',), 'code': 'ar-OM'},
        9: {'name': ('. (Yemen)',), 'code': 'ar-YE'},
        10: {'name': ('. (Syria)',), 'code': 'ar-SY'},
        11: {'name': ('. (Jordan)',), 'code': 'ar-JO'},
        12: {'name': ('. (Lebanon)',), 'code': 'ar-LB'},
        13: {'name': ('. (Kuwait)',), 'code': 'ar-KW'},
        14: {'name': ('. (U.A.E.)',), 'code': 'ar-AE'},
        15: {'name': ('. (Bahrain)',), 'code': 'ar-BH'},
        16: {'name': ('. (Qatar)',), 'code': 'ar-QA'},
    },
    2: {
        'name': 'Bulgarian',
        'code': 'bg',
        1: {'name': ('.',), 'code': 'bg-BG'},
    },
    3: {
        'name': 'Catalan',
        'code': 'ca',
        1: {'name': ('.',), 'code': 'ca-ES'},
    },
    4: {
        'name': 'Chinese',
        'code': 'zh',
        1: {'name': ('. (Taiwan)',), 'code': 'zh-TW'},
        2: {'name': ('. (PRC)',), 'code': 'zh-CN'},
        3: {'name': ('. (Hong Kong)',), 'code': 'zh-HK'},
        4: {'name': ('. (Singapore)',), 'code': 'zh-SG'},
        5: {'name': ('. (Macau)',), 'code': 'zh-MO'},
    },
    5: {
        'name': 'Czech',
        'code': 'cs',
        1: {'name': ('.',), 'code': 'cs-CZ'},
    },
    6: {
        'name': 'Danish',
        'code': 'da',
        1: {'name': ('.',), 'code': 'da-DK'},
    },
    7: {
        'name': 'German',
        'code': 'de',
        1: {'name': ('. German',), 'code': 'de-DE'},
        2: {'name': ('. Swiss',), 'code': 'de-CH'},
        3: {'name': ('. Austrian',), 'code': 'de-AT'},
        4: {'name': ('. Luxembourg',), 'code': 'de-LU'},
        5: {'name': ('. Liechtenstein',), 'code': 'de-LI'},
    },
    8: {
        'name': 'Greek',
        'code': 'el',
        1: {'name': ('.',), 'code': 'el-GR'},
    },
    9: {
        'name': 'English',
        'code': 'en',
        1: {'name': ('. (US)',), 'code': 'en-US'},
        2: {'name': ('. (British)',), 'code': 'en-GB'},
        3: {'name': ('. (Australian)',), 'code': 'en-AU'},
        4: {'name': ('. (Canada)',), 'code': 'en-CA'},
        5: {'name': ('. (New Zealand)',), 'code': 'en-NZ'},
        6: {'name': ('. (Irish)',), 'code': 'en-IE'},
        7: {'name': ('. (South Africa)',), 'code': 'en-ZA'},
        8: {'name': ('. (Jamaica)',), 'code': 'en-JM'},
        9: {'name': ('. (Caribbean)',), 'code': 'en-029'},
        10: {'name': ('. (Belize)',), 'code': 'en-BZ'},
        11: {'name': ('. (Trinidad)',), 'code': 'en-TT'},
        12: {'name': ('. (Zimbabwe)',), 'code': 'en-ZW'},
        13: {'name': ('. (Philippines)',), 'code': 'en-PH'},
        14: {'name': ('. (Indonesia)',), 'code': 'en-ID'},
        15: {'name': ('. (Hong Kong)',), 'code': 'en-HK'},
        16: {'name': ('. (India)',), 'code': 'en-IN'},
        17: {'name': ('. (Malaysia)',), 'code': 'en-MY'},
        18: {'name': ('. (Singapore)',), 'code': 'en-SG'},
    },
    10: {
        'name': 'Spanish',
        'code': 'es',
        1: {'name': ('. (Traditional)',), 'code': 'es-ES_tradnl'},
        2: {'name': ('. Mexico',), 'code': 'es-MX'},
        3: {'name': ('. (Modern)',), 'code': 'es-ES'},
        4: {'name': ('. (Guatemala)',), 'code': 'es-GT'},
        5: {'name': ('. (Costa Rica)',), 'code': 'es-CR'},
        6: {'name': ('. (Panama)',), 'code': 'es-PA'},
        7: {'name': ('. (Dominican Republic)',), 'code': 'es-DO'},
        8: {'name': ('. (Venezuela)',), 'code': 'es-VE'},
        9: {'name': ('. (Colombia)',), 'code': 'es-CO'},
        10: {'name': ('. (Peru)',), 'code': 'es-PE'},
        11: {'name': ('. (Argentina)',), 'code': 'es-AR'},
        12: {'name': ('. (Ecuador)',), 'code': 'es-EC'},
        13: {'name': ('. (Chile)',), 'code': 'es-CL'},
        14: {'name': ('. (Uruguay)',), 'code': 'es-UY'},
        15: {'name': ('. (Paraguay)',), 'code': 'es-PY'},
        16: {'name': ('. (Bolivia)',), 'code': 'es-BO'},
        17: {'name': ('. (El Salvador)',), 'code': 'es-SV'},
        18: {'name': ('. (Honduras)',), 'code': 'es-HN'},
        19: {'name': ('. (Nicaragua)',), 'code': 'es-NI'},
        20: {'name': ('. (Puerto Rico)',), 'code': 'es-PR'},
        21: {'name': ('. (United States)',), 'code': 'es-US'},
        57: {'name': ('. (Latin America)',), 'code': 'es-419'},
    },
    11: {
        'name': 'Finnish',
        'code': 'fi',
        1: {'name': ('.',), 'code': 'fi-FI'},
    },
    12: {
        'name': 'French',
        'code': 'fr',
        1: {'name': ('. French',), 'code': 'fr-FR'},
        2: {'name': ('. Belgium',), 'code': 'fr-BE'},
        3: {'name': ('. Canadian',), 'code': 'fr-CA'},
        4: {'name': ('. Swiss',), 'code': 'fr-CH'},
        5: {'name': ('. Luxembourg',), 'code': 'fr-LU'},
        6: {'name': ('. Monaco',), 'code': 'fr-MC'},
        7: {'name': ('. West Indies',), 'code': 'fr-029'},
        8: {'name': ('. Réunion',), 'code': 'fr-RE'},
        9: {'name': ('. D.R. Congo',), 'code': 'fr-CD'},
        10: {'name': ('. Senegal',), 'code': 'fr-SN'},
        11: {'name': ('. Camaroon',), 'code': 'fr-CM'},
        12: {'name': ('. Côte d\'Ivoire',), 'code': 'fr-CI'},
        13: {'name': ('. Mali',), 'code': 'fr-ML'},
        14: {'name': ('. Morocco',), 'code': 'fr-MA'},
        15: {'name': ('. Haiti',), 'code': 'fr-HT'},
        57: {'name': ('. North Africa',), 'code': 'fr-015'},
    },
    13: {
        'name': 'Hebrew',
        'code': 'he',
        1: {'name': ('.',), 'code': 'he-IL'},
    },
    14: {
        'name': 'Hungarian',
        'code': 'hu',
        1: {'name': ('.',), 'code': 'hu-HU'},
    },
    15: {
        'name': 'Icelandic',
        'code': 'is',
        1: {'name': ('.',), 'code': 'is-IS'},
    },
    16: {
        'name': 'Italian',
        'code': 'it',
        1: {'name': ('.',), 'code': 'it-IT'},
        2: {'name': ('. Swiss',), 'code': 'it-CH'},
    },
    17: {
        'name': 'Japanese',
        'code': 'ja',
        1: {'name': ('.',), 'code': 'ja-JP'},
    },
    18: {
        'name': 'Korean',
        'code': 'ko',
        1: {'name': ('.',), 'code': 'ko-KR'},
        2: {'name': ('. (Johab)',), 'code': 'ko-KR'},
    },
    19: {
        'name': 'Dutch',
        'code': 'nl',
        1: {'name': ('.',), 'code': 'nl-NL'},
        2: {'name': ('Flemish (Belgian .)',), 'code': 'nl-BE'},
    },
    20: {
        'name': 'Norwegian',
        'code': 'no',
        1: {'name': ('. (Bokmal)',), 'code': 'nb-NO'},
        2: {'name': ('. (Nynorsk)',), 'code': 'nn-NO'},
    },
    21: {
        'name': 'Polish',
        'code': 'pl',
        1: {'name': ('.',), 'code': 'pl-PL'},
    },
    22: {
        'name': 'Portuguese',
        'code': 'pt',
        1: {'name': ('. (Brasil)',), 'code': 'pt-BR'},
        2: {'name': ('. (Portugal)',), 'code': 'pt-PT'},
    },
    23: {
        'name': 'Rhaeto-Romanic',
        'code': 'rm',
        1: {'name': ('.',), 'code': 'rm-CH'},
    },
    24: {
        'name': 'Romanian',
        'code': 'ro',
        1: {'name': ('.',), 'code': 'ro-RO'},
        2: {'name': ('. (Moldova)',), 'code': 'ro-MD'},
    },
    25: {
        'name': 'Russian',
        'code': 'ru',
        1: {'name': ('.',), 'code': 'ru-RU'},
        2: {'name': ('. (Moldova)',), 'code': 'ru-MD'},
    },
    26: {
        'name': 'Serbo-Croatian',
        'code': 'sh',
        1: {'name': ('Croatian',), 'code': 'hr-HR'},
        2: {'name': ('Serbian (Latin)',), 'code': 'sr-Latn-RS'},
        3: {'name': ('Serbian (Cyrillic)',), 'code': 'sr-Cyrl-RS'},
        4: {'name': ('Croatian Bosnia/Herzegovina',), 'code': 'hr-BA'},
        5: {'name': ('Bosnian (Latin)',), 'code': 'bs-Latn-BA'},
        6: {'name': ('Serbian (Latin) (Bosnia and Herzegovina)',), 'code': 'sr-Latn-BA'},
        7: {'name': ('Serbian (Cyrillic) (Bosnia and Herzegovina)',), 'code': 'sr-Cyrl-BA'},
        8: {'name': ('Bosnian (Cyrillic)',), 'code': 'bs-Cyrl-BA'},
    },
    27: {
        'name': 'Slovak',
        'code': 'sk',
        1: {'name': ('.',), 'code': 'sk-SK'},
    },
    28: {
        'name': 'Albanian',
        'code': 'sq',
        1: {'name': ('.',), 'code': 'sq-AL'},
    },
    29: {
        'name': 'Swedish',
        'code': 'sv',
        1: {'name': ('. (Sweden)',), 'code': 'sv-SE'},
        2: {'name': ('. (Finland)',), 'code': 'sv-FI'},
    },
    30: {
        'name': 'Thai',
        'code': 'th',
        1: {'name': ('.',), 'code': 'th-TH'},
    },
    31: {
        'name': 'Turkish',
        'code': 'tr',
        1: {'name': ('.',), 'code': 'tr-TR'},
    },
    32: {
        'name': 'Urdu',
        'code': 'ur',
        1: {'name': ('. (Pakistan)',), 'code': 'ur-PK'},
        2: {'name': ('. (India)',), 'code': 'ur-IN'},
    },
    33: {
        'name': 'Indonesian',
        'code': 'id',
        1: {'name': ('.',), 'code': 'id-ID'},
    },
    34: {
        'name': 'Ukrainian',
        'code': 'uk',
        1: {'name': ('.',), 'code': 'uk-UA'},
    },
    35: {
        'name': 'Byelorussian',
        'code': 'be',
        1: {'name': ('.',), 'code': 'be-BY'},
    },
    36: {
        'name': 'Slovenian',
        'code': 'sl',
        1: {'name': ('.',), 'code': 'sl-SI'},
    },
    37: {
        'name': 'Estonian',
        'code': 'et',
        1: {'name': ('.',), 'code': 'et-EE'},
    },
    38: {
        'name': 'Latvian',
        'code': 'lv',
        1: {'name': ('.',), 'code': 'lv-LV'},
    },
    39: {
        'name': 'Lithuanian',
        'code': 'lt',
        1: {'name': ('.',), 'code': 'lt-LT'},
        2: {'name': ('. (Classic)',), 'code': 'lt-LT'},
    },
    40: {
        'name': 'Tajik',
        'code': 'tg',
        1: {'name': ('.',), 'code': 'tg-TJ'},
    },
    41: {
        'name': 'Farsi',
        'code': 'fa',
        1: {'name': ('.',), 'code': 'fa-IR'},
    },
    42: {
        'name': 'Vietnamese',
        'code': 'vi',
        1: {'name': ('.',), 'code': 'vi-VN'},
    },
    43: {
        'name': 'Armenian',
        'code': 'hy',
        1: {'name': ('.',), 'code': 'hy-AM'},
    },
    44: {
        'name': 'Azeri',
        'code': 'az',
        1: {'name': ('. (Latin)',), 'code': 'az-Latn-AZ'},
        2: {'name': ('. (Cyrillic)',), 'code': 'az-Cyrl-AZ'},
    },
    45: {
        'name': 'Basque',
        'code': 'eu',
        1: {'name': ('.',), 'code': 'eu-ES'},
    },
    46: {
        'name': 'Sorbian',
        'code': 'hsb',
        1: {'name': ('.',), 'code': 'hsb-DE'},
        2: {'name': ('Lower .',), 'code': 'dsb-DE'},
    },
    47: {
        'name': 'Macedonian',
        'code': 'mk',
        1: {'name': ('.',), 'code': 'mk-MK'},
    },
    48: {
        'name': 'Sutu',
        'code': 'st',
        # 'Sutu' is misspelling of Sotho in FF
        1: {'name': ('.',), 'code': 'st-ZA'},
    },
    49: {
        'name': 'Tsonga',
        'code': 'ts',
        1: {'name': ('.',), 'code': 'ts-ZA'},
    },
    50: {
        'name': 'Tswana',
        'code': 'tn',
        1: {'name': ('.',), 'code': 'tn-ZA'},
    },
    51: {
        'name': 'Venda',
        'code': 've',
        1: {'name': ('.',), 'code': 've-ZA'},
    },
    52: {
        'name': 'Xhosa',
        'code': 'xh',
        1: {'name': ('.',), 'code': 'xh-ZA'},
    },
    53: {
        'name': 'Zulu',
        'code': 'zu',
        1: {'name': ('.',), 'code': 'zu-ZA'},
    },
    54: {
        'name': 'Afrikaans',
        'code': 'af',
        1: {'name': ('.',), 'code': 'af-ZA'},
    },
    55: {
        'name': 'Georgian',
        'code': 'ka',
        1: {'name': ('.',), 'code': 'ka-GE'},
    },
    56: {
        'name': 'Faeroese',
        'code': 'fo',
        1: {'name': ('.',), 'code': 'fo-FO'},
    },
    57: {
        'name': 'Hindi',
        'code': 'hi',
        1: {'name': ('.',), 'code': 'hi-IN'},
    },
    58: {
        'name': 'Maltese',
        'code': 'mt',
        1: {'name': ('.',), 'code': 'mt-MT'},
    },
    59: {
        'name': 'Sami',
        'code': 'smi',
        1: {'name': ('. (Lappish)',), 'code': 'smi'},
        2: {'name': ('. (Northern) (Sweden)',), 'code': 'se-SE'},
        3: {'name': ('. (Northern) (Finland)',), 'code': 'se-FI'},
        4: {'name': ('. (Lule) (Norway)',), 'code': 'smj-NO'},
        5: {'name': ('. (Lule) (Sweden)',), 'code': 'smj-SE'},
        6: {'name': ('. (Southern) (Norway)',), 'code': 'sma-NO'},
        7: {'name': ('. (Southern) (Sweden)',), 'code': 'sma-SE'},
        8: {'name': ('. (Skolt)',), 'code': 'sms-FI'},
        9: {'name': ('. (Inari)',), 'code': 'smn-FI'},
    },
    60: {
        'name': 'Gaelic',
        'code': 'gd',
        1: {'name': ('. (Scottish)',), 'code': 'gd-GB'},
        2: {'name': ('. (Irish)',), 'code': 'ga-IE'},
    },
    61: {
        'name': 'Yiddish',
        'code': 'yi',
        1: {'name': ('.',), 'code': 'yi-001'},
    },
    62: {
        'name': 'Malay',
        'code': 'ms',
        1: {'name': ('.',), 'code': 'ms-MY'},
        2: {'name': ('. (Brunei)',), 'code': 'ms-BN'},
    },
    63: {
        'name': 'Kazakh',
        'code': 'kk',
        1: {'name': ('.',), 'code': 'kk-KZ'},
    },
    64: {
        'name': 'Kirghiz',
        'code': 'ky',
        1: {'name': ('.',), 'code': 'ky-KG'},
    },
    65: {
        'name': 'Swahili',
        'code': 'sw',
        1: {'name': ('. (Kenyan)',), 'code': 'sw-KE'},
    },
    66: {
        'name': 'Turkmen',
        'code': 'tk',
        1: {'name': ('.',), 'code': 'tk-TM'},
    },
    67: {
        'name': 'Uzbek',
        'code': 'uz',
        1: {'name': ('. (Latin)',), 'code': 'uz-Latn-UZ'},
        2: {'name': ('. (Cyrillic)',), 'code': 'uz-Cyrl-UZ'},
    },
    68: {
        'name': 'Tatar',
        'code': 'tt',
        1: {'name': ('. (Tatarstan)',), 'code': 'tt-RU'},
    },
    69: {
        'name': 'Bengali',
        'code': 'bn',
        1: {'name': ('.',), 'code': 'bn-IN'},
        2: {'name': ('. Bangladesh',), 'code': 'bn-BD'},
    },
    70: {
        'name': 'Punjabi',
        'code': 'pa',
        1: {'name': ('. (India)',), 'code': 'pa-IN'},
        2: {'name': ('. (Pakistan)',), 'code': 'pa-PK'},
    },
    71: {
        'name': 'Gujarati',
        'code': 'gu',
        1: {'name': ('.',), 'code': 'gu-IN'},
    },
    72: {
        'name': 'Oriya',
        'code': 'or',
        1: {'name': ('.',), 'code': 'or-IN'},
    },
    73: {
        'name': 'Tamil',
        'code': 'ta',
        1: {'name': ('.',), 'code': 'ta-IN'},
    },
    74: {
        'name': 'Telugu',
        'code': 'te',
        1: {'name': ('.',), 'code': 'te-IN'},
    },
    75: {
        'name': 'Kannada',
        'code': 'kn',
        1: {'name': ('.',), 'code': 'kn-IN'},
    },
    76: {
        'name': 'Malayalam',
        'code': 'ml',
        1: {'name': ('.',), 'code': 'ml-IN'},
    },
    77: {
        'name': 'Assamese',
        'code': 'as',
        1: {'name': ('.',), 'code': 'as-IN'},
    },
    78: {
        'name': 'Marathi',
        'code': 'mr',
        1: {'name': ('.',), 'code': 'mr-IN'},
    },
    79: {
        'name': 'Sanskrit',
        'code': 'sa',
        1: {'name': ('.',), 'code': 'sa-IN'},
    },
    80: {
        'name': 'Mongolian',
        'code': 'mn',
        1: {'name': ('. (Cyrillic)',), 'code': 'mn-MN'},
        2: {'name': ('. (Mongolian)',), 'code': 'mn-Mong-CN'},
    },
    81: {
        'name': 'Tibetan',
        'code': 'bo',
        1: {'name': ('. (PRC)',), 'code': 'bo-CN'},
        2: {'name': ('. Bhutan',), 'code': 'bo-BT'},
    },
    82: {
        'name': 'Welsh',
        'code': 'cy',
        1: {'name': ('.',), 'code': 'cy-GB'},
    },
    83: {
        'name': 'Cambodian',
        'code': 'km',
        # Duplicate in FF
        1: {'name': ('.', 'Khmer',), 'code': 'km-KH'},
    },
    84: {
        'name': 'Lao',
        'code': 'lo',
        1: {'name': ('.',), 'code': 'lo-LA'},
    },
    85: {
        'name': 'Burmese',
        'code': 'my',
        1: {'name': ('.',), 'code': 'my-MM'},
    },
    86: {
        'name': 'Galician',
        'code': 'gl',
        1: {'name': ('.',), 'code': 'gl-ES'},
    },
    87: {
        'name': 'Konkani',
        'code': 'kok',
        1: {'name': ('.',), 'code': 'kok-IN'},
    },
    88: {
        'name': 'Manipuri',
        'code': 'mni',
        1: {'name': ('.',), 'code': 'mni-IN'},
    },
    89: {
        'name': 'Sindhi',
        'code': 'sd',
        1: {'name': ('. India',), 'code': 'sd-Deva-IN'},
        2: {'name': ('. Pakistan',), 'code': 'sd-Arab-PK'},
    },
    90: {
        'name': 'Syriac',
        'code': 'syr',
        1: {'name': ('.',), 'code': 'syr-SY'},
    },
    91: {
        'name': 'Sinhalese',
        'code': 'si',
        1: {'name': ('.',), 'code': 'si-LK'},
    },
    92: {
        'name': 'Cherokee',
        'code': 'chr',
        1: {'name': ('.',), 'code': 'chr-US'},
    },
    93: {
        'name': 'Inuktitut',
        'code': 'iu',
        1: {'name': ('.',), 'code': 'iu-Cans-CA'},
        2: {'name': ('. (Latin)',), 'code': 'iu-Latn-CA'},
    },
    94: {
        'name': 'Amharic',
        'code': 'am',
        1: {'name': ('.',), 'code': 'am-ET'},
    },
    95: {
        'name': 'Tamazight',
        'code': 'tzm',
        1: {'name': ('. (Arabic)',), 'code': 'tzm-Arab-MA'},
        2: {'name': ('. (Latin)',), 'code': 'tzm-Latn-DZ'},
    },
    96: {
        'name': 'Kashmiri',
        'code': 'ks',
        2: {'name': ('. (India)',), 'code': 'ks-IN'},
    },
    97: {
        'name': 'Nepali',
        'code': 'ne',
        1: {'name': ('.',), 'code': 'ne-NP'},
        2: {'name': ('. (India)',), 'code': 'ne-IN'},
    },
    98: {
        'name': 'Frisian',
        'code': 'fy',
        1: {'name': ('.',), 'code': 'fy-NL'},
    },
    99: {
        'name': 'Pashto',
        'code': 'ps',
        1: {'name': ('.',), 'code': 'ps-AF'},
    },
    100: {
        'name': 'Filipino',
        'code': 'tl',
        # Duplicate in FF
        1: {'name': ('.', 'Tagalog'), 'code': 'tl-PH'},
    },
    101: {
        'name': 'Divehi',
        'code': 'dv',
        1: {'name': ('.',), 'code': 'dv-MV'},
    },
    102: {
        'name': 'Edo',
        'code': 'bin',
        1: {'name': ('.',), 'code': 'bin'},
    },
    103: {
        'name': 'Fulfulde',
        'code': 'ff',
        1: {'name': ('.',), 'code': 'ff-NG'},
    },
    104: {
        'name': 'Hausa',
        'code': 'ha',
        1: {'name': ('.',), 'code': 'ha-Latn-NG'},
    },
    105: {
        'name': 'Ibibio',
        'code': 'ibb',
        1: {'name': ('.',), 'code': 'ibb-NG'},
    },
    106: {
        'name': 'Yoruba',
        'code': 'yo',
        1: {'name': ('.',), 'code': 'yo-NG'},
    },
    107: {
        'name': 'Quecha',
        'code': 'qu',
        1: {'name': ('. (Bolivia)',), 'code': 'qu-BO'},
        2: {'name': ('. (Ecuador)',), 'code': 'qu-EC'},
        3: {'name': ('. (Peru)',), 'code': 'qu-PE'},
    },
    108: {
        'name': 'Sepedi',
        'code': 'nso',
        1: {'name': ('.',), 'code': 'nso-ZA'},
    },
    109: {
        'name': 'Bashkir',
        'code': 'ba',
        1: {'name': ('.',), 'code': 'ba-RU'},
    },
    110: {
        'name': 'Luxembourgish',
        'code': 'lb',
        1: {'name': ('.',), 'code': 'lb-LU'},
    },
    111: {
        'name': 'Greenlandic',
        'code': 'kl',
        1: {'name': ('.',), 'code': 'kl-GL'},
    },
    112: {
        'name': 'Igbo',
        'code': 'ig',
        1: {'name': ('.',), 'code': 'ig-NG'},
    },
    113: {
        'name': 'Kanuri',
        'code': 'kr',
        1: {'name': ('.',), 'code': 'kr-NG'},
    },
    114: {
        'name': 'Oromo',
        'code': 'om',
        1: {'name': ('.',), 'code': 'om-ET'},
    },
    115: {
        'name': 'Tigrinya',
        'code': 'ti',
        1: {'name': ('. Ethiopia',), 'code': 'ti-ET'},
        2: {'name': ('Tigrinyan Eritrea',), 'code': 'ti-ER'},
    },
    116: {
        'name': 'Guarani',
        'code': 'gn',
        1: {'name': ('.',), 'code': 'gn-PY'},
    },
    117: {
        'name': 'Hawaiian',
        'code': 'haw',
        1: {'name': ('.',), 'code': 'haw-US'},
    },
    118: {
        'name': 'Latin',
        'code': 'la',
        1: {'name': ('.',), 'code': 'la-VA'},
    },
    120: {
        'name': 'Yi',
        'code': 'ii',
        1: {'name': ('.',), 'code': 'ii-CN'},
    },
    121: {
        'name': 'Papiamentu',
        'code': 'pap',
        1: {'name': ('.',), 'code': 'pap-029'},
    },
    122: {
        'name': 'Mapudungun',
        'code': 'arn',
        1: {'name': ('.',), 'code': 'arn'},
    },
    124: {
        'name': 'Mohawk',
        'code': 'mkh',
        1: {'name': ('.',), 'code': 'mkh-CA'},
    },
    126: {
        'name': 'Breton',
        'code': 'br',
        1: {'name': ('.',), 'code': 'br-FR'},
    },
    128: {
        'name': 'Uighur',
        'code': 'ug',
        1: {'name': ('.',), 'code': 'ug-CN'},
    },
    129: {
        'name': 'Maori',
        'code': 'mi',
        1: {'name': ('.',), 'code': 'mi-NZ'},
    },
    130: {
        'name': 'Occitan',
        'code': 'oc',
        1: {'name': ('.',), 'code': 'oc-FR'},
    },
    131: {
        'name': 'Corsican',
        'code': 'co',
        1: {'name': ('.',), 'code': 'co-FR'},
    },
    132: {
        'name': 'Alsatian',
        'code': 'gsw',
        1: {'name': ('.',), 'code': 'gsw-FR'},
    },
    133: {
        'name': 'Sakha',
        'code': 'sah',
        1: {'name': ('.',), 'code': 'sah-RU'},
    },
    134: {
        'name': 'K’iche',
        'code': 'qut',
        1: {'name': ('.',), 'code': 'qut-GT'},
    },
    135: {
        'name': 'Kinyarwanda',
        'code': 'rw',
        1: {'name': ('.',), 'code': 'rw-RW'},
    },
    136: {
        'name': 'Wolof',
        'code': 'wo',
        1: {'name': ('.',), 'code': 'wo-SN'},
    },
    140: {
        'name': 'Dari',
        'code': 'fa',
        1: {'name': ('.',), 'code': 'fa-AF'},
    },
}


def languageCodeIterator(useTableInFontTools: bool = False):
    """Language code data iterator

    This iterator yields 3-tuple consisting of MS language ID,
    universal language code, and language name. For example,
    ``(0x409, 'en-US', 'English (US)')``.
    """
    for lsb, langData in languageData.items():
        for msb, subLangData in langData.items():
            if isinstance(msb, int):
                winLang = msb * 1024 + lsb
                if useTableInFontTools:
                    name = subLangData['name'][0]
                    if winLang == 0x40a:    # Skip Spanish (traditional sort)
                        pass
                    elif winLang == 0xc0a:  # Spanish (modern sort)
                        yield (winLang, _WINDOWS_LANGUAGES[winLang], 'Spanish (Spain)')
                    elif winLang in _WINDOWS_LANGUAGES:
                        yield (winLang, _WINDOWS_LANGUAGES[winLang], name.replace('.', langData['name']))
                else:
                    for name in subLangData['name']:
                        yield (winLang, subLangData['code'], name.replace('.', langData['name']))


def languageCodeReverseLookup(langName: str) -> str | None:
    """Lookup language code from language name"""
    for i, c, n in languageCodeIterator():
        if n == langName:
            return c
    return None
