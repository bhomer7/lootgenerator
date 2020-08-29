# Loot Generator

A small CLI interface for generating loot from loot tables. Designed with
Dungeons and Dragons in mind. Included base tables are from D&D 5e DMG.

# Creating Tables

Loot tables are json following the pattern found in [Example.json](./docs/Example.json).

Masses are in pounds.  
Volumes are in cups.  
Values are in gp.

## Specifying Amounts
Amounts can be specified in 3 ways:
1. A constant
2. A range
3. A dice roll

Ranges follow the syntax `<start>-<end>`. A uniform distribution between the
inclusive endpoints is used to pick a value.

Dice rolls follow the syntax
`[<number of dice>]d<number of sides>[*<multiplier][+<constant>]`.

-------------------------------------------------------------------------------

Allowed under the [Wizards of the Coast fan content policy](https://company.wizards.com/fancontentpolicy)