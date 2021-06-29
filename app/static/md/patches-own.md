`patches-own` is a special NetLogo keyword that allows us to define characteristics that belong exclusively to the patches in a model. These characteristics are variables that have a unique value for each individual patch. `patches-own` is helpful in modeling environmental variables. For example, if we wanted to create a model of pollution where a factory would pollute the patches immediately near them:



```
patches-own [pollution]
create-turtles 1 [
	set shape "factory"
	ask patches in-radius 3 [
		set pollution 100
	]
]
```

 



Things to keep in mind when using `patches-own`:

* We can define as many variables as we want within `patches-own` such as `patches-own [water nutrients heavy-metals altitude]` by separating each variable with a space.
* A turtle can access a characteristic of its current patch directly. For example, `ask turtles [set pollution 100]` does the same thing as `ask turtles [ ask patch-here [set pollution 100] ]`.





In the model example below, we are modeling a garden with flowers. We define a *nutrients* characteristic for our patches and assign each patch a random number of nutrients between 0 and 10. We also change each patch's `pcolor` according to its nutrient level so that a darker patch indicates higher nutrient levels. Finally, we sprout a flower on each patch. Initially, each flower has the same size but when the go button is clicked, each flower grows according to the nutrition level of their patch.

