`Set` changes the value of a variable to the provided new value. We can use `set` to change the values of global variables created with `globals`, local variables created with `let`, predetermined agent characteristics (e.g.,  `pcolor`, `size`, `xcor`), and custom agent characteristics created with `turtles-own`, `patches-own`, and `links-own`. For example, if we wanted to assign a random age to each turtle and make older turtles blue, we would write the following code:



```
turtles-own [age]
to setup
	clear-all
	create-turtles 100 [
		set color green
		set age random 80
		if age > 65 [
			set color blue
		]
	]
	reset-ticks
end
```



In the model example below, we have a garden with some brown patches that represent the areas on which berry plants grow. Our farmer moves around randomly and picks the berries. Each plant has a different amount of berry. We use `set` for various goals in this model. First, we use `set` to change agent characteristics such as the shape of the farmer, the pcolor of the patches, and the shape of the plants. Then, we use `set` to count the total amount of berries that our farmer collects.

