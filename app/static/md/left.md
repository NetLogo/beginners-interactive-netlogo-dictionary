`left` is primitive that tells a turtle to turn certain number of degrees (between 0 and 360) to the left. 



```
ask turtles [
	left 90
]
```



Things to keep in mind when using `left`: 

* Turtle(s) will turn right if you provide a negative number.
* You can also provide a floating point number such as `left 30.5` or `left -185.3`.



The model example below demonstrates how the `left`, and its sibling `right`, primitives work. We have 12 dots representing the 12 hours on the clock and an arrow representing the hour. When we click `spin-left`, our arrow turns left 1 degree at each tick until it completes the specified number of degrees on the slider.

