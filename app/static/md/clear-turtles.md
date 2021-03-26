`clear-turtles` is a primitive that removes all the turtles from the model. You can also use its shorthand version `cp` in your code. 



`clear-turtles` is only used when we do not want to use *clear-all*. For example, if you wanted to remove the turtles but keep some global variables’ values and/or the keep the patch colors the same, you would use `clear-turtles`. 



In the model example below, we have three buttons. The first one makes patches' color green and creates some cows on random positions. The second button runs the `clear-patches` primitive to clear the patches, as a proxy for grass, but leave the cows the same. The third button runs the `clear-turtles` primitive to remove the cows from the model but leave the patches/grass as is. 
