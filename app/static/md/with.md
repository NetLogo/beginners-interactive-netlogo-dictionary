`With` is used to narrow down a set of agents, usually **patches** or **turtles**, by addressing a specific group of those agents that have a certain characteristic. Using `with` will address only the agents in the set that match the certain characteristic. Its syntax is:



``` agentset with [ desired-characteristic ] ```



 For example, `ask turtles with [color = blue] [forward 1]` will make only the blue turtles move forward. You can have multiple required characteristics within the `[ ]` separated by `and` or `or` to further narrow down the agentset. For example



```ask turtles with [color = red and size > 5] [ ```

```	forward 1 ]```



would make only red turtles that are bigger than 5 move forward.



