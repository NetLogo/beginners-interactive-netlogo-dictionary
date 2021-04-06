`right` is primitive that tells a turtle to turn certain number of degrees (between 0 and 360) to the right. 



```
ask turtles [
	right 90
]
```



Things to keep in mind when using `right`: 

* Turtle(s) will turn left if you provide a negative number.
* You can also provide a floating point number such as `right 30.5` or `right -185.3`.



The model example below demonstrates how the `right`, and its sibling `left`, primitives work. We have 12 dots representing the 12 hours on the clock and an arrow representing the hour. When we click `spin-right`, our arrow turns right 1 degree at each tick until it completes the specified number of degrees on the slider.

