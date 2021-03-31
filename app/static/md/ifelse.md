`ifelse` is used to define two sets of rules to be followed by turtles conditionally: one set if a provided condition is *true* and another set if the condition is *false*. To do so, we use the following format: `ifelse condition(s)[...][...]`.



```
ask cows [
	ifelse thirst > 10 [
		drink-water
	][
		eat-grass
	]
]
```



Things to keep in mind when using `if-else`: 

* You can combine two or more conditional statements using `and` and `or` primitives.
* You can use the `not` primitive to make true statements false, and vice-versa.
* If you need your agents to follow a set of rules only if the provided condition is true, but do nothing otherwise, you should use the `if` primitive. 



The model example has some cars driving down a road and a gas station in the middle. The cars stop at the gas station to top up their tanks before moving on. At each tick, each car checks if it is at the gas station and if its tank is not full (less than 1) (if the patch they are on has an x coordinate of 0). If it is not at the gas station, it keeps moving. If it is at the gas station,it starts filling up its tank until full. Otherwise, it start moving again. Each time a car drives, it loses a little bit of gas, so when it loops back around to the gas station again, it will refill its tank.
