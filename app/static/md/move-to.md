`move-to` allows a turtle to set its x and y coordinates to be the same as another turtle or patch without altering the turtle's other variables (e.g., heading, color, size). The format of this is `move-to *insert agent here*`. For example:

```
ask rabbits [
	move-to one-of patches with [pcolor = green]
	eat-grass
]
```
This paragraph of code would make each rabbit move to the exact location of a randomly picked green patch. **Note** that if the target turtle or patch does not exist, the model will give an error. 
