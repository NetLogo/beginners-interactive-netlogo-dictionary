# The First 9 NetLogo Primitives to Learn

&nbsp;

<p class="badge badge-warning">Note to the devs: this page needs to be finished.</p>

When beginning to learn NetLogo, there are some primitives you will use in nearly every model you create. Here is a Beginner’s Guide to the first 9 primitives you should learn.

#### `to` and `end`
`to` and `end` are essential for creating procedures in NetLogo. `to` begins a procedure, and `end` concludes it. You can create procedures that can do anything! Simply add all your code within `to procedure-name` and `end`. 





2. `ask`

   `ask` is used to make agents and agentsets do things. This is how you accomplish almost all actions in NetLogo. You can use `ask` on turtles, links, and patches. Within the `[...]` following `ask`, simply define the actions you want the agents to complete.

   3. tick`

   ``tick` is used to advance the tick-counter in your model. A tick is just a measure of time in NetLogo, like minutes or seconds. `tick` is only necessary when using tick-based updates. When you use `tick`, it increases the tick counter by 1, and updates all the plots and monitors in your model.

   

   4. `if`

   `if` is used to conditionally run a command. If you want a portion of code to run only if a certain check passes, you would use `if`. For example, if you want turtles to move **only** if they are standing on a red patch, you could use `if` to say:

   ``` ask turtles [```

   `````` if [ pcolor ] of patch-here = red [```

    forward 1`````

   

   5. `set`

   `set` is used to set the value of a certain variable. A variable is (how to describe a variable here??) This can be used for any type of variable: turtle variables, patch variables, locally defined and globally defined variables. 

   

   6. `clear-all`

   `clear-all` is used to clear out everything in your model. This is usually used in your `setup` procedure, to start your model off with a clean slate. `clear-all` clears any turtles and links, resets all variables, and sets patches back to black.

   

   7. `and` and `or`

   `and` and `or` are used to check multiple conditions at the same time. `and` will only return true if both of the individual conditions are true, while `or` will return true if at least one of the individual conditions are true. `and` and `or` are commonly used with `if` to conditionally run commands. 

   

   8. `turtles` and `patches`

   `turtles` and `patches` are used to report the agentsets of either `turtles` or `patches`. They are commonly used with `ask` to 	make the turtles or patches do things. So to make all patches or all turtles complete an action, you would say `ask turtles [ commands ]` or `ask patches [ commands ]`. 

   

   9. `create-turtles`

   `create-turtles` is how you first make turtles in your models. `create-turtles` is used by the Observer, or not within any `ask [ … ]` block. You can create any number of turtles you would like, and make them complete any action that is defined in the `[ … ]` following `create-turtles`. 

