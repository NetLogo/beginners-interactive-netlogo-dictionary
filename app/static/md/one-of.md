### **one-of** agentset
### **one-of** list
`One-of` is used to randomly select only one agent out of an agentset or a list. For example `ask one-of patches [ set pcolor red ]` will turn one random patch red. `One-of` can also randomly select one item from a provided list. For example, `ask turtles [set color one-of [ red yellow blue ] ]` will change the color of each turtle randomly to either red, yellow, or blue.

If `one-of` is used on an agentset which has no agents (for example, `ask turtles with [color = red]` but there are no red turtles), an error will occur. See `nobody` for how to prevent the error. 