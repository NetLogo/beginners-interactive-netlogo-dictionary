`mean` is a mathematics primitive that reports the mean, or average, of the numeric values in a given list. For example, `mean [4 6 -4]` would report 2. Similarly, if we wanted to demarcate the turtles who are larger than the average turtle size with a different color, we would write the following code:

```
let average-turtle-size mean [ size ] of turtles
ask turtles with [ size >=  average-turtle-size][ 
    set color green 
]
```


In the model example below, we have a farm and a farmer. Our farm initially has no plants. When the go button is clicked, our farmer moves around randomly and every time it moves, it checks whether there is already a plant on the same patch that is larger than the average size of all the plants. If there is, the farmer picks up this large-enough plant. If not, our farmer checks if there is even a plant on the same patch. If there is already a plant, our farmer leaves this small plant alone to continue growing. If there is no plant on the patch, our farmer plants a new small plant. We also use the `mean` primitive to display the average size of plants with a monitor and a plot in our model's interface.

