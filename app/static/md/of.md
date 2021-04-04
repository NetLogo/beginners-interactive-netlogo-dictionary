`of` is a primitive that allows us to reach into an agent and pull out the value of a variable it owns. Normally, agent variables (such as `color`, `size`, `shape`, as well as variables defined with `<agents>-own` commands) are accessed within an agent context using the `ask` primitive. `of` allows us to get to those variables outside of such a block or to get all the values for each agent in an agentset all at once as a list. For example, if we wanted to create model where each person picked a random friend and gave them an apple if they didn't already have one, we would write the following code: 



```
ask people [
	let my-friend one-of other people
	if [apple] of my-friend = 0 [
		ask my-friend [ set apple apple + 1 ]
	]
]
```



Things to keep in mind when using `of`:

* `of` is very useful to query agent characteristics such as finding the average size of turtles (`mean [size] of turtles`), the largest turtle size (`max [size] of turtles`), etc.
* `of` is also very useful in creating monitors or plots in the interface. Often times, we will need to present some sort of a summary value such as the average wealth of turtles (`mean [wealth] of turtles`) or 
* You can also do some simple operations within a reporter that comes before `of` such as `[checking-account + savings-account] of customers` to get the total money in customers' accounts or `[size / 2] of circles` to automatically calculate the radius of circles in a model.
* If we use `of` with agentsets (and without primitives such as `mean`), it will report a list. For example, if we have 3 turtles in a model, `[size] of turtles` would report `[1 1 1]`.



In the model example below, we have a model that is similar to the popular online game [*agar.io*](https://en.wikipedia.org/wiki/Agar.io). We have many turtles that represent circles and they move around randomly. When two turtles touch each other, the larger turtle *eats* the small turtle. We use `of` to compare the two touching turtles within an `ask` statement in order to pick the larger one and then to add the sizes of the two touching turtles.