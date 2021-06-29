`sort-on` allows us to sort the agents in an agentset based on a reporter such as an agent characteristic (e.g.,`size`, `xcor`) or custom agent variable (e.g., `age`, `speed`). Its syntax is: ` sort-on [ variable-or-reporter ] agentset `. For example, if we wanted to create a model of earthquake search-and-rescue in which the rescuers checked the largest buildings first, we would write the following code:



```
let buildings-sorted sort-on [size] buildings
ask rescuers [
	move-to last buildings-sorted
]
```



Things to keep in mind when using `sort-on`:

* `sort-on` will always sort in ascending order, so if you want the results in descending order, you can pass the output into `reverse` such as `reverse sort-on [size] turtles`. 
* Although we used a simple agent characteristic in the example above, the reporter can include more advanced reporters. For example, if we wanted to sort turtles based on how close their x-coordinate was to 0, we could use `sort on [abs xcor] turtles` which would get the absolute value of the xcor before passing into the sorting algorithm. 
* The output of `sort-on` will always be a newly created list -- it will not modify the original agentset at all. 