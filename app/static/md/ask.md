`ask` is one of the foundational primitives in NetLogo. It allows us to *ask* one or more agents (i.e., turtles, links, patches) to follow a provided set of rules. When `ask` is used with more than one agents, each agent will take its turn in a random order. 



For example, the following code would make all the turtles in a model to move forward one unit and all the patches in a model pink.

```
ask turtles [ fd 1 ] 
ask patches [ set pcolor pink ]
```



We can also provide more than one command with an `ask` primitive. For example, the following code would make all the turtles put their `pen-down`, and then turn right by ten degrees and go forward one unit 36 times, which would draw a circle.

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
* You can use `ask` with `turtles`, `links`, and `patches`. 
* If you write a code outside an ask statement, NetLogo will try to ask the `observer` to run the code but you cannot write a code such as `ask observer [...]`. 
* Note that each NetLogo primitive has a *scope*. If you use a primitive within an incompatible ask statement, NetLogo will show an error.  A primitive can be observer-only (e.g.,`create-turtles`, `diffuse`), turtle-only (e.g., `forward`, `hatch`), patch-only (e.g., `sprout`, `max-pxcolor`) or link-only (e.g., `tie`, `thickness`). On the other hand, some primitives can be used within multiple scopes (e.g., `pcolor`, `neighbors`) and the utility primitives are scope-independent (e.g., `mean`, `with`).



In the model below, we want the fish to swim around randomly and the stars to just rotate, and we want all the turtles (fish + stars) to grow little by little. To make them follow these actions, we just use the `ask` primitive !