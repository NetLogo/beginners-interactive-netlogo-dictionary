`Pen-down` (shortened to `pd`) is used to trace the movements of turtles. The color of the pen is the same as the color of the turtle. While `pen-down` starts tracing, `pen-up` (shortened to `pu`) stops tracing a turtle’s movement. Think of `pen-up` and `pen-down` like a pen on the belly of a turtle; `pen-down` lowers the pen to the ground, leaving a mark of its path, while `pen-up` pulls the pen up, no longer marking the ground. `Pen-down` and `pen-up` are primitives used only with turtles. For example, `ask turtles [ pen-down]` would start drawing lines from the turtles’ movement, and `ask turtles [ pen-up]` would no longer trace the movement. (`Pen-down`, `pen-up`, and `pen-erase` are all equivalent to setting the turtle’s `pen-mode` to `down`, `up`, or `erase`) 

The following code would make turtles draw squares and then move to a random location without leaving a trace:

```	
ask turtles [
   		pen-down
		repeat 4 [ forward 10 right 90 ]
		pen-up 
		setxy random-xcor random-ycor
]
```

`Pen-erase` (shortened to `pe`) erases any previously drawn lines when the turtle passes over them. Think of it as an eraser on the belly of the turtle. 



In the model below, an airplane is flying around. Depending on the procedure selected, the airplane will simply fly around (using `pen-up`), fly around while leaving a trail (using `pen-down`), or fly around while erasing past lines (using `pen-erase`). 