`random` is a primitive that allows us to add randomness into our models. When we provide a number to `random` , it will report a random number from 0 to N-1. Imagine that each time you run the primitive  `random N`, you are rolling a die with N number of sides. For example, if we wanted to create a forest fire in which we assigned each patch to be either a tree (`pcolor = green`) or ground (`pcolor = brown`) but with 70 percent tree density, we would write the following code:



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

* Always remember that `random` will give us numbers within the range from 0 to N - 1, instead of 1 to N. For example, if we run `random 3`, we may get 0, 1, or 2, but not 0. 
* If you want to generate a random number between a custom range, you can use the following format: `minnumber + (random (maxnumber - minnumber))`. For example, if we wanted to generate a random floating point number between 4 and 7, we could write the following code: `4 + random 3`.
* `random` only generates positive integer numbers. If you need to generate floating point numbers, you should use `random-float`.
* The algorithm of `random` generates a uniform distribution. For example, everytime we run `random 5`, there is an equal likelihood of getting 0, 1, 2, 3, or 4. If you would like to generate random numbers over a *normal distribution*, you should use `random-normal`. 



In the model example below, we have 6 turtles that represent 6 dices. Every time we click the **roll dice** button, each turtle picks a random number between 1 to 6 (including 6) and updates its shape accordingly. 

