`color` is a built-in turtle characteristic that represents the color of each turtle in a NetLogo model. Every time we create new turtles, each one is assigned a random color. We can use the `set` primitive and the `color` primitive together to change a turtle's color as follows: `set color red`. 



```
ask turtles [
	ifelse size > 2 [
		set color red
	][
		set color green
	]
]
```



`color` is also a reporter; we can use it to access the color of a turtle as follows: 

```
ask turtles with [color = red][
	set size 5
]
```



Things to keep in mind when using `color`: 

* NetLogo uses a custom numbering scheme to represent colors. You can access this color numbering scheme by clicking the *Tools* menu and choosing the *Color Swatches* option. 
* As you noticed in the examples above, you can use the names of the common colors directly in your code. These names are: `red`,`green`,`blue`,`brown`,`black`,`pink`,`white`,`violet`,`magenta`,`cyan`, and `gray`.  
* You should write the name of a color directly, without any quotations around the color name (`""`). 
* As NetLogo uses a simple numbering scheme for colors, you can actually treat color names like numerical values. This allows us to manipulate the lightness of colors with simple math. For example, `green + 2`is will result in a lighter green color, while `green - 2` will result in a darker green. You can also use non-integer numbers to achieve an even more precise color such as `red + 0.25`or `blue - 1.85`.



In the model example below, we have a white sheep and some plants. We use the `color` primitive to make some of the plants green and some yellow. We use the `ask turtles with [color = white]` to just ask the sheep to move, while the plants remain stationary. Our sheep moves around randomly. When there is a yellow plant on the same patch, our sheep just ignores it. However, if there is a green plant on the same patch, our sheep eats the green plant. 
