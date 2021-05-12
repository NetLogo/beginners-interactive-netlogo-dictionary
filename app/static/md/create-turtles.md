`create-turtles` is a primitive that creates a given number of new turtles in the model. These new turtles are all placed at the center of the model with the same default shape but with random colors and headings.  The shorthand version of this primitive is `crt`.



```
create-turtles 1015
crt 30
```





In addition, we can use the brackets () `[ ]`)  to immediately give some rules to our new turtles. For example, the following code would not only create 100 new turtles but also make all of these turtles green and make each one go to a random patch. This way, we would not need to use a separate `ask` command.



```
create-turtles 100 [
	set color green
	move-to one-of patches
]
```



Things to keep in mind when using `create-turtles`: 

* You can use the `create-<breed>` format to create new turtles of a specific custom breed such as `create-dogs 100` or `create-buildings 5 [ set color gray ]`.
* Only the `observer` can create new turtles. You cannot use this primitive within an `ask` primitive. For example, both `ask chickens [create-eggs 1]` and `ask patches [ create-plants 1 ]` would show an error message. If you need already existing turtles to create new turtles, you should use the `hatch` primitive. If you need the patches to create new turtles, you should use the `sprout` primitive.



In the model example below, we use the `create-turtles` primitive to create a landscape with a house, some plants, people, dogs, and clouds. 