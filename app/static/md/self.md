

`self` is a primitive that is useful when there is a single `ask` command, and the turtle, link, or patch is trying to refer to themselves. For example, 

```
let my-turtle nobody 
create-turtles 1 [ 
	set shape “turtle” 
	set my-turtle self
] 
ask my-turtle [ forward 2]
```

would set the variable `my-turtle` to be the newly created turtle.  It is rarely used, because  `[color] of self` is equivalent to just saying `color`. 

