`pn-down` (short version `pd`) is used to trace the movements of turtles. The color of the pen is the same as the color of the turtle. While `pen-down` starts tracing, `pen-up` (short version to `pu`) stops tracing a turtle’s movement. Think of `pen-up` and `pen-down` like a pen on the belly of a turtle; `pen-down` lowers the pen to the ground, leaving a mark of its path, while `pen-up` pulls the pen up, no longer marking the ground. `Pen-down` and `pen-up` are primitives used only with turtles. For example, if we wanted our turtles to draw a square, we would write the following code:



```
ask turtles [
	pen-down
	repeat 4 [
		right 90
		forward 5
	]
	pen-up
]
```



In the model below, an airplane is flying between two mythical destinations: Atlantis and Valhalla. As it is flying, it leaves a trail behind it if the `draw-path?` switch is on. Every time a plane reaches a destination and turns around, it also changes its color, which leads to a new trail color. If the `draw-path?` switch is off, our plane picks up its pen and stops drawing. We also use the `clear-drawing` primitive to clear all the previously drawn paths when the  `draw-path?` switch is off. Notice that `clear-drawing` is an observer-only primitive, so we use it outside the `ask turtles` statement.