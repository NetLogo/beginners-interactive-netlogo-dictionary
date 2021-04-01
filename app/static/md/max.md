`max` reports the maximum value in a given list. For example, `show max [14 -2 7]` would reports 14. `max` is commonly used to find a specific agent within an agentset. For example, if we wanted to create a model of cell division and have the largest cell to divide in half at each tick, we would write the following code:



```
ask cells [
	if size = max [size] of cells [
		set size (size / 2)
		hatch 1
	]
]
```



In the model example below, we have some poeple who represent an absurdly simple economy. At each tick, a randomly picked turtle executes a trade by picking another turtle randomly and giving that turtle 5 of its money. This exchange is represented with a temporary link between the two turtles. We use `max` to change the richest turtle's color to blue. We also use `min` to change the poorest turtle's color to red.