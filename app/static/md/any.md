`any?` is used when you want to determine if there are any agents within an agentset. If there are, it will return **True**, otherwise it will return **False**. It can be combined with an if statement to perform an action if there are any agents at all that fit a given criteria, regardless of how many. Its syntax is 

```any? <agentset>```

Note that you can, as always, use the `with` command to narrow down an agentset. So if you wanted to check if there were any turtles with a size greater than 2, you could use 

```any? turtles with [size > 2.0]``` .

For example, imagine that you are modeling how long it takes a virus to become eradicated. It would be useful to stop the model once there are no more infected individuals to collect that data. In the model below, infected individuals are represented as red turtles. At the start of the go procedure, we check if there are any red turtles present, and if so, use the stop command to stop running the model.

