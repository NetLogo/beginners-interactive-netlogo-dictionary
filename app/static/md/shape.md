`shape` is a turtle and link characteristic that represents the shape of an agent and allows us to change an agent's shape using the `set` primitive. New turtles and links are created with the default corresponding shapes. We can change an agent's shape using `set shape “shape-name”` format within an `ask` context. In addition, we can use `shape` as a reporter/variable to create conditionals etc. For example, if we wanted to create a model in which we wanted our turtles to look like either sheep or wolves and then make the wolves large, we would write the following code: 



```
ask turtles [ 
	set shape one-of ["wolf" "sheep"]
	if shape = "wolf"[
		set size 1.5
	]
] 
```


Things to keep in mind when using "shape":

* You must quotation marks (`“”`) for the shapes.
* To view the list of available shapes in NetLogo, click on the Tools menu and choose the “Turtle Shapes Editor” or the “Link Shapes Editor” options. Each new NetLogo model comes pre-loaded with a small set of shapes (e.g., sheep, turtle, car, square) that you can directly use in your code. For example, the following code would work in any new NetLogo model: `ask turtles [set shape "plant"]` but the following code would throw an error: `ask turtles [ set shape “cactus”]`. You can use the “Import from library” option in the editor to find an extensive list of shapes that are used in other models. Additionally, you can create your own shapes in the editor.





In the model example below, there are sheep and wolves wandering around. Only the sheep eat the grass, not wolves, so we can distinguish between them by using `shape` to narrow down the agents who eat grass to only `turtles with [ shape = "sheep" ]` . 