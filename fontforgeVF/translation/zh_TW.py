translation_zh_TW = {
    # common
    'Yes': '是',
    'No': '不',
    '_Yes': '是 (_Y)',
    '_No': '不 (_N)',
    '_OK': '確定 (_O)',
    '_Cancel': '取消 (_C)',

    # __main__.py
    '_Variable Font': '可變字型 (_V)',
    '_Open a variable font': '開啟可變字型 (_O)',
    'By named _instance...': '按命名實例 (_I)...',
    'By _parameter...': '按參數 (_P)...',
    '_Generate a variable font...': '產生可變字型 (_G)...',
    'Design _axes...': '設計軸 (_A)...',
    'Named _instances...': '命名實例 (_I)...',
    '_Delete VF info': '刪除可變字型訊息(_D)',

    # design_axes.py
    'Italic': '斜體',
    'Optical Size': '光學尺寸',
    'Slant': '斜角',
    'Width': '寬度',
    'Weight': '字重',
    'Custom 1': '自訂1',
    'Custom 2': '自訂2',
    'Custom 3': '自訂3',
    'Unset': '未設定',
    'Set': '設定',
    'Default ({0})': '預設 ({0})',
    '\tLabels:': '\t標籤:',
    '{0} tag:': '{0}的tag:',
    'This master': '這個主',
    'Custom axes': '自訂軸',
    'Axis map': '軸對應',
    'Axis order': '軸順序',
    'Axis names': '軸名稱',
    'Design axes': '設計軸',

    # export.py
    'Failed to export': '匯出失敗了',
    "'{0}' failed with return code {1}": "'{0}' 失敗了，回傳代碼為 {1}",
    'Finished': '完成了',
    'Finished to output variable fonts': '完成輸出可變字型了',
    '_Roman VF:': '羅馬體VF (_R):',
    '_Italic VF:': '斜體VF (_I):',
    '_Save as:': '另存為 (_S):',
    'Options:': '選項:',
    'Decompose _nested refs': '分解嵌套參照 (_N)',
    'Decompose _transformed refs': '分解已轉換的參照 (_T)',
    "Add '_aalt' feature": "新增 '_aalt' 功能",
    'Save variable font': '儲存可變字型',

    # instance.py
    'PostScript Name:': 'PostScript名:',
    'Subfamily Name:': '子族名:',
    'Instance {0}': '實例{0}',
    'Named instances': '命名實例',

    # language.py
    'Localized names {0}': '本地化名稱 {0}',
    'Language:': '語言:',
    # TODO: language names

    # load.py
    'Please specify an instance to open': '請指定要開啟的實例',
    'Choose instance(s) to open': '選擇要開啟的實例',
    'Instances in this font': '此字型中的實例',
    'Open a variable font': '開啟可變字型',
    "{0} does not have 'fvar' table": "{0} 沒有 'fvar' 列表",
    "{0} has 'fvar' table but all axes are fixed": "{0} 包含 'fvar' 列表，但所有軸都已固定。",
    'Variable font': '可變字型',
    (
        'This font has variable font metadata in its persistent dict.\n'
        'Did you intend to output a variable font?\n'
        '(all masters need to be opened beforehand)'
    ): (
        '該字型在其 persistent dict 中具有可變字型元資料。\n'
        '要不要輸出可變字型嗎？\n'
        '(所有主都需要事先開啟。)'
    ),
    (
        "The font '{0}' in\n"
        "'{1}'\n"
        "seems to be a variable font.\n"
        "Would you like to open another instance of this font?"
    ): (
        "'{1}'\n"
        "中的字型 '{0}'\n"
        "似乎是可變字型。\n"
        "要不要開啟此字型的另一個實例嗎？"
    ),
    'Open with _parameters': '開啟並設定參數 (_P)',

    # utils.py
    'Data loss warning': '資料遺失警告',
    (
        "In active font, `font.persistent` exists but is other than a dict.\n"
        "This will be overwritten if you continue."
    ): (
        "在現在字型中，`font.persistent` 存在，但不是dict。\n"
        "如果您繼續操作，此設定將被覆蓋。"
    ),
}
