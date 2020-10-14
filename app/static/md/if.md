`If` is used when you want to conditionally run a command. It has the form of:



 ```if condition [ command ], or `if this-is-true [ then run these commands ]```



 If the condition is **True**, the command will run. If the condition is **False**, the commands will not run, and if the value resolves to anything other than true or false, an error will occur.  For example, 



```ask turtles [ if time = night [ sleep ]```



 would mean “if it is nighttime, then the turtles will go to sleep”. Multiple commands can be executed, as long as they are all contained within the same `[ ]`.



In the model below, people are playing a game of "the floor is lava". We create conditionals using `if` to determine if a person is safe (on a blue patch) or out (on a lava patch).