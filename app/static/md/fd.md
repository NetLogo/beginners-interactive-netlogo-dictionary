`forward` is a turtle primitive that makes the asked turtle move forward on a straight patch for a provided number of units. The shorthand version of this primitive is `fd`. 



```
ask turtles [
	forward 2
]
ask turtle 0 [
	fd 3.35
]
```





Things to keep in mind when using `forward`: 

* You can provide both integers (e.g., 48, -4) and floating point numbers (e.g., 0.05, -6.23, 3.14159).
* If you provide negative numbers, the turtle will move backwards on a straight path.
* You can provide a variable instead of a specific number such as `ask turtles [ forward speed]`.
* A turtle will always maintain its straight path with the `forward` primitive. 
* If you ask a turtle to move forward in a way that requires it to move beyond the edge of the NetLogo world, there are two possible outcomes:
  * If the world wrapping is turned on, which is the default setting in new NetLogo models, your turtle will leave the world on one edge and enter it again from the opposite edge.
  * If the world wrapping is turned off (through the Settings menu), your turtle will move all the way to the world's edge and then get *stuck* there unless you change its direction with either the `right` or `left` primitives or by using the `set` primitive to change its `heading` parameter.  



In the model example below, we have a road represented with gray patches and a car on the road. We use the `set heading 90` code in our *setup* procedure to make sure that our car is heading towards east. Our model has 3 different go buttons: `go-slow`, `go-fast`, and `go-back`, each doing exactly what the name suggest. 

