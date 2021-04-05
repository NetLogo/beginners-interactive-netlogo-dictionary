`pcolor` is a built-in patch variable that reports the color of a patch. Because `pcolor` is a variable, as well as a reporter, you can use  `set` to change it. `pcolor` can be set by simply stating the color (e.g., brown, yellow, red; note that there are no quotation marks around the color names) or NetLogo color (a single number). For example, if we wanted to make our patches blue to represent an ocean and then create an island in the middle, we would write the following code:



```
ask patches [
	set pcolor blue
	if distancexy 0 0 < 5 [
		set pcolor brown
	]
]
```



If we wanted to put some trees on our island, `pcolor` would be useful as follows:



```
create-trees 10 [
	move-to one-of patches with [pcolor = green]
]
```



Things to keep in mind when using `pcolor`:

* A turtle can directly access `pcolor` of its patch. For example, `ask turtles [set pcolor green]` results in the same outcome as `ask turtles [ ask patch-here [ set pcolor green ] ]`.
* NetLogo uses a custom numbering scheme to represent colors. You can access this color numbering scheme by clicking the *Tools* menu and choosing the *Color Swatches* option. 
* As you noticed in the examples above, you can use the names of the common colors directly in your code. These names are: `red`,`green`,`blue`,`brown`,`black`,`pink`,`white`,`violet`,`magenta`,`cyan`, and `gray`.  
* You should write the name of a color directly, without any quotations around the color name (`""`). 
* As NetLogo uses a simple numbering scheme for colors, you can actually treat color names like numerical values. This allows us to manipulate the lightness of colors with simple math. For example, `green + 2`is will result in a lighter green color, while `green - 2` will result in a darker green. You can also use non-integer numbers to achieve an even more precise color such as `red + 0.25`or `blue - 1.85`.





In the model example below, we have some sheep that wander around randomly. We use `pcolor` to make some of our patches brown to represent ground and some of our patches to represent grass. Sheep can only eat when they are on a patch with grass on it, so they can only eat `if pcolor = green` . This model not only changes the `pcolor` of a patch using `set`, but it shows how `pcolor` can be used in conditional statements.