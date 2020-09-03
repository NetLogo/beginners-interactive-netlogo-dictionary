`Set` sets a variable to a certain value, and takes the form `set variable value`. It can set global variables that have been defined at the top of the code, and local variables that were defined by `let`. It can also set variables belonging to the agent who calls `set` (including turtle, breed, or patch variables defined by turtles-own or patches-own); for example, 

```
turtles-own [age] 
ask one-of turtles [ 
	set age 10 ]
```
would set the age of a turtle to 10. Turtles can also access and set the variable of the patch they are standing on. 