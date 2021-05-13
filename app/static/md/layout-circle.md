`layout-circle` is a primitive that moves a set of turtles into an evenly spaced circle of a given radius. For example:



```
create-turtles 100 [
	set shape "person"
]
layout-circle turtles 10
```



Things to keep in mind when using `layout-circle`: 

* `layout-circle` is an *observer-only* primitive, so you cannot use it within an `ask` statement.
* The actual placement of turtles in a circle layout will be random every single time you use this primitive with an *agentset*. 
* You can use layout-circle with custom turtle breeds such as `layout-circle tables 3`.



The model example below demonstrates how  `layout-circle` works. It has two *setup* buttons: one to create an empty model and another to create a model with 10 houses at random places. When the go button is clicked, we create a new house at each tick if there are less than 10 houses (i.e. if we used the setup-empty button). Then, we use `layout-turtle` to organize our neighborhood. This model also includes a variable radius and increments it at each tick to show how `layout-turtle` works for different radius values.