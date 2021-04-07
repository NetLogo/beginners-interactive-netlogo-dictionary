` to` is used to begin a command procedure. You can think of `to` as a way to define a set of actions/verbs for NetLogo, such as `to go`, `to add-money`, `to move`, etc. We can use these procedures anywhere in the code. 



Each procedure that starts with `to` must always be finished with the `end` primitive in order for it to work. Procedures can also be called from buttons! For example, using a `go` button (which is located on the Interface tab) runs the procedure created as to `go ... end` in the code tab. Let’s see that in action:



```
to go
	ask turtles [
		wiggle
		forward 1
	]
	tick
end
```



Another purpose for the `to` primitive is to allow us to divide our code into smaller pieces. For example:



```
ask turtles [
  wiggle  ;; first turn a little bit
  move    ;; then step forward
]

to wiggle
  rt random 90
  lt random 90
end

to move
	forward speed 
end
```


See how in the first chunk of code, you are calling the turtles to *wiggle*, then *move*. **Wiggle** and **move** are then written as a command procedure. It ends up saving you a lot of space and repetition!



In the model example below, we have a very simple model with three buttons. When the `setup` button is clicked, the *setup* procedure that we created with `to setup` in our code is run by NetLogo, which makes our patches green and creates a few butterflies on random locations in the model. When the `move` button is clicked, the *move* procedure that we created with `to move` in our code is run by NetLogo, which makes the butterflies move 1 step forward at a random direction. When the `grow` button is clicked, the *g*row procedure that we created with `to grow` in our code is run by NetLogo, which makes the butterflies a bit larger.