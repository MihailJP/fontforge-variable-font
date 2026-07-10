translation_zh_CN = {
    # common
    'Yes': '是',
    'No': '不',
    '_Yes': '是 (_Y)',
    '_No': '不 (_N)',
    '_OK': '确定 (_O)',
    '_Cancel': '取消 (_C)',

    # __main__.py
    '_Variable Font': '可变字体 (_V)',
    '_Open a variable font': '打开可变字体 (_O)',
    'By named _instance...': '按命名实例 (_I)...',
    'By _parameter...': '根据参数 (_P)...',
    '_Generate a variable font...': '生成可变字体 (_G)...',
    'Design _axes...': '设计轴 (_A)...',
    'Named _instances...': '命名实例 (_I)...',
    '_Delete VF info': '删除可变字体信息 (_D)',

    # design_axes.py
    'Italic': '斜体',
    'Optical Size': '光学尺寸',
    'Slant': '倾斜角',
    'Width': '宽度',
    'Weight': '字重',
    'Custom 1': '自定义1',
    'Custom 2': '自定义2',
    'Custom 3': '自定义3',
    'Unset': '没有',
    'Set': '有',
    'Default ({0})': '默认 ({0})',
    '\tLabels:': '\t标签:',
    '{0} tag:': '{0}的tag:',
    'This master': '这个母版',
    'Custom axes': '自定义轴',
    'Axis map': '轴映射',
    'Axis order': '轴序',
    'Axis names': '轴名称',
    'Design axes': '设计轴',

    # export.py
    'Failed to export': '导出失败了',
    "'{0}' failed with return code {1}": "'{0}' 失败了，返回码为 {1}",
    'Finished': '完成了',
    'Finished to output variable fonts': '完成输出可变字体了',
    '_Roman VF:': '罗马体VF (_R):',
    '_Italic VF:': '斜体VF (_I):',
    '_Save as:': '另存为 (_S):',
    'Options:': '选项:',
    'Decompose _nested refs': '分解嵌套参照 (_N)',
    'Decompose _transformed refs': '分解已变换的参照 (_T)',
    "Add '_aalt' feature": "添加 '_aalt' 功能",
    'Save variable font': '保存可变字体',

    # instance.py
    'PostScript Name:': 'PostScript名:',
    'Subfamily Name:': '子族名:',
    'Instance {0}': '实例{0}',
    'Named instances': '命名实例',

    # language.py
    'Localized names {0}': '本地化名称 {0}',
    'Language:': '语言:',
    # TODO: language names

    # load.py
    'Please specify an instance to open': '请指定要打开的实例。',
    'Choose instance(s) to open': '选择要打开的实例',
    'Instances in this font': '此字体的实例',
    'Open a variable font': '打开可变字体',
    "{0} does not have 'fvar' table": "{0} 没有 'fvar' 列表",
    "{0} has 'fvar' table but all axes are fixed": "{0} 包含 ‘fvar’ 列表，但所有轴均已固定",
    'Variable font': '可变字体',
    (
        'This font has variable font metadata in its persistent dict.\n'
        'Did you intend to output a variable font?\n'
        '(all masters need to be opened beforehand)'
    ): (
        '该字体在其 persistent dict 中包含可变字体元数据。\n'
        '要不要输出可变字体吗？\n'
        '(所有母版都需要预先打开。)'
    ),
    (
        "The font '{0}' in\n"
        "'{1}'\n"
        "seems to be a variable font.\n"
        "Would you like to open another instance of this font?"
    ): (
        "'{1}'\n"
        "中的字体 '{0}'\n"
        "似乎是可变字体。\n"
        "要不要打开该字体的另一个实例吗？"
    ),
    'Open with _parameters': '带参数打开 (_P)',

    # utils.py
    'Data loss warning': '数据丢失警告',
    (
        "In active font, `font.persistent` exists but is other than a dict.\n"
        "This will be overwritten if you continue."
    ): (
        "在现在字体中，存在 `font.persistent`，但其类型并非dict。\n"
        "如果继续，这将遭到覆盖。"
    ),
}
