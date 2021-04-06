`repeat` allows us to execute any set of commands *n* amount of times back-to-back. `repeat` is especially useful when drawing geometric shapes in conjunction with the `pen-down` and `pen-up` primitives. For example, if we wanted our turtles to draw a square, we would write the following code:



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



In the model example below, we have 36 turtles who are initially placed in a circle layout when the *setup* button is clicked. When we click the go button, each turtle turns right 1 degrees and moves forward 0.03 units 360 times. This simple repetition behavior results in a very interesting shape.