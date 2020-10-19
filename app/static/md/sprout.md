`Sprout` creates new turtles from the current patch, and must be used within an `ask patches [...]` context.  It takes the form of:



 ```sprout number-of-turtles [ optional-commands ]```



Unless specified in the commands, the new turtles will have random headings and colors. After being created, the turtles run the commands one at a time, in a random order. `Sprout-<breed>` can also be used to create turtles of a specific breed. For creating new turtles from existing turtles, see `hatch`. 



In the model below, there is a swamp full of bugs. If a patch is swampy enough, it will `sprout` a new bug.

