`setxy` moves a turtle to the given coordinates in the world. For example, if we wanted to create a house and put it on a specific location, we would write the following code:

 

```
create-turtles 1 [
	set shape "house"
	setxy 
]
```



Things to keep in mind when using `setxy`:

* By default, the x and y coordinates at the center of the world are both 0, so `setxy 0 0` will set the position of the turtle to the center of the world.
* The x and y coordinates given to `setxy` can be decimal values, not just whole numbers, so `setxy 0.5 -0.5` will place the turtle 0.5 units to the right and 0.5 units down from the center. 
* If you want to pick a random position for a turtle, you can use the `random-xcor` and `random-ycor` primitives such as `setxy random-xcor random-ycor`. We can also mix and match this setup. For example, if we wanted our turtles to be randomly distributed along the x axis, we could write `setxy random-xcor 0`.
* Note that `setxy` follows the wrapping rules of the current NetLogo world, so in a world that is 10 units by 10 units with vertical and horizontal wrapping,  `setxy 26 42` would wrap all the way around to (6,2). 



In the model example below, `setxy` is used with two user-inputted values to place a chess piece at a chosen place on the chess board. You can imagine how essential `setxy` would be to creating an actual game of chess in NetLogo.



**Note:** The "chess board" in this model is 7 squares by 7 squares instead of the traditional 8 by 8. This was done for the sake of example because by default, NetLogo encourages worlds with odd edge lengths to make sure that the center is always at (0,0) and the overall world is symmetrical. To make this "chess board" the proper size, go into the settings panel found in the interface tab and change the location of the origin (another word for the center of the world) to "Custom". There you can change the `max-pxcor` and `min-pycor` both to 4. Voila, an actual chess board.