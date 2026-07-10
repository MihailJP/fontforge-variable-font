translation_fr = {
    # common
    'Yes': 'Oui',
    'No': 'Non',
    '_Yes': '_Oui',
    '_No': '_Non',
    # '_OK': '_OK',
    '_Cancel': '_Annuler',

    # __main__.py
    '_Variable Font': 'Fonte _variable',
    '_Open a variable font': '_Ouvrir une fonte variable',
    'By named _instance...': 'Par _instance nommée...',
    'By _parameter...': '_Par paramètre...',
    '_Generate a variable font...': '_Générer une fonte variable...',
    'Design _axes...': '_Axes de conception...',
    'Named _instances...': '_Instances nommées...',
    '_Delete VF info': '_Supprimer les infos sur FV',

    # design_axes.py
    'Italic': 'Italique',
    'Optical Size': 'Taille optique',
    'Slant': 'Pente',
    'Width': 'Chasse',
    'Weight': 'Graisse',
    'Custom 1': 'Personnalisé 1',
    'Custom 2': 'Personnalisé 2',
    'Custom 3': 'Personnalisé 3',
    'Unset': 'Non défini',
    'Set': 'Défini',
    'Default ({0})': 'Défaut ({0})',
    '\tLabels:': '\tÉtiquettes:',
    '{0} tag:': 'Attribut de {0}:',
    'This master': 'Ce maître',
    'Custom axes': 'Axes personnalisés',
    'Axis map': 'Application des axes',
    'Axis order': 'Ordre des axes',
    'Axis names': 'Noms des axes',
    'Design axes': 'Axes de conception',

    # export.py
    'Failed to export': 'Échec de l\'exportation',
    "'{0}' failed with return code {1}": "«{0}» a échoué avec le code de retour {1}",
    'Finished': 'Fini',
    'Finished to output variable fonts': 'Finalisé pour générer de la fonte variable',
    '_Roman VF:': 'FV _Romaine:',
    '_Italic VF:': 'FV _Italique:',
    '_Save as:': 'Enregi_strer sous:',
    # 'Options:': 'Options:',
    'Decompose _nested refs': 'Décomposer les référe_nces imbriquées',
    'Decompose _transformed refs': 'Décomposer les références _transformées',
    "Add '_aalt' feature": "Ajouter la fonctionnalité «_aalt»",
    'Save variable font': 'Enregistrer la fonte variable',

    # instance.py
    'PostScript Name:': 'Nom PostScript:',
    'Subfamily Name:': 'Nom de la sous-famille:',
    # 'Instance {0}': 'Instance {0}',
    'Named instances': 'Instances nommées',

    # language.py
    'Localized names {0}': 'Noms localisés {0}',
    'Language:': 'Langue:',
    # TODO: language names

    # load.py
    'Please specify an instance to open': 'Veuillez spécifier une instance à ouvrir',
    'Choose instance(s) to open': 'Choisir la ou les instances à ouvrir',
    'Instances in this font': 'L\'instances dans cette fonte',
    'Open a variable font': 'Ouvrir une fonte variable',
    "{0} does not have 'fvar' table": "{0} ne possède pas de table «\u00a0fvar\u00a0»",
    "{0} has 'fvar' table but all axes are fixed": "{0} possède une table «\u00a0fvar\u00a0», mais tous les axes sont fixes.",
    'Variable font': 'Fonte variable',
    (
        'This font has variable font metadata in its persistent dict.\n'
        'Did you intend to output a variable font?\n'
        '(all masters need to be opened beforehand)'
    ): (
        'Cette fonte contient des métadonnées de fonte variable dans son dict «persistent».\n'
        'Aviez-vous l\'intention de générer une fonte variable\u00a0?\n'
        '(tous les maîtres doivent être ouverts au préalable)'
    ),
    (
        "The font '{0}' in\n"
        "'{1}'\n"
        "seems to be a variable font.\n"
        "Would you like to open another instance of this font?"
    ): (
        "La fonte «{0}» dans\n"
        "«{1}»\n"
        "semble être une fonte variable.\n"
        "Souhaitez-vous ouvrir une autre instance de cette fonte\u00a0?"
    ),
    'Open with _parameters': 'Ouvrir avec des _paramètres',

    # utils.py
    'Data loss warning': 'Avertissement de perte de données',
    (
        "In active font, `font.persistent` exists but is other than a dict.\n"
        "This will be overwritten if you continue."
    ): (
        "Dans la fonte active, `font.persistent` existe mais n'est pas un dict.\n"
        "Ceci sera écrasé si vous continuez."
    ),
}
