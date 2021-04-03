`neighbors` reports an agentset that contains the four patches that surround an agent's current patch in the north, east, west, and south directions. Both turtles and patches are allowed to use this reporter. For example, if we wanted to create a model in which a fire spread from one patch to its neighbors, we would werite the following code: 



```
ask patches [
	if pcolor = red [
		ask neighbors4 [
			if pcolor = green [
				set pcolor red
			]
		]
	]
]
```



Things to keep in mind when using `neighbors4`:

* `neighbors4` will always report patches even if we use it within an `ask turtles` context. If you would like an agent to see neighboring turtles, you can use `turtles-on neighbors4`.
* There is also a `neighbors` primitive that reports all eight neighboring patches.
* Be mindful of *world-wrapping* when using `neighbors4` as a patch at the edge of the world will report the patch on the other end of the model as its neighbor. If you turned off *world-wrapping*, then a patch will report only either two patches if it is on the corner or three patches if it is at the edge.



In the model example below, there is a fire spreading in a forest. A patch on fire will spread to its neighboring patches in cardinal directions that contain trees. If a fire patch has brown neighboring patches that indicate ground, it will turn the ground patches gray to indicate the edge of the forest fire.