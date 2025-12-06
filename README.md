Fontforge Variable Font Plugin
==============================

A FontForge_plugin to create a variable font

As of October 2025, Fontforge supports legacy (maybe obsolete) multiple
master formats but not yet OpenType variable fonts. This plugin adds
frontend of [fontmake](https://pypi.org/project/fontmake/) and
[fonttools](https://pypi.org/project/fonttools/) so that variable fonts can
be created through Fontforge interface.

This module requires Python 3.10 or later.

Install
-------

```shell
pip3 install fontforgeVF
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
  - Open a variable font... (not implemented)
  - Generate a variable font...
  - Design axes...
  - Instance list... (not implemented)
  - Delete VF info

#### Open a variable font

> [!NOTE]
> This item is not yet implemented.

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

Currently available options:

- Remove nested refs: Tell fontmake to decompose nested references into simple
  ones. Nested references are known to cause problems in certain environments.

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

##### Custom axes

This section is needed for default master (choose one master as
default.)

Sets the tag for each custom axis. A tag must be up to 4-letter
alphanumeric. Will be padded with implicit trailing spaces. Leave
them blank if not used.

> [!NOTE]
> You must set a tag before a custom axis can be used.

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
  * Whether label name is elidable (1 if so, 0 if not)
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

#### Instance list

> [!NOTE]
> This item is not yet implemented.

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
fontforgeVF.setVFValue(fontCL, "axes.wght.localNames.de", "Strichstärke")
fontforgeVF.setVFValue(fontCL, "axes.wdth.map", [(200, 200), (400, 350), (800, 800)])
fontforgeVF.setVFValue(fontCL, "axes.wdth.name", "Width")
fontforgeVF.setVFValue(fontCL, "axes.wdth.order", 0)
fontforgeVF.setVFValue(fontCL, "axes.wdth.map", [(50, 50), (200, 200)])
fontforgeVF.setVFValue(fontCL, "axes.wdth.localNames.de", "Laufweite")
fontforgeVF.setVFValue(fontCL, "axes.ital.name", "Italic")
fontforgeVF.setVFValue(fontCL, "axes.ital.order", 2)
fontforgeVF.setVFValue(fontCL, "axes.ital.localNames.de", "Kursiv")

fontforgeVF.setVFValue(fontCL, "axes.wght.label.200.name", "Extra Light")
fontforgeVF.setVFValue(fontCL, "axes.wght.label.300.name", "Light")
fontforgeVF.setVFValue(fontCL, "axes.wght.label.400.name", "Regular")
fontforgeVF.setVFValue(fontCL, "axes.wght.label.400.elidable", True)
fontforgeVF.setVFValue(fontCL, "axes.wght.label.400.linkedValue", 700)
fontforgeVF.setVFValue(fontCL, "axes.wght.label.500.name", "Medium")
fontforgeVF.setVFValue(fontCL, "axes.wght.label.600.name", "Semibold")
fontforgeVF.setVFValue(fontCL, "axes.wght.label.700.name", "Bold")
fontforgeVF.setVFValue(fontCL, "axes.wght.label.800.name", "Extra Bold")

fontforgeVF.setVFValue(fontCL, "axes.wght.label.200.localNames.de", "Extramager")
fontforgeVF.setVFValue(fontCL, "axes.wght.label.300.localNames.de", "Mager")
fontforgeVF.setVFValue(fontCL, "axes.wght.label.400.localNames.de", "Standard")
fontforgeVF.setVFValue(fontCL, "axes.wght.label.500.localNames.de", "Mittel")
fontforgeVF.setVFValue(fontCL, "axes.wght.label.600.localNames.de", "Halbfett")
fontforgeVF.setVFValue(fontCL, "axes.wght.label.700.localNames.de", "Fett")
fontforgeVF.setVFValue(fontCL, "axes.wght.label.800.localNames.de", "Extrafett")

# User-defined axes (custom1 to custom3)
fontforgeVF.setVFValue(fontCL, "axes.custom1.active", True)
fontforgeVF.setVFValue(fontCL, "axes.custom1.value", 15)
fontforgeVF.setVFValue(fontCL, "axes.custom1.tag", "abc")  # needed for custom axes; will be padded with space
fontforgeVF.setVFValue(fontCL, "axes.custom1.name", "User-defined axis")
fontforgeVF.setVFValue(fontCL, "axes.custom1.order", 3)
fontforgeVF.setVFValue(fontCL, "axes.custom1.localNames.de", "Benutzerdefinierte Achse")

# Instances: not implemented

# Export TTF
fontforgeVF.export(fontCL, 'MyFont.ttf')

# In case you want to drop the VF info
fontforgeVF.deleteVFInfo(fontCL)
```
