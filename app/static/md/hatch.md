`hatch` is a primitive that creates a provided number of identical copies of a turtle. Similar to the `create-turtles` primitive, it takes a number and it also allows optional rules defined for the new turtles by following it with brackets `[]`.



```
ask turtles [
	if season = "spring" [
		hatch 3 [
			set size 0.1
			set shape "penguin egg"
			set color white
		]
	]
]
```



Things to keep in mind when using `hatch`: 

* `hatch` can only be used by turtles within an `ask` statement. If you need your patches to create new turtles, you should use the `sprout` primitive.
* You can use `hatch` for custom turtle breeds, too, by using the `hatch-pluralbreedname` convention. For example, if your model has a *penguins* breed, you can use `hatch-penguins` and if you have an `eggs` breed, you can use `hatch-eggs`.



In the model example below, we have a turtle that represents a bug and some brown patches that represent food. When a bug bumps into a patch of food while walking around randomly, it eats the food and then *hatches* a new bug. Note that every time we create a new bug with the `hatch` primitive, we add the following command around brackets `[ right random 360 ]` because if we do not add this code, our new turtle would have the exact same location, size, and direction with its parent turtle, making it virtually impossible for us to differentiate the two. 

