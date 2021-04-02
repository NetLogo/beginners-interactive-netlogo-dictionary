`distance` is a turtle and patch primitive that reports the shortest distance between the current agent and another provided agent. For example, the following code would make the turtles who are close enough to the center patch (0,0) to move one step forward, but if their distance to the center patch (0,0) is 5 units or more, they would not move.



```
ask turtles [
	if distance (patch 0 0) < 5 [ forward 1 ]
]
```



Things to keep in mind when using `distance`: 

* You can only provide a specific agent to the `distance` primitive. For example, if we had a turtle `breed` named `trees`, the following code would show an error `distance trees` even if there are only one trees in our model because the `trees` breed name will always report an agentset. In such a situation where you know that there will only be one of a breed of turtles in the model, you can use the `one-of` primitive: `distance one-of trees`.
* If you need to learn an agent's distance to a certain location, not another agent, you can use the `distancexy` primitive.



In the model example below, we use `distance` to implement a rudimentary path finding behavior for a lumberjack. The lumberjack has a "target" tree that they will try to move towards and cut down. Once they cuts down that tree, they will set their eyes to the closest tree. We use `distance` to get the distance between the lumberjack and all of the trees so that we can figure out which tree is closest. In the case of ties, we choose one of the closest trees randomly.
