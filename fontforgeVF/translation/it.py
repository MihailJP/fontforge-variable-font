translation_it = {
    # common
    'Yes': 'Sì',
    'No': 'Non',
    '_Yes': '_Sì',
    '_No': '_Non',
    # '_OK': '_OK',
    '_Cancel': '_Annulla',

    # __main__.py
    '_Variable Font': 'Font _variabile',
    '_Open a variable font': '_Apri un font variabile',
    'By named _instance...': 'Tramite _istanza denominata...',
    'By _parameter...': 'Tramite _parametro...',
    '_Generate a variable font...': '_Crea un font variabile...',
    'Design _axes...': 'A_ssi di progettazione...',
    'Named _instances...': '_Istanze denominate...',
    '_Delete VF info': '_Elimina le informazioni sul FV',

    # design_axes.py
    'Italic': 'Corsivo',
    'Optical Size': 'Dimensione ottica',
    'Slant': 'Inclinazione',
    'Width': 'Larghezza',
    'Weight': 'Peso',
    'Custom 1': 'Personalizzato 1',
    'Custom 2': 'Personalizzato 2',
    'Custom 3': 'Personalizzato 3',
    'Unset': 'Annullato',
    'Set': 'Definito',
    'Default ({0})': 'Predefinito ({0})',
    '\tLabels:': '\tEtichette:',
    '{0} tag:': 'Etichetta di {0}:',
    'This master': 'Questo maestro',
    'Custom axes': 'Assi personalizzati',
    'Axis map': 'Mappa degli assi',
    'Axis order': 'Ordine degli assi',
    'Axis names': 'Nomi degli assi',
    'Design axes': 'Assi di progettazione',

    # export.py
    'Failed to export': 'Esportazione non riuscita',
    "'{0}' failed with return code {1}": "'{0}' non è riuscito con codice di ritorno {1}",
    'Finished': 'Completato',
    'Finished to output variable fonts': 'Completato per generare il font variabile',
    '_Roman VF:': 'FV _Romano:',
    '_Italic VF:': 'FV _in Corsivo:',
    '_Save as:': '_Salva con nome:',
    'Options:': 'Opzioni:',
    'Decompose _nested refs': 'Scompo_ni i riferimenti annidati',
    'Decompose _transformed refs': 'Scomponi i riferimenti _trasformati',
    "Add '_aalt' feature": "Aggiungi la funzionalità '_aalt'",
    'Save variable font': 'Salva il font variabile',

    # instance.py
    'PostScript Name:': 'Nome PostScript:',
    'Subfamily Name:': 'Nome della sottofamiglia:',
    'Instance {0}': 'Istanza {0}',
    'Named instances': 'Istanze denominate',

    # language.py
    'Localized names {0}': 'Nomi localizzati {0}',
    'Language:': 'Lingua:',
    # TODO: language names

    # load.py
    'Please specify an instance to open': 'Si prega di specificare un\'istanza da aprire',
    'Choose instance(s) to open': 'Scegli l\'istanza o le istanze da aprire',
    'Instances in this font': 'Istanze in questo font',
    'Open a variable font': 'Apri un font variabile',
    "{0} does not have 'fvar' table": "{0} non possiede la tabella 'fvar'",
    "{0} has 'fvar' table but all axes are fixed": "{0} possiede una tabella 'fvar', ma tutti gli assi sono fissi.",
    'Variable font': 'Font variabile',
    (
        'This font has variable font metadata in its persistent dict.\n'
        'Did you intend to output a variable font?\n'
        '(all masters need to be opened beforehand)'
    ): (
        'Questo font ha metadati di font variabile nel suo dict persistent.\n'
        'Intendevi generare un font variabile?\n'
        '(Tutti i maestri devono essere aperti in precedenza)'
    ),
    (
        "The font '{0}' in\n"
        "'{1}'\n"
        "seems to be a variable font.\n"
        "Would you like to open another instance of this font?"
    ): (
        "Il font «{0}» in\n"
        "«{1}»\n"
        "sembra essere un font variabile.\n"
        "Desideri aprire un'altra istanza di questo font?"
    ),
    'Open with _parameters': 'Apri tramite _parametri',

    # utils.py
    'Data loss warning': 'Avviso di perdita di dati',
    (
        "In active font, `font.persistent` exists but is other than a dict.\n"
        "This will be overwritten if you continue."
    ): (
        "Nel font attivo, `font.persistent` esiste ma non è un dict.\n"
        "Questo verrà sovrascritto se si continua."
    ),
}
