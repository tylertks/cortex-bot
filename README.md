# cortex-bot

This is a Discord bot for the Cortex Prime Role Playing Game.

It can roll any number of any sided dice, and will return the result of each die.

Additionally it will calculate the result from the two highest rolls, count the number of spoilers, and tell you the effect die

`$roll 2d6`

Will give the result:

```
RESULTS
--------
d6 : 5
d6 : 4

For a roll of: 9
with an effect die of: d4
```

To roll more than one type of die, separate the die types with any character that isn't whitespace, a number, or the letter 'd'

`$roll 3d8,2d6`

Will give the result:

```
RESULTS
--------
d8 : 6
d8 : 7
d8 : 8
d6 : 5
d6 : 5

For a roll of: 15
with an effect die of: d8
```
