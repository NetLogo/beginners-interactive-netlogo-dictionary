`clear-all` essentially clears everything in a model: *all* drawings, turtles, plots, links, etc. It also sets the values of all the `globals` and agent properties to zero and makes all the patches black. It esentially reverts the model to a blank slate. You can also use `ca` as a shortened version.

 

`clear-all` is usually located at the beginning of a model’s setup procedure to make sure the model starts out with nothing already there. 



In the model example below, we have two buttons. The first one makes patches' color yellow and asks turtles to draw some random lines. The second button simply runs the `clear-all` primitive to clear everything. 

