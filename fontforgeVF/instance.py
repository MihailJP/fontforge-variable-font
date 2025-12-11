import fontforge
from fontforgeVF import utils
from fontforgeVF.design_axes import designAxes


def _instances_getval(font: fontforge.font, cnt: int, key: str, defaultVal):
    instances = utils.getVFValue(font, 'instances', [])
    if (cnt - 1) < len(instances):
        if isinstance(instances[cnt - 1], dict):
            if key in instances[cnt - 1]:
                return instances[cnt - 1][key]
    return defaultVal


def _prepareQuestions_instances(cnt: int):
    font = fontforge.activeFont()
    questions = [
        {
            'type': 'string',
            'question': 'PostScript Name:',
            'tag': 'psName' + str(cnt),
            'default': _instances_getval(font, cnt, 'psName', ''),
        },
        {
            'type': 'string',
            'question': 'Subfamily Name:',
            'tag': 'name' + str(cnt),
            'default': _instances_getval(font, cnt, 'name', ''),
        },
    ]
    for k, v in designAxes.items():
        if utils.getVFValue(font, 'axes.' + k + '.active'):
            if k == 'ital':
                val = _instances_getval(font, cnt, 'ital', False)
                questions.append({
                    'type': 'choice',
                    'question': v['name'] + ':',
                    'tag': k + '_' + str(cnt),
                    'checks': True,
                    'answers': [
                        {'name': 'No', 'tag': '0', 'default': not val},
                        {'name': 'Yes', 'tag': '1', 'default': val},
                    ],
                })
            else:
                questions.append({
                    'type': 'string',
                    'question': v['name'] + ':',
                    'tag': k + '_' + str(cnt),
                    'default': str(_instances_getval(font, cnt, k, '')),
                })
    return questions


def _prepareQuestions():
    font = fontforge.activeFont()
    questions = []
    for i in range(max(((len(utils.getVFValue(font, 'instances', [])) + 7) // 4) * 4, 8)):
        questions.append({
            'category': _instances_getval(font, i + 1, 'name', 'Instance ' + str(i + 1)),
            'questions': _prepareQuestions_instances(i + 1)
        })
    return questions


def _saveInstances(result: dict):
    print(result)
    font = fontforge.activeFont()
    instanceList = []
    cnt = 1
    while 'psName' + str(cnt) in result:
        if result['psName' + str(cnt)]:
            instance = {'psName': result['psName' + str(cnt)]}
            instance['name'] = result['name' + str(cnt)]
            for k, v in designAxes.items():
                if k + '_' + str(cnt) not in result:
                    pass
                elif k == 'ital':
                    instance['ital'] = bool(int(result['ital_' + str(cnt)]))
                else:
                    instance[k] = utils.intOrFloat(result[k + '_' + str(cnt)])
            instanceList.append(instance)
        cnt += 1
    utils.setVFValue(font, 'instances', instanceList)


def instanceMenu(u, glyph):
    result = fontforge.askMulti("Named instances", _prepareQuestions())
    if result:
        _saveInstances(result)


def instanceEnable(u, glyph):
    return True
