`move-to` allows a turtle to set its x and y coordinates to be the same as another turtle or patch without altering the turtle's other variables (e.g., heading, color, size). Its syntax is:



 ```move-to desired-agent ```



For example, if we wanted to make each rabbit move to the exact location of a randomly picked green patch, we would say:

```
ask rabbits [
	move-to one-of patches with [pcolor = green]
	eat-grass
]
```
 **Note** that if the target turtle or patch does not exist, the model will give an error. In the model below, there is a family and their house. We want the family to be in their house, and use `move-to` to move them there.

