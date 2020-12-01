# The First 12 NetLogo Primitives to Learn

&nbsp;

<p class="badge badge-warning">Note to the devs: this page needs to be finished.</p>

When beginning to learn NetLogo, there are some primitives you will use in nearly every model you create. Here is a Beginner’s Guide to the first 9 primitives you should learn.



#### `to` and `end`
`to` and `end` are essential for creating procedures in NetLogo. `to` begins a procedure, and `end` concludes it. All code in the Code Tab must be written within a procedure, or else it will cause an error.  Procedures are used to create  smaller blocks of code that do specific things, and will simplify and break up your code. Simply add all your code within `to procedure-name` and `end`. 





#### `ask`

`ask` is used to make agents and agentsets do things. This is how you accomplish almost all actions in NetLogo; for agents to do any action, you must command them using `ask`.  You can use `ask` on turtles, links, and patches. Within the `[...]` following `ask`, simply define the actions you want the agents to complete.





#### `tick`

``tick` is used to advance the tick-counter in your model. A tick is just a measure of time in NetLogo, like minutes or seconds. `tick` is only necessary when using tick-based updates. When you use `tick`, it increases the tick counter by 1, and updates all the plots and monitors in your model.





#### `if`

`if` is used to conditionally run a command. If you want a portion of code to run only if a certain check passes, you would use `if`. For example, if you want turtles to move **only** if they are standing on a red patch, you could use `if` to say:

```
ask turtles [
	if [ pcolor ] of patch-here = red [
		forward 1
	]
]
```





#### `set`

`set` is used to set the value of a certain variable. A variable is a certain characteristic or value that belongs to an agent or the model. Each variable has a certain value, which can be changed. For example, turtles have the variables `color` whose value could be red, yellow, blue, etc., and  `xcor`, and `ycor` whose values could be any coordinate of the world.  This can be used for any type of variable: turtle variables, patch variables, locally defined and globally defined variables. `set` is used to change the value of a variable.





#### `clear-all`

`clear-all` is used to clear out everything in your model. This is usually used in your `setup` procedure, to start your model off with a clean slate. `clear-all` clears any turtles and links, resets all variables, and sets patches back to black.





#### `and` 

`and`is used to check multiple true-or-false conditions at the same time. `and` will **only** return true if both of the individual conditions are true. `and` is commonly used with `if` to create more complex conditions. For example, if you wanted your turtles to move forward **only** if they are red **and** are bigger than 2, you could say:

```
ask turtles [
	if color = red and size > 2 [
		forward 1
	]
]
```





#### `or`

`or` is used to check if at least one true-or-false condition is met. `or` will return true if at least one of the multiple conditions is true, so it will return true if 1) the first condition is true but the second is false, 2) the first condition is false but the second is true, or 3) both are true. `or` is usually used with `if` to create these conditions. For example, if you wanted turtles to move forward if they are red or if they are bigger than 2, you could say:

```
ask turtles [
	if color = red or size > 2 [
	forward 1
	]
]
```

So now, red turtles would move, large turtles would move, and large red turtles would move.





#### `turtles` and `patches`

`turtles` and `patches` are used to report the agentsets of either `turtles` or `patches`. They are commonly used with `ask` to 	make the turtles or patches do things. So to make all patches or all turtles complete an action, you would say `ask turtles [ commands ]` or `ask patches [ commands ]`. 





#### `create-turtles`

`create-turtles` is how you first make turtles in your models. Turtles are the main agents in most models, moving around and interacting with other turtles or patches. In most models, the emergence is seen in the behavior of turtles, and turtles are very important for NetLogo models.  `create-turtles` is used by the Observer, or not within any `ask [ … ]` block. You can create any number of turtles you would like, and make them complete any action that is defined in the `[ … ]` following `create-turtles`. 

