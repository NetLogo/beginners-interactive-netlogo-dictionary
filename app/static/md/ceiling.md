`ceiling` is a mathematics primitive that rounds *reports* the closest integer above a given number. In other words, it rounds the number *up*. For example, `ceiling 5.2` would report 6, and `ceiling -4.8` would report -4. 



In the model example below, each turtle has a `my-money` variable that increases or decreases a little bit at each tick. We use the `ceiling` primitive to *round up* a turtle's `my-money` variable because we want to present a label under each turtle showing their current money. If we do not round this variable either up or down, its label would show many floating point numbers such as `1.822882372836`, which would be visually unpleasant. We also use the `ceiling` primitive in setting each turtle's `ycor` parameter so that the turtles move only when the rounded-up version of their `my-money` variable changes. If they make or lose only a little bit of money, they remain stationary. Lastly, we use the `ceiling` and its opposite `floor` for two of our three monitors in the interface.

