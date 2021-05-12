`clear-patches` is a primitive that resets all the patches at once. It makes the values of the custom patch variables (defined with the `patches-own` primitive) to their default initial values and makes all the patches black. You can also use its shorthand version `cp` in your code. 



`clear-patches` is only used when we do not want to use *clear-all*. For example, if we wanted to clear the patches but keep some global variables’ values and the existing turtles the same, we would use `clear-patches`. 



In the model example below, we have three buttons. The first one makes patches' color green and creates some cows on random locations. The second button runs the `clear-patches` primitive to clear the patches, as a proxy for grass, but leaves the cows the same. The third button runs the `clear-turtles` primitive to remove the cows from the model but leave the patches/grass as is. 