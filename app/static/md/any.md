`any?` is used to determine if there are at least one agent within a given agentset. If there are, it will return **true**, otherwise it will return **false**.



For example, the following code would repeat running the `go` procedure on a repeated basis as long as there is at least 1 turtle in the model. If, let's say, there were many turtles but they could `die`, the model would stop when all the turtles die.

```
while any? turtles [ go ]
```



You can combine `any?` with a conditional reporter using the `with` primitive such as the following example that stops the model if any of the turtles in the model are smaller than 1 unit: 

```
if any? turtles with [size < 1] [stop]
```



Things to keep in mind in mind when using `any?`: 

* Don't forget the question mark (`?`) at the end. 
* You can use the `not` primitive, like in the example above, to reverse the outcome of `any?`. This would come handy if you 
* `any?` itself does not do anything; you should use it within a conditional statement such as `if` and `if-else` or other primitives that require true-false values such as `while`. 

<br />

The model example below represents the spread of a contagious disease within a healthy population. We use `any?` primitive to run the model as long as there is at least one healthy (green) individual in the model. Once all of the individuals turned red, the model automatically stops.

