`ask` is one of the foundational primitives in NetLogo. It allows us to *ask* one or more agents (i.e., turtles, links, patches) to follow a provided set of rules. When `ask` is used with more than one agents, each agent will take its turn in a random order. 



For example, the following code would make all the turtles in a model to move forward one unit and all the patches in a model pink.

```
ask turtles [ fd 1 ] 
ask patches [ set pcolor pink ]
```



You can also provide more than one commands with an `ask` primitive. For example, the following code would make all the turtles put their `pen-down`, and then turn right by ten degrees and go forward one unit 36 times, which would draw a circle.

```
ask turtles [
	pen-down
	repeat 36 [
	   right 10
	   forward 1
	]
]
```



Things to keep in mind when using `ask`: 

* You can use the `ask  ` primitive with the custom turtle types that you define with the `breed` primitive. 
* You can ask individual turtles to follow a set of rules using the form `turtle n`, such as `ask turtle 1 [...]`, `ask turtle 2 [...]`
* You can ask individual patches to follow a set of rules using the form `patch x y`, such as `patch 3 0 [...]`.
* You can use the `with` primitive to ask an even smaller subset of given agents such as `ask turtles with [color = red][ ... ]` or `ask patches with [pxcor = 5][ ... ]`.



<br />

In the model below, we want the fish to swim around randomly and the stars to just rotate, and we want all the turtles (fish + stars) to grow little by little. To make them follow these actions, we just use the `ask` primitive !