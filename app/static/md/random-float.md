`random-float` is a procedure that reports back a random number anywhere between 0 and the given number, both whole numbers and not. For instance, `random-float 10` could resolve to 6.9105, 4.2, 0.451, 0.0000001, 9.99999, etc.

In the common case where you want to get a random value that is somewhere in between the minimum and maximum x or y coordinates, you can use the built-in procedures `random-xcor` and `random-ycor`, which also report back non-integer values. 

Note that due to the way `random-float` is defined, `random-float 5.0` could, however unlikely, report back `0.0`, but it could never report back `5.0`. 

In this model, `random-float` is used to randomly place a dart somewhere on (or off of) a dartboard. By using `random-float`, we are ensuring that the dart could land at every possible point on the dart board, not just integer points like `random` would produce. 
