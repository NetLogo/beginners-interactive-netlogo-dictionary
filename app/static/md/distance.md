`distance` is a turtle and patch primitive that reports the distance between the current agent and some other agent. For example, if you wanted to print out the distance from turtle 0 to turtle 1, you could write 



```ask turtle 0 [show distance turtle 1]```



 or, from the other direction, 



```ask turtle 1 [show distance turtle 0]```



Note that `distance` respects any wrapping that the world is set up to do. So if the world wraps horizontally or vertically, `distance` will report the shortest distance between two turtles, which might be along a path that wraps around the world.

In this example, `distance` is used to implement rudimentary path finding for a lumberjack. The lumberjack has a "target" tree that it will try to move towards and cut down. Once it cuts down that tree, it will set its target to be the closest tree. (In the case of ties, one of the closest will be randomly chosen.) We use `distance` to get the distance between the lumberjack and all of the trees so that we can figure out which tree is closest.
