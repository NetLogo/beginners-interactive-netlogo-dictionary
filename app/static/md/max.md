`Max` reports the maximum value in a given list. For example, `show max [1 2 3]` will return 3. `Max` is commonly used on a specific variable of an agentset, which would look like:



 ```max [variable] of agentset```



So to set the largest turtle or turtles in a model white, we would say:



`ask turtles with max [size] of turtles [ set color white ]`



In the model below, there is a group of people who are aging. We want to keep track of who is the oldest , so we use `max` to change the color of the oldest person.