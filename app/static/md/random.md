`random` is a primitive that allows us to add randomness into our models. When we provide a number to `random`, it will report a random number from 0 to N-1. Imagine that each time you run the primitive  `random N`, you are rolling a die with N number of sides. For example, if we wanted to create a forest fire in which we assigned each patch to be either a tree (`pcolor = green`) or ground (`pcolor = brown`) but with 70 percent tree density, we would write the following code:



```
ask patches [
	ifelse random 100 < 70 [
		set pcolor green
	][
		set pcolor brown
	]
]
```





Things to keep in mind when using `random`:

* Always remember that `random` will give us numbers within the range from 0 to N - 1, instead of 1 to N. For example, if we run `random 3`, we may get 0, 1, or 2, *but not 3*.
* If you want to generate a random number from `A` to `B`, you can use the following format: `A + (random (B - A + 1))`. For example, if we wanted to generate a random number between 4 and 6 (that is, we want to get 4, 5, or 6), we could write the following code: `4 + random (6 - 4 + 1)` or just `4 + random 3`.
* `random` only generates positive integer numbers. If you need to generate floating point numbers, you should use `random-float`.
* The algorithm of `random` generates a *uniform distribution*. For example, every time we run `random 5`, there is an equal likelihood of getting 0, 1, 2, 3, or 4. If you would like to generate random numbers over a *normal distribution*, you should use `random-normal`.

In the model example below, we have 6 turtles that represent the 6 faces of a dice. Every time we click the **roll dice** button, each turtle picks a random number between 1 to 6 (including 6) and updates its shape accordingly.

Why do we need to add 1 to value we give to random to get the full range of values?  In math and computer science language, we would say that the `random` primitive produces numbers in the range 0 to N *exclusive*, meaning that the number N itself is *excluded* from the possible set of values.  In order to make it *inclusive* for N we have tell `random` to set the *exclusive* limit at N + 1, which gets N back in the range of possible results.
