`create-links-with` is a turtle procedure that creates a link between the current turtle (self) to every member of a provided agentset. 



```
ask turtles [
	create-links-with other turtles-here
]
```



Notice that we use the `other` primitive in our code because if we did not use `other`, our code would give an error. NetLogo shows this error because the `turtles-here` primitive reports all the turtles in a model, including the turtle who is trying to create the links, but a turtle cannot create a link with itself. So, do not forget to use the `other primitive` when you are using similar agentset reporter primitives such as `in-radius` and `turtles`.



Also keep in mind that his primitive is used to create multiple links at once, so you need to provide an agentset. If you want to create a link with just one specific turtle, you should use the `create-link-with` primitive.\



In the model example below, we use the `create-links-with` primitive to simulate contact tracing. Every time two people are on the same patch, a new link between them is created. Then, the trace-back button/procedure uses the links between the individuals to trace back the people who may have been exposed to an infectious person. 