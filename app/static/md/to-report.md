A **reporter** is a predefined procedure that returns a value and, unlike a command, cannot be a stand-alone code element . NetLogo has some useful built-in reporters that cannot be changed directly such as `ticks`, `pi`, `e`, `world-width`, and `world-height`. For example, we cannot just write `ticks` in the code. We need to use ticks in some other algorithm such as: 



```
if ticks > 9 [ 
	wake-up 
]
```



Other primitives that we use for filtering agentsets or manipulating lists such as `of`, `with`, `sort-on`, and `word` are reporters, too. 



Many turtle, patch, and link properties such as `color` or `label` can be thought of as both variables that we can change with the `set` command, as well as reporters that provide us with the values of these variables. Notice in the following example that the brackets `[ ]` that come before `of`:



```
if xcor < 0 [ 
	if [pycor] of patch-here > 0 [ 
		set label “Quadrant II” 
	] 
]
```



Finally, you can create custom reporters using the `to-report` keyword to begin a reporter procedure and the `report` command at the end of your procedure, right before the `end` keyword. Reporters can be useful to tidy up your code and keep you from repeating lines of code; if you use the same equation or long line of code multiple times, a `to-report` procedure can be used to replace it. 



For example, instead of writing `ask turtles with [ shape = “person” and color = green and size > 5 ]` many times, we could define a reporter procedure as follows:

 

```
to-report big-green-people 
	report turtles with [ shape = “person” and color = green and size > 5 ]
end
```



Once we define this variable, we can replace each `turtles with [ shape = “person” and color = green and size > 5 ]`  statement in our code with `big-green-people`, such as `ask big-green-people [ do-things ] `.  



`to-report` is often used for complex calculations. For example, if we wanted to calculate the area of circles many times in our code, we could define the following reporter:



```
to-report circle-area [ r ]
	report ( pi * ( r  ^ 2 ) )
end
```


Now, whenever we would like to calculate the area of a circle, we could simply write ` circle-area radius `.



In the model example below, we have many circles large and small. These circles represent particles within a gas container. Each particle has the same energy. However, each of them has a different speed because a particle's kinetic energy is equal to its mass times the square of its speed divided by two ($E = \frac{1}{2} m v^2$). Instead of writing this complicated code to calculate a particle's speed within the `go` procedure, we define a *speed* reporter. Although we kept the code of this model example deliberately simple, defining this reporter would make a big difference if we had a more complex model where we needed to calculate the speed of a particle in many different parts of our code.