`any?` is used to determine if there are at least one agent within a given agentset. If there are, it will return **true**, otherwise it will return **false**. 

<br />

Its syntax is: **```any? agentset```**

<br />

For example, the following code would stop the model if there are zero turtles in the unit. If there is even one turtle, the model would continue running: 

```
if not any? turtles [stop]
```



You can combine `any?` with a conditional statement  using the `with` primitive such as the following example that stops the model if any of the turtles in the model are smaller than 1 unit: 

```
if any? turtles with [size < 1] [stop]
```



The model example below represents the spread of a contagious disease (red) within a healthy population (green). We use `any?` primitive to run the model as long as there is at least one green individual in the model. Once all of the individuals turned red, the model automatically stops.

