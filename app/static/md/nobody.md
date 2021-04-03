`nobody` is a special primitive that we use to check whether an agent actually exists. In addition, when a turtle dies, it becomes `nobody`, too. For example, if we wanted to create a model in which each turtle formed a link with another turtle on a neighboring patch, we would write the following code: 



```
ask turtles [
	let my-potential-friend one-of turtles-on neighbors
	if my-potential-friend != nobody [
		create-link-with my-potential-friend
	]
]
```


Things to keep in mind when using `nobody`

*  `nobody` is only used when looking for a single agent. If we need to check whether an agentset is empty, we need to use the `any?` primitive such as `if any? turtles with [color = green]` .



In the model example below. we have a campfire in the middle, 10 tents, and 10 campers. When the go button is clicked, each camper moves around randomly. As long as an agent's `my-tent` variable is set to `nobody`, they keep moving around. In other words, the tents are randomly claimed by the campers.

