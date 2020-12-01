`and` is a primitive that allows us to combine two true-false statements into one single statement that is true *if and only if* both statements are true. 

For example, if we wanted a turtle to eat **only** if (A) they were hungry *and* (B) if there was food on the same patch, we could say:



```
if my-hunger-level > 100 and food-here > 0 [
  eat-food
  set my-hunger-level 0
]
```



In the model example below, we use `and` to generate a river down the middle of our world. A patch turns blue *if and only if* its x-coordinate is *both* to the left of `(width / 2)` *and* to the right of `- (width / 2)`, otherwise, it remains a green patch.