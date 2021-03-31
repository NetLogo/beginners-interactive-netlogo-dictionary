`in-cone` is a primitive that heps us simulate a "cone of vision" in front of a turtle. It allows us to model an agent having some sight or other sense in front of them, but not behind or to the side of them.

The cone is constructed with two inputs: how far the agent can see (*radius*), and how wide the agent can see (*degrees between 0 to 360*). For example, if we wanted some rabbits to eat if there were carrots in front of them, but not behind or to the side, we could write the following code:



```
ask rabbits [
  if any? carrots in-cone 3 45 [ eat ]
]
```



Things to keep in mind when using `in-cone`: 

* You can also use floating point values for the radius and angle parameters such as `in-cone 1.25 66.66`.
* Both *turtles* and *patches* can use `in-cone`.
* Keep in mind that `in-cone` may report the original turtle, too, if you are using the same breeds. Be sure to account for that in your models by using the `other` primitive. For example, this code would throw an error `ask turtles [ create-links-with turtles in-cone 2 30 ]`, while this one would work fine `ask turtles [ create-links-with other turtles in-cone 2 30 ]`. 
* You can combine `in-cone` and the `with` primitive to narrow down the target agents but make sure to encapsulate the first `with` statement within parantheses `( )`. For example, you can write a code like `if any? (carrots with [color = orange]) in-cone 3 45 [ eat ]`.



In the model example below, we use `in-cone` to simulate four motion-activated wildlife cameras. When a camera detects that there are `any? animals in-cone 8 50`, it will turn yellow to simulate taking a picture. (Note that the highlighted patches are just to better visually show the cone of vision. In actuality none of the `in-cone` turtle detection has anything to do with which patch a turtle is standing on.)