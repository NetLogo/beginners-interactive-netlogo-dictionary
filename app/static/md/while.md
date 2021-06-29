`while` begins repeating a provided set of rules (like `ask`) indefinitely as long as a given reporter reports true. If the reporter reports **false** , `while` stops repeating the provided rules.  For example, if we wanted to create a model of a real-estate market where each buyer continued searching for a house until they found one cheap enough, we would write the following code: 



```
ask turtles [
	let found-home? false
	while [not found-home?] [
		move-to one-of patches with [residents = 0]
		if [price] of patch-here < my-budget [
			set found-home? true
		]
	]
]
```



In the model example below, we have many turtles placed in a grid layout. Each turtle is either purple or green and each is either happy or sad depending on the number of turtles around them. If a turtle has more than 2 neighbors with a different color, we use the `while` primitive to make each turtle move around the grid until they find a spot that makes them happy.

