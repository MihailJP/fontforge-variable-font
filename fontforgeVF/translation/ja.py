translation_ja = {
    # common
    'Yes': 'はい',
    'No': 'いいえ',
    '_Yes': 'はい (_Y)',
    '_No': 'いいえ (_N)',
    # '_OK': '_OK',
    '_Cancel': 'キャンセル (_C)',

    # __main__.py
    '_Variable Font': '可変フォント (_V)',
    '_Open a variable font': '可変フォントを開く (_O)',
    'By named _instance...': 'インスタンス名を指定 (_I)...',
    'By _parameter...': 'パラメータを指定 (_P)...',
    '_Generate a variable font...': '可変フォントを生成 (_G)...',
    'Design _axes...': 'デザイン軸 (_A)...',
    'Named _instances...': '名前付きインスタンス (_I)...',
    '_Delete VF info': '可変フォント情報を削除 (_D)',

    # design_axes.py
    'Italic': 'イタリック',
    'Optical Size': 'オプティカルサイズ',
    'Slant': '傾き',
    'Width': '幅',
    'Weight': '太さ',
    'Custom 1': 'カスタム1',
    'Custom 2': 'カスタム2',
    'Custom 3': 'カスタム3',
    'Unset': '未設定',
    'Set': '設定',
    'Default ({0})': 'デフォルト ({0})',
    '\tLabels:': '\tラベル:',
    '{0} tag:': '{0}のタグ:',
    'This master': 'このマスター',
    'Custom axes': 'カスタム軸',
    'Axis map': '軸マップ',
    'Axis order': '軸の順序',
    'Axis names': '軸の名前',
    'Design axes': 'デザイン軸',

    # export.py
    'Failed to export': 'エクスポートに失敗しました',
    "'{0}' failed with return code {1}": "'{0}' がリターンコード {1} で失敗しました",
    'Finished': '完了',
    'Finished to output variable fonts': '可変フォントの出力が完了しました',
    '_Roman VF:': '正立体のVF (_R):',
    '_Italic VF:': 'イタリックのVF (_I):',
    '_Save as:': '保存先 (_S):',
    'Options:': 'オプション:',
    'Decompose _nested refs': 'ネストした参照を分解 (_N)',
    'Decompose _transformed refs': '変形した参照を分解 (_T)',
    "Add '_aalt' feature": "'_aalt' 機能を追加",
    'Save variable font': '可変フォントを保存',

    # instance.py
    'PostScript Name:': 'PostScript名:',
    'Subfamily Name:': 'サブファミリ名:',
    'Instance {0}': 'インスタンス{0}',
    'Named instances': '名前付きインスタンス',

    # language.py
    'Localized names {0}': 'ローカライズ名 {0}',
    'Language:': '言語:',
    # TODO: language names

    # load.py
    'Please specify an instance to open': '開くインスタンスを指定してください',
    'Choose instance(s) to open': '開くインスタンスを選択してください',
    'Instances in this font': 'フォントに含まれるインスタンス',
    'Variable font': '可変フォント',
    (
        'This font has variable font metadata in its persistent dict.\n'
        'Did you intend to output a variable font?\n'
        '(all masters need to be opened beforehand)'
    ): (
        'このフォントの persistent dict に可変フォントのメタデータが含まれています。\n'
        '可変フォントを出力しますか？\n'
        '(事前にすべてのマスターを開いておく必要があります)'
    ),
    (
        "The font '{0}' in\n"
        "'{1}'\n"
        "seems to be a variable font.\n"
        "Would you like to open another instance of this font?"
    ): (
        "'{1}'\n"
        "内のフォント '{0}'\n"
        "は可変フォントのようです。\n"
        "このフォントの他のインスタンスを開きますか？"
    ),
    'Open with _parameters': 'パラメータを指定して開く (_P)',

    # utils.py
    'Data loss warning': 'データが失われます',
    (
        "In active font, `font.persistent` exists but is other than a dict.\n"
        "This will be overwritten if you continue."
    ): (
        "現在のフォントには `font.persistent` が存在しますが辞書型ではありません。\n"
        "このまま続けると上書きされます。"
    ),
}
