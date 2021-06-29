`random-normal` is similar to the primitive `random`, in that it randomly generates and reports a number. However, `random` and `random-normal` differ in the distribution that they generate. 



`Random` will produce a **uniform distribution**, which means every number has an equal chance of being generated, and there will be roughly the same amount of every number. So in `random 4`, 0, 1, 2, and 3 are all equally likely to be generated, and after many repetitions of `random 4`, there will be an equal number of 0’s, 1’s, 2’s, and 3’s. 



But `random-normal` will take a *mean* value and a *standard-deviation* value to produce a **normal distribution**, which looks like a bell curve with many values in the middle, and fewer values on the lower and upper tails. Its syntax is as follows: `random-normal mean stdev`.



Normal distributions are found more often in nature than uniform distributions and can add accuracy to your model.  For example, if we wanted to create a model of bug evolution in which each bug had a different sized antenna, but with a normal distribution, we would write the following code:



```
create-bugs 100 [
	set shape "bug"
	set antenna-size random-normal 2.5 0.5
]
```



In the model example below, we are a population of colorful butterflies. At every 50 ticks, each butterfly produces a new baby. A baby butterfly inherits its parent's color but can have a slightly different size. We achieve this natural size difference between the adults and the children by using the `random-normal` primitive. A histogram at the bottom shows the change in the distribution of bug sizes over time. Notice how we get much larger and much smaller bugs after running the model but the average bug size (`mean [size] of turtles`) barely changes.