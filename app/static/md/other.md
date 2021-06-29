`other` reports an agentset which is the same as the input agentset but omits the asking agent. It is very useful when we want turtles to communicate with each other. For example, if we wanted to create a network model in which each turtle is connected to another randomly picked turtle with a link, we would write the following link:



```
ask turtles [
	create-link-with one-of other turtles
]
```



We use `other` in this context because if we did not, there is a chance that `one-of turtles`  would report the same turtle. If this happens, NetLogo would show an error  because a turtle cannot create a link with itself.



In the model example below, we have clusters of stationary turtles randomly distributed in the world that represent people and we have a mobile turtle who represents a doctor. The doctor moves around randomly and when it comes across `other turtles`, it asks the other turtles on the same patch to turn themselves green if they are healthy and red if they are infected.