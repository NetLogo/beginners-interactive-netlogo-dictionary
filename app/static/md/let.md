The `let` primitive allows us to create new local variables and set their initial values. A local variable is a variable that only exists within the procedure it was created in or within the brackets of a specific `ask` statement. However, similar to a `global` variable, its value is the same for all the turtles. Once you create a local variable with `let`, you can then use the `set` primitive to assign it a new value. `let` is very useful for calculating temporary values or creating temporary agentsets.



```
ask turtles [
	let people-nearby (other turtles in-radius 2)
  if any? people-nearby [
  	let new-friend one-of people-nearby
  	set my-friends (lput new-friend my-friends)
  ]
]
```



The model example below shows how `let` works. We have some happy and some sad turtles in this model. Every time two turtles are on the same patch, one turtle will ask the other to change its shape. In a way, either a sad turtle will make its friend sad, or a happy turtle will make its friend happy. We use `let` in this model because it allows us to not rewrite a longer piece of code again and again (`other turtles-here`).

