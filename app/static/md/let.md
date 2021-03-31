`let` creates a new local variable and sets its initial value. A local variable is a variable that only exists within the procedure it was created in or within the brackets of a specific `ask` statement. Similar to a `global` variable, a local variable's value is the same for all the turtles.



```
ask turtles [
	let people-nearby (other turtles in-radius 2)
  if any? people-nearby [
  	let new-friend one-of people-nearby
  	set my-friends (lput new-friend my-friends)
  ]
]
```



Once you create a local variable with `let`, you can then use the `set` primitive to assign it a new value. `let` is very useful for calculating temporary values or creating temporary agentsets. For example, if we wanted to a turtle to roll 6 dices and report the sum of the dices, we could use `let` as shown below:



```
to-report roll-six
	let total-outcome 0
	repeat 6 [
		let new-outcome (one-of [1 2 3 4 5 6])
		set total-outcome (total-outcome + new-outcome)
	]
	report total-outcome
end
```



In the model example below, we have some happy and some sad turtles. Every time two turtles are on the same patch, one turtle will ask the other to change its shape. In a way, either a sad turtle will make its friend sad, or a happy turtle will make its friend happy. We use `let` in this model because it allows us to not rewrite a longer piece of code again and again (`other turtles-here`).

