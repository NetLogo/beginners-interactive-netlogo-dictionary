`turtles-own` allows us to define custom turtle characteristics (variables) for all the turtles in a model (in addition to the default turtle characteristics such as `color`, `size`, and `heading`). Although the name of the characteristic will be the same for all the turtles, each turtle will have a different value for these custom characteristics. Once we create such custom characteristics, we can use the `set` primitive to change its value. For example, if we wanted to create a model of electric vehicles in which each car had a different level of remaining battery, we would write the following code:



```
turtles-own [remaining-battery passengers]
to setup
	clear-all
	create-turtles 100 [
		set shape "car"
		set remaining-battery random 100
		set passengers one-of [1 2 3]
	]
	reset-ticks
end
to go
	ask turtles [
		if remaining-battery > 0 [
			forward 1
			set remaining-battery remaining-battery - 1
		]
	]
	tick
end
```



Things to keep in mind when using `turtles-own`:

* You should always use `turtles-own` in the beginning of your code, on top of the code tab.

* We can define multiple characteristics within a `turtles-own` primitive by separating each characteristic with a space.

* You can create breed specific characteristics by following the `<breed>-owns` format. For example, if we had a model with *banks* and *customers*, we could write `banks-own [balance customer-list] customers-own [income]`. If you have multiple breeds in your model, characteristics defined with `turtles-own` will apply to all turtles regardless of their breed.

  

In the model example below, we have three cars on three parallel roads. Each car has a different amount of gas in its tank, shown with a label next to each car. When the *go* button is clicked, each car starts moving forward until they run out of gas.