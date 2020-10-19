` To` is used to begin a command procedure. You can think of `to` as a way to define a set of actions/verbs for NetLogo, such as `to go`, `to add-money`, etc. You can use these procedures anywhere in the code. **Note**: You must put `end` at the end of the procedure in order for it to work. Procedures can also be called from buttons! For example, using a `go` button (which is located on the Interface tab) runs the procedure created as to go ... end. Let’s see that in action. 

```
to setup
clear-all
create-turtles 100
end
```

`Setup` is the procedure name. `Clear-all` &  `create-turtles 100` are the commands in this procedure. And `end` tells NetLogo that the procedure is complete. When this is used as a button, this all happens at once. 

Another purpose for this primitive is to divide code into smaller pieces. For example:
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
fd 1
end
```
See how in the first chunk of code, you are calling the turtles to *wiggle*, then *move*. **Wiggle** and **move** are then written as a command procedure. It ends up saving you a lot of space and repetition!
