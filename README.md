Fontforge Variable Font Plugin
==============================

A FontForge_plugin to create a variable font

As of October 2025, Fontforge supports legacy (maybe obsolete) multiple
master formats but not yet OpenType variable fonts. This plugin adds
frontend of [fontmake](https://pypi.org/project/fontmake/) and
[fonttools](https://pypi.org/project/fonttools/) so that variable fonts can
be created through Fontforge interface.

This module can also export to WOFF2; in this case the
[woff2](https://github.com/google/woff2) tool will be used as backend.

This module requires Python 3.10 or later.

Install
-------

```shell
pip3 install fontforge-variable-font
```

### Make sure Fontforge Python module is usable

In interactive mode of Python, run:

```python
import fontforge
```

If it raises ``ModuleNotFoundError`` exception, install Fontforge first. If
installed, make sure the build option set that the Python module gets also
installed. If already so, Python interpreter does not recognize the module
path where the required module.

```shell
export PYTHONPATH=/path/to/fontforge/python/module:$PYTHONPATH
```

Usage
-----

### Interactive usage

As a Fontforge plugin, fontforgeVF adds 'Variable Font' submenu to 'Tools'
menu which is dedicated for plugins.

- Variable Font
  - Open a variable font
    - By named instance...
    - By parameter...
  - Generate a variable font...
  - Design axes...
  - Named instances...
  - Delete VF info

> [!IMPORTANT]
> Since the plugin feature has been hardly (maybe never) used (hence it can
> be tested not well,) Fontforge may crash especially after a dialog is shown.
> You are advised to back up your font project before use.

#### Open a variable font

Shows a dialog to open a variable font

> [!TIP]
> If you open a webfont (WOFF2,) the plugin will first copy it to a temporary
> directory, then decompress with calling ``woff2_decompress`` in order to
> open as a TTF.

> [!TIP]
> VF-specific metadata will be loaded to ``font.persistent``.
> Minimum, default, and maximum values of axis values are also loaded in
> ``font.persistent['VF']``, but are not used when re-exporting.

##### By named instance

Open file dialog is shown first. If a variable font is selected, then another
dialog is shown to select (one or more) named instances. If a non-variable
font is selected, simply opens that font.

> [!NOTE]
> If an empty list gets shown, the font does not have any named instances.
> Use 'By parameter' in such case.

##### By parameter

Like above, but the second dialog is not to select a named instance, but to
specify design axis parameters.

> [!TIP]
> Valid range will be shown together with the name for each axis.

#### Generate a variable font

Shows a dialog where you can set output file name and other options.

In order to build a variable font, SFD must be converted into UFO and
create a designspace document. This plugin will do this first, and
then required modification. The required files will be created in a
temporary directory, and deleted after everything is done. So users
won't see intermediate files.

Fontforge may export with ``postscriptIsFixedPitch`` flag clear when
it should be set. The plugin checks if monospaced font is intended and
fix the flag. Unlike Fontforge itself, only U+0020 to U+007E will be
checked their width, because combining marks may have zero width even
for monospaced fonts.

In a feature file, 'aalt' feature is specially treated. Fontforge may
export incompatible 'aalt' feature (concretely 'script' or 'language'
instructions must not be included unlike other features.) This
function fix this first.

> [!TIP]
> You do not have to add 'aalt' lookups manually. You can still do it for
> 'aalt'-only glyph substitutions.

Currently available options:

- Remove nested refs: Tell fontmake to decompose nested references into simple
  ones. Nested references are known to cause problems in certain environments.
- Add 'aalt' feature: Calculate and output 'aalt' feature to UFO.

> [!TIP]
> To generate web font (instead of TTF), specify output file name ending
> with '.woff2'; in this case the plugin calls ``woff2_compress`` after
> generating TTF.

> [!IMPORTANT]
> If the font family has both roman (non-italic) and italic styles, you
> have to specify 2 output files. This is because roman and italic files
> are usually incompatible since they are designed separately.

> [!IMPORTANT]
> You need all masters open before you use this menu item. Also, make
> sure the family name is consistent among the masters, or such masters
> will be ignored.

> [!NOTE]
> This item will not be active if active font does not have VF data.

#### Design axes

Shows a dialog where you can set design axes.

> [!NOTE]
> If there is already non-``dict`` value in ``font.persistent``, warns that
> that data will be lost.

##### This master

This section is needed for all masters.

For active font as one of VF masters, sets position in each design
axis of VF master. Leave unset for unused axes. Registered axes can
use default values which refers font properties.

* Italic: default value is whether ``font.italicangle`` is negative.
  This axis is boolean: you choose the master is for italic or not.
  Seldom used together with slant axis.
* Optical size: can default to ``font.design_size``. Set in points.
  Must be positive.
* Slant: can default to ``font.italicangle``. 0 if upright, negative
  if oblique. This value is hardly positive (left-slanted.)
* Width: can default using ``font.os2_width``. 100 if normal width,
  less if condensed, greater if expanded. Must be positive.
* Weight: can default to ``font.os2_weight``. 400 if regular weight,
  700 if bold. The minimum is 1 (hairline thin) and the maximum is
  999 (extreme bold.)
* Custom axes: there is a room for 3 user-defined axes. No default
  values.

> [!TIP]
> You can find an example of custom axes at [Google Fonts][1] site, and they
> are explained at the [glossary](https://fonts.google.com/knowledge/glossary).

[1]: https://fonts.google.com/?categoryFilters=Technology:%2FTechnology%2FVariable

> [!NOTE]
> 'Italic' axis is exceptionally treated. Unlike other axes, it cannot be
> interpolated (anything like "semi-italic" will never be available.)
> Roman and italic styles will be exported separately, hence you do not have
> to match numbers of points or of contours between them.

> [!IMPORTANT]
> Custom axes will not be treated like italic axis. If you want custom
> discrete axes, you must open only those masters which have the same
> positions on such axes at once. For example,
> [wonky axis](https://fonts.google.com/knowledge/glossary/wonky_axis)
> allows only 0 (off) or 1 (on;) you must open masters with WONK=0 and
> generate WONK=0 VF first, close all masters and then open WONK=1 masters
> and generate VF.

##### Custom axes

This section is needed for default master (choose one master as
default.)

Sets the tag for each custom axis. A tag must be up to 4-letter
alphanumeric. No known axis tags use less than 4 letters; if it
happens, pad with trailing space. Leave them blank if not used.

> [!NOTE]
> You must set a tag before a custom axis can be used.

> [!NOTE]
> Axis tags with less than 4 letters are not tested.

> [!CAUTION]
> Do not set tags which is duplicate or same as predefined ones, or
> undefined behavior occurs.

##### Axis order

This section is needed for default master (choose one master as
default.)

Sets the order of design axes.

##### Axis map

This section is needed for default master (choose one master as
default.)

Maps user position to design position.

Input must be comma-separated values and even number of elements.
Each pair consists of user and design positions in this order.

##### Axis name

This section is needed for default master (choose one master as
default.)

Names the design axes. For predefined axes can use default name.
Custom axes must be named if used.

* Axis name: name of axis itself.
* Labels: comma-separated list which consists of multiple of 4 of
  elements. Leading and trailing spaces will be trimmed. Every
  group of 4 elements:
  * Axis value
  * Flags
    * 0: Neither
    * 1: ``OLDER_SIBLING_FONT_ATTRIBUTE``
    * 2: ``ELIDABLE_AXIS_VALUE_NAME``
    * 3: Both
  * Linked value if exist
  * Name

##### Localized names

This section is needed for default master (choose one master as
default.)

Design axes can have translated names. Each page for each language.
Set language code before you use. Choose a language from the list.

By default there is a room for 8 languages, but this will be
extended if already more than 4 languages are defined.

* Axis name: name of axis itself.
* Labels: comma-separated list which consists of even number of
  elements. Leading and trailing spaces will be trimmed. Every
  pair of elements:
  * Axis value
  * Name

> [!CAUTION]
> Do not select the same language more than once, or undefined behavior will
> occur.

#### Instance list

Shows a dialog where you can set named instances.
Instance list is needed for default master (choose one master as
default.)

> [!NOTE]
> If there is already non-``dict`` value in ``font.persistent``, warns that
> that data will be lost.

##### Instance

At these pages you can set PostScript name, subfamily name, and
associated design positions on each axis.

By default the pages are named 'Instance 1' and so on, but will be
same as subfamily name if already set.

By default there is a room for 8 instances, but this will be
extended if already more than 4 instances are defined.

##### Localized names

Instances can have translated names. Each page (or group or pages)
for each language. Choose a language from the list first. If there
are already 13 instances or more, multiple pages for each language.

By default there is a room for 8 languages, but this will be
extended if already more than 4 languages are defined.

> [!CAUTION]
> Do not select the same language more than once, or undefined behavior will
> occur.

#### Delete VF info

Deletes VF data.

> [!WARNING]
> You will see **no** warning.

### Script usage

As a Python module, in addition to `fontforge` module, scripting to export
variable fonts from SFD projects will be possible.

```python
import fontforge
import fontforgeVF

# Open all masters
fontCL = fontforge.open('MyFont-UltraCondensed-ExtraLight.sfd')
fontCB = fontforge.open('MyFont-UltraCondensed-ExtraBold.sfd')
fontXL = fontforge.open('MyFont-UltraExpanded-ExtraLight.sfd')
fontXB = fontforge.open('MyFont-UltraExpanded-ExtraBold.sfd')

# Open an instance from an existing variable font
font1 = fontforgeVF.openVariableFont('MyFont[wdth,wght].ttf', {'wdth': 100, 'wght': 400})  # by parameters
font2 = fontforgeVF.openVariableFont('MyFont[wdth,wght].ttf', 'Regular')  # named instance
font3 = fontforgeVF.openVariableFont('MyFont[wdth,wght].ttf', 2)  # list index (instances are listed in 'fvar' table)

# Set VF-specific metadata
fontforgeVF.initPersistentDict(fontCL)
fontforgeVF.setVFValue(fontCL, "axes.wght.active", True)
fontforgeVF.setVFValue(fontCL, "axes.wght.useDefault", False)
fontforgeVF.setVFValue(fontCL, "axes.wght.value", 200)
fontforgeVF.setVFValue(fontCL, "axes.wdth.active", True)
fontforgeVF.setVFValue(fontCL, "axes.wdth.useDefault", False)
fontforgeVF.setVFValue(fontCL, "axes.wdth.value", 50)
fontforgeVF.setVFValue(fontCL, "axes.ital.active", True)
fontforgeVF.setVFValue(fontCL, "axes.ital.useDefault", False)
fontforgeVF.setVFValue(fontCL, "axes.ital.value", False)

fontforgeVF.initPersistentDict(fontCB)
fontforgeVF.setVFValue(fontCB, "axes.wght.active", True)
fontforgeVF.setVFValue(fontCB, "axes.wght.useDefault", True)
fontforgeVF.setVFValue(fontCB, "axes.wdth.active", True)
fontforgeVF.setVFValue(fontCB, "axes.wdth.useDefault", True)
fontforgeVF.setVFValue(fontCB, "axes.ital.active", True)
fontforgeVF.setVFValue(fontCB, "axes.ital.useDefault", True)

fontforgeVF.initPersistentDict(fontXL)
fontforgeVF.setVFValue(fontXL, "axes.wght.active", True)
fontforgeVF.setVFValue(fontXL, "axes.wght.useDefault", True)
fontforgeVF.setVFValue(fontXL, "axes.wdth.active", True)
fontforgeVF.setVFValue(fontXL, "axes.wdth.useDefault", True)
fontforgeVF.setVFValue(fontXL, "axes.ital.active", True)
fontforgeVF.setVFValue(fontXL, "axes.ital.useDefault", True)

fontforgeVF.initPersistentDict(fontXB)
fontforgeVF.setVFValue(fontXB, "axes.wght.active", True)
fontforgeVF.setVFValue(fontXB, "axes.wght.useDefault", False)
fontforgeVF.setVFValue(fontXB, "axes.wght.value", 800)
fontforgeVF.setVFValue(fontXB, "axes.wdth.active", True)
fontforgeVF.setVFValue(fontXB, "axes.wdth.useDefault", False)
fontforgeVF.setVFValue(fontXB, "axes.wdth.value", 200)
fontforgeVF.setVFValue(fontXB, "axes.ital.active", True)
fontforgeVF.setVFValue(fontXB, "axes.ital.useDefault", False)
fontforgeVF.setVFValue(fontXB, "axes.ital.value", False)

# Font-family-wide metadata
# Here assume fontCL as the default font
fontforgeVF.setVFValue(fontCL, "axes.wght.name", "Weight")
fontforgeVF.setVFValue(fontCL, "axes.wght.order", 1)
fontforgeVF.setVFValue(fontCL, "axes.wght.localNames.0x407", "Strichstärke")
fontforgeVF.setVFValue(fontCL, "axes.wdth.map", [(200, 200), (400, 350), (800, 800)])
fontforgeVF.setVFValue(fontCL, "axes.wdth.name", "Width")
fontforgeVF.setVFValue(fontCL, "axes.wdth.order", 0)
fontforgeVF.setVFValue(fontCL, "axes.wdth.map[0]", (50, 50))
fontforgeVF.setVFValue(fontCL, "axes.wdth.map[1]", (200, 200))
fontforgeVF.setVFValue(fontCL, "axes.wdth.localNames.0x407", "Laufweite")  # 0x407 stands for German (Germany)
fontforgeVF.setVFValue(fontCL, "axes.ital.name", "Italic")
fontforgeVF.setVFValue(fontCL, "axes.ital.order", 2)
fontforgeVF.setVFValue(fontCL, "axes.ital.localNames.0x407", "Kursiv")

fontforgeVF.setVFValue(fontCL, "axes.wght.labels.200.name", "Extra Light")
fontforgeVF.setVFValue(fontCL, "axes.wght.labels.300.name", "Light")
fontforgeVF.setVFValue(fontCL, "axes.wght.labels.400.name", "Regular")
fontforgeVF.setVFValue(fontCL, "axes.wght.labels.400.olderSibling", False)
fontforgeVF.setVFValue(fontCL, "axes.wght.labels.400.elidable", True)
fontforgeVF.setVFValue(fontCL, "axes.wght.labels.400.linkedValue", 700)
fontforgeVF.setVFValue(fontCL, "axes.wght.labels.500.name", "Medium")
fontforgeVF.setVFValue(fontCL, "axes.wght.labels.600.name", "Semibold")
fontforgeVF.setVFValue(fontCL, "axes.wght.labels.700.name", "Bold")
fontforgeVF.setVFValue(fontCL, "axes.wght.labels.800.name", "Extra Bold")

fontforgeVF.setVFValue(fontCL, "axes.wght.labels.200.localNames.0x407", "Extramager")
fontforgeVF.setVFValue(fontCL, "axes.wght.labels.300.localNames.0x407", "Mager")
fontforgeVF.setVFValue(fontCL, "axes.wght.labels.400.localNames.0x407", "Standard")
fontforgeVF.setVFValue(fontCL, "axes.wght.labels.500.localNames.0x407", "Mittel")
fontforgeVF.setVFValue(fontCL, "axes.wght.labels.600.localNames.0x407", "Halbfett")
fontforgeVF.setVFValue(fontCL, "axes.wght.labels.700.localNames.0x407", "Fett")
fontforgeVF.setVFValue(fontCL, "axes.wght.labels.800.localNames.0x407", "Extrafett")

# User-defined axes (custom1 to custom3)
fontforgeVF.setVFValue(fontCL, "axes.custom1.active", True)
fontforgeVF.setVFValue(fontCL, "axes.custom1.value", 15)
fontforgeVF.setVFValue(fontCL, "axes.custom1.tag", "abc")  # needed for custom axes; will be padded with space
fontforgeVF.setVFValue(fontCL, "axes.custom1.name", "User-defined axis")
fontforgeVF.setVFValue(fontCL, "axes.custom1.order", 3)
fontforgeVF.setVFValue(fontCL, "axes.custom1.localNames.0x407", "Benutzerdefinierte Achse")

# Instances
fontforgeVF.setVFValue(fontCL, "instances[0].psName", "MyFont-ExtraLight")
fontforgeVF.setVFValue(fontCL, "instances[0].name", "ExtraLight")
fontforgeVF.setVFValue(fontCL, "instances[0].wght", 200)
fontforgeVF.setVFValue(fontCL, "instances[0].wdth", 100)
fontforgeVF.setVFValue(fontCL, "instances[0].ital", False)
fontforgeVF.setVFValue(fontCL, "instances[0].localNames.0x407", "Extramager")

# Export TTF
fontforgeVF.export(fontCL, 'MyFont.ttf')

# Export Webfont
fontforgeVF.export(fontCL, 'MyFont.woff2')

# In case you want to drop the VF info
fontforgeVF.deleteVFInfo(fontCL)
```

#### Some example of language codes

| Code   | Language                     |
|-------:|:-----------------------------|
| 0x401  | Arabic (Saudi Arabia)        |
| 0xc01  | Arabic (Egypt)               |
| 0x403  | Catalan                      |
| 0x404  | Chinese (Taiwan)             |
| 0x804  | Chinese (Mainland)           |
| 0xc04  | Chinese (Hong Kong)          |
| 0x407  | German (Germany)             |
| 0x807  | German (Switzerland)         |
| 0x408  | Greek                        |
| 0x409  | English (US) (default)       |
| 0x809  | English (UK)                 |
| 0xc09  | English (Australia)          |
| 0x1009 | English (Canada)             |
| 0x1409 | English (New Zealand)        |
| 0x80a  | Spanish (Mexico)             |
| 0xc0a  | Spanish (Spain, modern sort) |
| 0x40c  | French (France)              |
| 0x80c  | French (Belgium)             |
| 0xc0c  | French (Canada)              |
| 0x100c | French (Switzerland)         |
| 0x40d  | Hebrew                       |
| 0x410  | Italian (Italy)              |
| 0x810  | Italian (Switzerland)        |
| 0x411  | Japanese                     |
| 0x412  | Korean                       |
| 0x413  | Dutch                        |
| 0x813  | Flemish                      |
| 0x416  | Portuguese (Brazil)          |
| 0x816  | Portuguese (Portugal)        |
| 0x417  | Romansh                      |
| 0x419  | Russian                      |
| 0x420  | Urdu                         |
| 0x439  | Hindi                        |

> [!NOTE]
> Language code 0x409 (American English) is used as default and specially treated. You do not have to use it for ``localName``.
