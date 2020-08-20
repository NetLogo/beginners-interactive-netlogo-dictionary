A **reporter** is something that returns a value and, unlike a command, cannot be a stand-alone code element . NetLogo has some useful built-in reporters that cannot be changed directly such as `ticks`, `pi`, `e`, `world-width`, and `world-height`. For example, we cannot just write `ticks` in the code. We need to use ticks in some other algorithm such as: `if ticks > 9 [  wake-up ] ` or `let world-area (world-width * world-height)`. 


Other primitives that we use for filtering agentsets or manipulating lists such as `of`, `with`, `sort-on`, and `word` are reporters, too. 

Many turtle, patch, and link properties such as `color` or `label` can be thought of as both variables that we can change with the `set` command, as well as reporters that provide us with the values of these variables. Notice in the following example that the brackets `[ ]` that come before 

```
if xcor < 0 [ 
If [pycor] of patch-here > 0 [ 
set label “Quadrant II” ] 
]
```

Finally, you can create custom reporters using the `to-report` keyword to begin a reporter procedure and the `report` command at the end of your procedure, right before the `end` keyword. Reporters can be useful to tidy up your code and keep you from repeating lines of code; if you use the same equation or long line of code multiple times, a `to-report` procedure can be used to replace it. 

For example, if you write `ask turtles with [ shape = “person” and color = green and size > 5 ]` many times, you could instead add a reporter procedure like 
```
to-report big-green-people 
report turtles with [ shape = “person” and color = green and size > 5 ]
end
```

and then replace each `turtles with [ shape = “person” and color = green and size > 5 ]` for `big-green-people` in your code, such as `ask big-green-people [ do-things ] `.  Once you have calculated the value you would like to return from the procedure, add the primitive `report` in front of the value.

`to-report` is often used for calculations. For example, if you want to calculate the area of circles many times in your code, you can write 

```
To-report circle-area [ r ]
Report ( pi * ( r  ^ 2 ) )
end
```
Now, whenever you would like to calculate the area of a circle, simply write ` circle-area [ radius ]`.
