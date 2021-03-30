`if` is a primitive that allows us to define conditional agent behaviors. It has the following structure: ```if condition [ command(s) ]```. If the given condition is true, NetLogo will run the provided code within the brackets. If the given condition is false, NetLogo will not do anything.



```
ask cars [
	if my-speed < 60 [
		accelerate
	]
]
```



Things to keep in mind when using `if`: 

* You can combine two or more conditional statements using `and` and `or` primitives.
* You can use the `not` primitive to make true statements false, and vice-versa.
* If you need your agents to follow a separate set of rules if the provided condition is false, you should use the `ifelse` primitive. 



In the model example below, we have some patches that represent mousetraps and a few mice moving around randomly. If a mouse steps on a mousetrap, it sets its `trapped?` variable to `true`. The mice who are `not trapped?` continue moving  around, while the ones who are trapped remain stationary.