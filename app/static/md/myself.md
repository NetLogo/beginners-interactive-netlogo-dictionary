`myself` is a primitive that is useful when we want an agent to refer itself while trying to address a different agent or agentset within an `ask` command or a reporter (e.g., `of`, `with`). For example, if we wanted to create a model within which turtles with the same color tried to find each other, we would write the following code:

 

```
ask turtles [
	face one-of turtles with [color = [color] of myself]
	forward 1
]
```



In the model example below, we have a model that is similar to the popular online game [*agar.io*](https://en.wikipedia.org/wiki/Agar.io). We have many turtles that represent circles and they move around randomly. When two turtles touch each other, the larger turtle *eats* the small turtle. We use `myself` for two purposes: first to compare the two touching turtles within an `ask` statement in order to pick the larger one, and then to add the sizes of the two touching turtles.