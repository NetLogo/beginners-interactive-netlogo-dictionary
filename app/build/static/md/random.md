`random` is a built in procedure to NetLogo that allows you to add randomness into your models. Imagine that each time you run the command  `random N`, you are rolling a die with N number of sides.

The one thing you have to remember when using random is that the numbers you get out of range from 0 to N - 1, instead of 1 to N. For example, if you run `random 3`, you may get 0, 1, or 2. In the example below I add one to the result of `random 6` to Account for this difference between NetLogo's random dice rolls and those of an actual six sided die.
