`layout-circle` is a primitive that automatically lays out an agentset or list of turtles into an evenly spaced circle of a given radius centered around the center of the world, all facing outwards. It is often used with models that use links because it makes it easy to see which turtles are connected to which. 

The syntax is `layout-circle agentset radius` or `layout-circle list-of-turtles radius`. It is an observer command (i.e., not called within an `ask` block or anything like that) because it acts on all of the turtles "at once", not just one at a time. When using an agentset, the order of turtles is random, but when used with a list-of-turtles, the turtles are arranged clockwise in the given order starting at the top of the circle. 

The model below shows a typical use of `layout-circle` in a network diagram. 
