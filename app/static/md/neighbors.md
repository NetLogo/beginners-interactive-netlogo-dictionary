`neighbors` reports an agentset that contains the eight patches that surround an agent's current patch in the north, northeast, east, southeast, south, southwest, west, and northwest directions. Both turtles and patches are allowed to use this reporter. For example, if we wanted to create a model in which a fire spread from one patch to its neighbors, we would werite the following code: 



```
ask patches [
	if pcolor = red [
		ask neighbors [
			if pcolor = green [
				set pcolor red
			]
		]
	]
]
```



Things to keep in mind when using `neighbors`:

* `neighbors` will always report patches even if we use it within an `ask turtles` context. If you would like an agent to see neighboring turtles, you can use `turtles-on neighbors`.
* There is also a `neighbors4` primitive that reports only the four neighboring patches in cardinal directions (east, west, north, and south).
* Be mindful of *world-wrapping* when using `neighbors` as a patch at the edge of the world will report the patch on the other end of the model as its neighbor. If you turned off *world-wrapping*, then a patch will report only three patches if it is on the corner or five patches if it is at the edge.



In the model example below, we have gren patches that represent vegetation and some brown bugs that eat this vegetation. You can see this as bugs on a leaf. At each tick, our bugs eat a little bit of the patch that they are on. If a bug finishes all the grass on one patch, it moves to a neighboring patch and continues eating.

