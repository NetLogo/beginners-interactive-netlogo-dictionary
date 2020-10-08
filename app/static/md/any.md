`any?` is used when you want to determine if there are any agents within an agentset. If there are, it will return **True**, otherwise it will return **False**. Its syntax is: 

```any? <agentset>```

`any?` can be combined with a conditional statement to perform an action if there are at least one agent that fit a given criteria:

```if any? turtles with [size > 2][stop]``` .



Note that you can, as always, use the `with` primitive to narrow down an agentset as the example below does to for turtles with a size greater than 2.



In the model example below, imagine that you are modeling how long it takes a virus to become eradicated. It would be useful to stop the model once there are no more infected individuals to collect that data. In the model below, infected individuals are represented as red turtles. At the start of the go procedure, we check if there are any red turtles present, and if so, use the stop command to stop running the model.

