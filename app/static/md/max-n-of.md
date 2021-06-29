`max-n-of` reports an agentset that contains a specified number of agents with the highest value of a given reporter. For example, if we wanted to create a model where the largest 5 turtles are divided in half, we would write the code below:

```
ask max-n-of 5 turtles [size] [
	set size (size / 2)
	hatch 1
]
```



Things to keep in mind when using `max-n-of`: 

* There is also a `min-n-of` primitive that reports an agentset that contains a specified number of agents with the lowest value of a given reporter.
* If there are less than the specified number of turtles in a given agentset, `max-n-of` will report the entire agentset. For example, if we have only 2 turtles in a model, `max-n-of 5 turtles [ size ]` would report all 2 turtles. 
* When turtles are sorted based on their characteristics, ties are broken randomly. 



In the model example below, we have some people who represent an absurdly simple economy. At each tick, a randomly picked turtle executes a trade by picking another turtle randomly and giving that turtle 5 of its money. This exchange is represented with a temporary link between the two turtles. We use `max-n-of` to change the richest three turtles' color to blue. We also use `min-n-of` to change the poorest 3 turtles' color to red.

