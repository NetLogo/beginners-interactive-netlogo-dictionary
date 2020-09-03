### **max** *list*

`Max` reports the maximum value in a given list. For example, `show max [1 2 3]` will return 3. `Max` is commonly used on a specific variable of an agentset, which would look like `max [variable] of agentset`. So 

`ask turtles with max [size] of turtles [ set color white ]`

would set the largest turtle or turtles to white. 
