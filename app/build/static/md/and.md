`and` is a primitive that can be used to combine two true-or-false statements, known as booleans in the computer world, into a single true-or-false statement such that the result is true *if and only if* both inputs are true. For instance, if we wanted a turtle to eat if (A) they were hungry *and* (B) if there was food in their patch, we could say:
```
if hungry? and food-here? [
  eat
]
```

In this model, we use `and` to generate a river down the middle of our world. a patch turns blue if and only if its x coordinate is *both* to the left of `(width / 2)` *and* to the right of `- (width / 2)`, otherwise, it remains a green patch.