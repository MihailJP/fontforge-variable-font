translation_es = {
    # common
    'Yes': 'Sí',
    # 'No': 'No',
    '_Yes': '_Sí',
    # '_No': '_No',
    # '_OK': '_OK',
    '_Cancel': '_Cancelar',

    # __main__.py
    '_Variable Font': 'Fuente _variable',
    '_Open a variable font': '_Abrir una fuente variable',
    'By named _instance...': 'Por _instancia con nombre...',
    'By _parameter...': 'Con _parámetros...',
    '_Generate a variable font...': '_Generar una fuente variable...',
    'Design _axes...': '_Ejes de diseño...',
    'Named _instances...': '_Instancias con nombre...',
    '_Delete VF info': 'E_liminar información de FV',

    # design_axes.py
    'Italic': 'Cursiva',
    'Optical Size': 'Tamaño óptico',
    'Slant': 'Pendiente',
    'Width': 'Ancho',
    'Weight': 'Peso',
    'Custom 1': 'Personalizado 1',
    'Custom 2': 'Personalizado 2',
    'Custom 3': 'Personalizado 3',
    'Unset': 'Desactivado',
    'Set': 'Activo',
    'Default ({0})': 'Preselección ({0})',
    '\tLabels:': '\tEtiqueta:',
    '{0} tag:': 'Etiqueta de {0}:',
    'This master': 'Este maestro',
    'Custom axes': 'Eje personalizado',
    'Axis map': 'Mapa de los ejes',
    'Axis order': 'Orden de los ejes',
    'Axis names': 'Nombres de los ejes',
    'Design axes': 'Ejes de diseño',

    # export.py
    'Failed to export': 'No se pudo exportar',
    "'{0}' failed with return code {1}": "'{0}' falló con el código de retorno {1}",
    'Finished': 'Finalizado',
    'Finished to output variable fonts': 'Finalizado para generar fuentes variables',
    '_Roman VF:': 'FV _Romana:',
    '_Italic VF:': 'FV en Curs_iva:',
    '_Save as:': '_Guardar como:',
    'Options:': 'Opciones:',
    'Decompose _nested refs': 'Descomponer referencias anidadas',
    'Decompose _transformed refs': 'Descomponer referencias transformadas',
    "Add '_aalt' feature": "_Añadir la función 'aalt'",
    'Save variable font': 'Guardar la fuente variable',

    # instance.py
    'PostScript Name:': 'Nombre PostScript:',
    'Subfamily Name:': 'Nombre de la subfamilia:',
    'Instance {0}': 'Instancia {0}',
    'Named instances': 'Instancias con nombre',

    # language.py
    'Localized names {0}': 'Nombres localizados {0}',
    'Language:': 'Idioma:',
    # TODO: language names

    # load.py
    'Please specify an instance to open': 'Por favor, especifique una instancia para abrir',
    'Choose instance(s) to open': 'Seleccione la(s) instancia(s) que desea abrir',
    'Instances in this font': 'Instancias en esta fuente',
    'Open a variable font': 'Abrir una fuente variable',
    "{0} does not have 'fvar' table": "{0} no tiene la tabla 'fvar'",
    "{0} has 'fvar' table but all axes are fixed": "{0} tiene una tabla 'fvar', pero todos los ejes están fijos.",
    'Variable font': 'Fuente variable',
    (
        'This font has variable font metadata in its persistent dict.\n'
        'Did you intend to output a variable font?\n'
        '(all masters need to be opened beforehand)'
    ): (
        'Esta fuente contiene metadatos de fuente variables en su dict persistent.\n'
        '¿Deseaba generar una fuente variable?\n'
        '(Es necesario abrir previamente todos los maestros)'
    ),
    (
        "The font '{0}' in\n"
        "'{1}'\n"
        "seems to be a variable font.\n"
        "Would you like to open another instance of this font?"
    ): (
        "La fuente «{0}» en\n"
        "'{1}'\n"
        "parece ser una fuente variable.\n"
        "¿Desea abrir otra instancia de esta fuente?"
    ),
    'Open with _parameters': 'Abrir con _parámetros',

    # utils.py
    'Data loss warning': 'Advertencia de pérdida de datos',
    (
        "In active font, `font.persistent` exists but is other than a dict.\n"
        "This will be overwritten if you continue."
    ): (
        "En la fuente activa, `font.persistent` existe, pero no es un dict.\n"
        "Se sobrescribirá si continúa."
    ),
}
