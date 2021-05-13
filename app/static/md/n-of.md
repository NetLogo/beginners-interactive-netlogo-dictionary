`n-of` is used when we want to randomly select a specific number of elements out of an agent set. It is similar to how `one-of` works. For example, if we wanted to create a model in which we wanted to have 90 yellow birds and 10 red birds, we would write the following code instead of using `create-turtles` twice:



```
create-turtles 100 [
	set shape "bird"
	set color yellow
	setxy random-xcor random-ycor
]
ask n-of 10 turtles [
	set color red
]
```



Things to keep in mind when using `n-of`:

* If an agentset has less than the provided number of agents, NetLogo will show an error. For example, if we had 5 turtles in a model, the following code would give an error: `ask n-of 10 turtles [move]`.



In the model example below, we use `n-of` to pick 50 random patches to `sprout` 50 plants. We also create 5 cows to graze in this grassland. We also use `n-of` to make two of our cows violet.