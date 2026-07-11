translation_ko = {
    # common
    'Yes': '예',
    'No': '아니오',
    '_Yes': '예 (_Y)',
    '_No': '아니오 (_N)',
    '_OK': '확인 (_O)',
    '_Cancel': '취소 (_C)',

    # __main__.py
    '_Variable Font': '가변 폰트 (_V)',
    '_Open a variable font': '가변 폰트를 열기 (_O)',
    'By named _instance...': '인스턴스명으로 (_I)...',
    'By _parameter...': '매개변수로 (_P)...',
    '_Generate a variable font...': '가변 폰트를 생성 (_G)...',
    'Design _axes...': '디자인 축 (_A)...',
    'Named _instances...': '명명된 인스턴스 (_I)...',
    '_Delete VF info': '가변 폰트 정보 삭제 (_D)',

    # design_axes.py
    'Italic': '이탤릭',
    'Optical Size': '광학적 크기',
    'Slant': '기울기',
    'Width': '폭',
    'Weight': '가중치',
    'Custom 1': '사용자정의1',
    'Custom 2': '사용자정의2',
    'Custom 3': '사용자정의3',
    'Unset': '미설정',
    'Set': '설정',
    'Default ({0})': '디폴트 ({0})',
    '\tLabels:': '\t라벨:',
    '{0} tag:': '{0} 태그:',
    'This master': '이 마스터',
    'Custom axes': '사용자정의 축',
    'Axis map': '축 맵',
    'Axis order': '축 순서',
    'Axis names': '축 이름',
    'Design axes': '디자인 축',

    # export.py
    'Failed to export': '내보내기 실패',
    "'{0}' failed with return code {1}": "'{0}'이(가) 반환 코드 {1}(으)로 실패했습니다.",
    'Finished': '완료',
    'Finished to output variable fonts': '가변 폰트 출력이 완료했습니다.',
    '_Roman VF:': '로만채 VF (_R):',
    '_Italic VF:': '이탤릭 VF (_I):',
    '_Save as:': '저장 파일명 (_S):',
    'Options:': '옵션:',
    'Decompose _nested refs': '중첩된 참조를 분해 (_N)',
    'Decompose _transformed refs': '변형된 참조를 분해 (_T)',
    "Add '_aalt' feature": "'_aalt' 기능을 추가",
    'Save variable font': '가변 폰트를 저장',

    # instance.py
    'PostScript Name:': 'PostScript 명:',
    'Subfamily Name:': '하위패밀리명:',
    'Instance {0}': '인스턴스 {0}',
    'Named instances': '명명된 인스턴스',

    # language.py
    'Localized names {0}': '현지화명 {0}',
    'Language:': '언어:',
    # TODO: language names

    # load.py
    'Please specify an instance to open': '열 인스턴스를 지정해 주십시오',
    'Choose instance(s) to open': '열 인스턴스를 선택하십시오',
    'Instances in this font': '이 폰트의 인스턴스',
    'Open a variable font': '가변 폰트를 열기',
    "{0} does not have 'fvar' table": "{0}에 'fvar' 테이블이 없습니다.",
    "{0} has 'fvar' table but all axes are fixed": "{0}에 'fvar' 테이블이 있지만 모든 축이 고정되어 있습니다.",
    'Variable font': '가변 폰트',
    (
        'This font has variable font metadata in its persistent dict.\n'
        'Did you intend to output a variable font?\n'
        '(all masters need to be opened beforehand)'
    ): (
        '이 폰트는 persistent dict에 가변 폰트 메타데이터를 포함하고 있습니다.\n'
        '가변 폰트를 출력하려고 하셨나요?\n'
        '(모든 마스터는 사전에 열려 있어야 합니다)'
    ),
    (
        "The font '{0}' in\n"
        "'{1}'\n"
        "seems to be a variable font.\n"
        "Would you like to open another instance of this font?"
    ): (
        "'{1}'\n"
        "의 폰트 '{0}'\n"
        "은 가변 폰트인 것 같습니다.\n"
        "이 폰트의 다른 인스턴스를 열겠습니까?"
    ),
    'Open with _parameters': '매개변수를 지정해 열기 (_P)',

    # utils.py
    'Data loss warning': '데이터 손실 경고',
    (
        "In active font, `font.persistent` exists but is other than a dict.\n"
        "This will be overwritten if you continue."
    ): (
        "현재 폰트에서 `font.persistent`는 존재하지만 dict가 아닙니다.\n"
        "계속하면 덮어쓰기됩니다."
    ),
}
