`with` is a reporter primitive that allows us to extract a sub-agentset from an agentset based on a provided set of conditional statements. A condition within a `with` statement is similar to an `if` statement. For example, if we wanted to model a predator-prey ecosystem where a hawk could only see brighter colored mice, but not the darker colored ones, we would write the following code:



```
ask hawks [
	if any? (mice-here with [color = gray and distance myself < 2]) [
		hunt
	]
]
```



Notice that we first wrote the name of the agentset (`mice-here`), then used the `with` primitive, and then provided our conditional statements within brackets (`[ ]`).



Things to keep in mind when using `with`:

* We can use `with` for all kinds of agent types (`turtles`, `patches`, and `links`).
* You can also do some simple operations within a reporter that comes before `with` such as `customers with [(checking-account + savings-account) > 1000]` to get an agentset that contains only the customers whose total account balance is larger than 1000 or `circles with [size / 2 > 1]` to get an agentset that contains only the circles with a radius larger than 1.



In the model example below, we have three parallel roads and each road has a car on it. In the go procedure, we use `with` to differentiate between the speeds of blue cars and red cars. Blue cars go twice as fast as the red cars when they also have enough gas. When a car does not have enough gas, it goes much much slower. Lastly, we use `with` to stop the model when all the cars run out of gas.



