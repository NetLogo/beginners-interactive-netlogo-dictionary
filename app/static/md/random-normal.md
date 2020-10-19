`Random-normal` is similar to the primitive `random`, in that it randomly generates and reports a number. However, `random` and `random-normal` differ in the distribution that they generate. `Random` will produce a **uniform distribution**, which means every number has an equal chance of being generated, and there will be roughly the same amount of every number. So in `random 4`, 0, 1, 2, and 3 are all equally likely to be generated, and after many repetitions of `random 4`, there will be an equal number of 0’s, 1’s, 2’s, and 3’s. 

But `random-normal` will produce a **normal distribution**, which looks like a bell curve with many values in the middle, and fewer values on the lower and upper tails. Its syntax is :



``` random-normal mean standard-deviation ```



Normal distributions are found more often in nature than uniform distributions, and can add accuracy to your model.  So `random-normal 5 1` would represent a normal distribution with a mean of 5 and a standard deviation of 1; numbers close to 5 are much more likely to be generated than 3 or 7, which are two standard deviations away from the mean. 



In the model below, we are modeling the heights of 100 random people. Because in real life height is normally distributed, we want more people to be the average height than very tall or very short. Looking at the histogram, you can see the difference between a uniform distribution of height and a normal distribution.