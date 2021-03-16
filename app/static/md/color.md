`color` is a built-in turtle characteristic that represents the color of the turtles in a NetLogo model. Every time we create turtles, each one is assigned a random color. We can use the `set` command and the `color` primitive to change a turtle's color as follows: `set color red`. It is also a reporter; we use it to access the color of a turtle. 



 ```ask turtles [ set color brown ]``` 



will set the initial color of the turtles brown. In the model below, there are some eagles, white rats, and gray rats. The eagles are hunting the rats, but can see the white rats much better than the gray. So if an eagle is on the same patch as a white rat (but not a gray one) it will eat it.
