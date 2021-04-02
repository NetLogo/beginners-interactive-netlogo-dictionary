`move-to` allows a turtle to set its x and y coordinates to be the same as another turtle or patch without altering the turtle's other variables (e.g., heading, color, size). For example, if we were working on a model of people moving between houses, where both houses and families were represented with a house, we would write the following code:



```
ask families [
	if my-house != nobody [
		set my-house one-of houses
		move-to my-house
	]
]
```



In the model example below, we have a simple environment. Some of our patches are brown, which represents earth, and some are blue, which represents water. We have some bugs in this environment and they need to only move on the brown patches. First, we use the `move-to` primitive in the *setup* procedure to make each bug be placed on a random brown patch. Second, we use the `move-to` primitive (instead of `forward`) to make sure that our bugs pick a random neighboring brown patch and move to it.

