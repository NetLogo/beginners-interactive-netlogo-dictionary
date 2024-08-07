`min-pycor` reports the `pycor` of the bottommost patches in a model. This primitive and its siblings (`max-pxcor`, `max-pycor`, `min-pycor`) are very useful in modeling the agent behavior that involves the boundaries of an environment. For example, if we wanted to build a model where we had a wall at the edges, we would write the following code:



```
ask patches [
	if pxcor = max-pxcor or
	   pxcor = min-pxcor or
	   pycor = max-pycor or
	   pycor = min-pycor [
	   		set pcolor gray
	   ]
]
```



Or if we wanted turtles to not walk beyond the world's borders, we would write the following code:



	ask turtles [
		if [pxcor] of patch-ahead 1 < min-pycor [
			forward 1
		] 
	]



Things to keep in mind when using `min-pycor`: 

* `max-pxcor`,`min-pxcor`,`max-pycor`, and `min-pycor` are not variables; they are constant reporters. That is,a code such as `set min-pxcor 30` would show an error message. 
* You can change your model's size through the **Settings** button in the Interface Tab or using the `resize-world` primitive.



In the model example below, we use `min-pycor` and its siblings to create walls that represent a container. The balls inside the container bounce off of the green wall but they *stick* to the red wall.