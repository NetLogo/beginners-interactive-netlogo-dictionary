`self` is a primitive that is useful when we need an agent to refer itself within an `ask` statement. `self` is very useful in assigning one turtle to a global variable. For example, if we had a restaurant patch that all of our customers needed to go to, we would write the following code

```
globals [the-restaurant]
to setup
 	ask one-of patches [
 		set color yellow
 		set the-restaurant self
 	]
end
to go 
	ask turtles [
		facer the-restaurant
		forward 1
	]
end
```



In the model example below, we have a model that is similar to the popular online game [*agar.io*](https://en.wikipedia.org/wiki/Agar.io). We have many turtles that represent circles and they move around randomly. When two turtles touch each other, the larger turtle *eats* the small turtle. We use `self` for two purposes: first to compare the two touching turtles within an `ask` statement in order to pick the larger one, and then to add the sizes of the two touching turtles.