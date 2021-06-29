Turtles are mobile agents in NetLogo that can be placed anywhere in the world, can look like anything (e.g., shape, color, size), and can move around. They are the primary type of agents in NetLogo models. 



The `turtle` primitive reports a specific turtle with the given number. For example, if we wanted to create a model with just two turtles, one a cat and the other a mouse, we could write the following code. Notice that when we create turtles, the numbering starts with zero.



```
create-turtles 2
ask turtle 0 [
	set shape "cat"
]
ask turtle 1 [
	set shape "mouse"
]
```

 

The `turtles` primitive reports all the patches in the model. This primitive is helpful in asking all the turtles to do the same things (e.g., move around, change shape) or narrow down a subset of turtles using it in conjunction with the `with` primitive. For example, if we wanted to create a forest fire model with some green turtles representing healthy trees and some yellow turtles representing dead/dry trees, and wanted to start a fire from a dry tree, we would write the following code:



```
create turtles 100 [
	set shape "tree"
	setxy random-xcor random-ycor
	set color one-of [green yellow]
]
ask one-of turtles with [color = yellow][
	set color red
]
```



Things to keep in mind when using `turtle` and `turtles`:

* The primitive `turtles` will always report the same agentset (unless a turtle died), but the order of the turtles will be random each time we use it.
* Turtles have some default characteristics that can be a different value for each turtle. Some of the characteristics come prebuilt (e.g., `color`, `xcor`,`ycor`,`label`, `size`, `heading`), but we can also define custom characteristics with the `turtles-own` primitive such as `turtles-own [minerals water]`.
* We can also create custom turtle breeds using the `breed` primitive such as `breed [trees tree]`.



In the model example below, we have a number of turtles and each turtle represents a different agent. We have a large turtle that represents a house, some green turtles that represent plants, some colorful turtles that represent dogs, some turtles that represent people, and some turtles on the top that represent clouds. The house and the plants remain stationary, while the people, the dogs, and the clouds move. On the other hand, the plants grow little by little at each tick. 