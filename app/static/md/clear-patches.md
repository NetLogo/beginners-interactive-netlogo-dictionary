`Clear-patches` is a primitive that resets all the patches at once. It makes the values of the custom patch variables (defined with `patches-own`) to their default initial values and makes all the patches black. The shorthand version of this primitive is `cp`. 



`clear-patches` is only used when we do not want to use *clear-all*. For example, if you wanted to clear the patches but keep some global variables’ values and the keep the existing turtles the same, you would use `clear-patches`. 



In the model example below, we have two buttons. The first one makes patches' color green and creates some cows on random positions. The second button simply runs the `clear-patches` primitive to clear the patches but leave the cows the same. 



