`one-of` is used to randomly select only one agent out of an agentset or a list. It takes the form of: 



```one-of <agentset/list>```



For example, `ask one-of patches [ set pcolor red ]` will turn one random patch red. `One-of` can also randomly select one item from a provided list. For example, to change the color of each turtle randomly to red, yellow, or blue, we could say:



 ```ask turtles [set color one-of [ red yellow blue ] ]```



**Note**: If `one-of` is used on an agentset which has no agents (for example, `ask turtles with [color = red]` but there are no red turtles), an error will occur. See `nobody` for how to prevent the error. 



In the model below, a disease is being spreaded. It starts with one infected person, who is chosen randomly. To pick one person to begin the disease spread, we use `one-of` to randomly chose one turtle. 

