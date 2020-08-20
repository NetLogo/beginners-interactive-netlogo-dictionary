`other` reports an agentset which is the same as the input agentset but omits the agent who is asking for the report. In other words, it excludes an agent from the resulting agentset. For example:
```
show count turtles-here
=> 10
show count other turtles-here
=> 9  
```
See how one number is excluded from the agentset which then results in the final count to be “9”. 

`other` is often useful when we want our agents (e.g., turtles) interact with other agents. For example, if we write `ask turtles [if any? turtles-here [set color red]]` would make all the turtles red because turtles-here reports the original turtle as well. There are always at least 1 turtle when we use turtles-here. However, if we write “ask turtles [if any? other turtles-here [set color red]]”, only the turtles who have another turtle on the same patch would turn red.

