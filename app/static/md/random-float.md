`random-float` is a mathematics primitive that reports a random floating point number anywhere between 0 and the given number. For instance, `random-float 10` could report 6.9105, 7, 4.2, 0.451, 0.0000001, 9.99999, etc. `random-float` is very useful in modeling phenomena that requires continuous numbers. For example, if we wanted to create a model where we wanted to have people with various heights, we could write the following code, which would make each person have a random height between 5 feet to 7 feet:



```
create-people 100 [
	set size 5 + random-float 2
]
```



Things to keep in mind when using `random-float`:

* If you want to generate a random number between a custom range, you can use the following format: `minnumber + (random-float (maxnumber - minnumber))`. For example, if we wanted to generate a random floating point number between 4 and 7, we would write the following code: `4 + random-float 3`.
* In the common case where you want to get a random value that is somewhere in between the minimum and maximum x or y coordinates, you can use the procedures `random-xcor` and `random-ycor`, which also report back non-integer values. 
* Because `random-float` will return a number between 0 and (n-1), `random-float 5.0` could report  `0.0`, but it could never report  `5.0`. The highest number `random-float` could report is `4.999999....`



In the model example below, we use `random-float` to randomly place a dart somewhere on (or off of) a dartboard. By using `random-float`, we are ensuring that the dart could land at every possible point on the dart board, not just integer points. 