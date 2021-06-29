`in-radius` is a primitive that reports all the agents within a certain radius of the current agent. For example, a turtle might like to know how many other turtles are within a radius of two units of itself or a patch might like to know how many turtles are within three units of itself. 



```
ask turtles [
	if any? other turtles in-radius 2 [
		create-link-with one-of other turtles in-radius 2
	]
]
```



Things to keep in mind when using `in-radius`: 

* You can also use floating point values for the radius parameter such as `in-radius 3.65`.
* Both *turtles* and *patches* can use `in-radius`.
* Keep in mind that `in-radius` may report the original turtle, too, if you are using the same breeds. Be sure to account for that in your models by using the `other` primitive as shown in the example above.
* You can combine `in-radius` and the `with` primitives to narrow down the target agents but make sure to encapsulate the first `with` statement within parentheses `( )`. For example, you can write a code like `if any? (carrots with [color = orange]) in-radius 2 [ eat ]`.



In the model example below, we have an environment represented with green patches and a factory at the center. When the go button is clicked, the factory pollutes all the patches within a radius of 5, represented by darker green patches.