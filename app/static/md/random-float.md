`random-float` is a primitive that reports a random float number anywhere between 0 and the given number, both whole numbers and decimals. For instance, `random-float 10` could report 6.9105, 7, 4.2, 0.451, 0.0000001, 9.99999, etc. (See `random` for finding a random whole number.)

In the common case where you want to get a random value that is somewhere in between the minimum and maximum x or y coordinates, you can use the procedures `random-xcor` and `random-ycor`, which also report back non-integer values. 

**Note:** because `random-float` will return a number between 0 and (n-1), `random-float 5.0` could report  `0.0`, but it could never report  `5.0`. 



In this model, `random-float` is used to randomly place a dart somewhere on (or off of) a dartboard. By using `random-float`, we are ensuring that the dart could land at every possible point on the dart board, not just integer points like `random` would produce. 