`face` sets a turtle’s heading to point towards another specific agent. `face` is usually used to point a turtle towards another turtle or a specific patch. For example, if two turtles are on opposite edges of a model, `ask one-of turtles [ face other-turtle ]` will turn the turtle to face the other turtle. `ask turtles [ face patch 0 0 ]` will turn all turtles to face the center of the model. 



In the model below, there is a cat chasing a mouse. The mouse is running from the cat and is trying to escape into its mouse hole. To make the cat chase the mouse and the mouse to run to its hole, we use `face`. 

