`link-neighbors` is a turtle primitive that reports an agentset that contains all the turtles that are connected to the original turtle via links. For instance, if we were using links to represent friendship relationships, a turtle could send its friends new messages by using the `link-neighbors` primitive. For example, the following code would ensure that turtles with less than 2 friends make new friends.



```
ask turtles [
	if count link-neighbors < 2 [
		make-new-friends
	]
]
```





In the model example below, we use `link-neighbors` to simulate contact tracing. Every time two turtles get close to each other, a link between them is formed. Each link represents a "contact" between two turtles, so calling `link-neighbors`  on an individual reports back every other person that this individual had contact with. When we implement the `trace-back` procedure in our code (on line 26), we ask all of the `link-neighbors` of any exposed (red) individuals to turn red themselves to signify that they have been exposed as well.