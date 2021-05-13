Patches are a special kind of stationary agents in NetLogo that make up the world of a model. You can think of the patches as the squares that make up a chess board. 



The `patch` primitive reports the specific patch with the given coordinates. For example, if we wanted to create a model of an ant colony whose entrance was the patch at the center, we could write the following code:



```
ask patch 0 0 [
	set pcolor green
]
```

 

The `patches` primitive reports all the patches in the model. This primitive is helpful in asking all the patches to do the same things (e.g., change pcolor) or narrow down a subset of patches. For example, if we wanted to create a forest fire model with some green patches representing trees, some green patches representing ground, and the leftmost patches representing the fire (red), we would write the following code:



```
ask patches [
	set pcolor one-of [green brown]
]
ask patches with [pxcor = min-pxcor][
	set pcolor red
]
```



Things to keep in mind when using `patch` and `patches`:

* The primitive `patches` will always report the same agentset, but the order of the patches will be random each time we use it.
* Like turtles, patches have characteristics, too. Some of the characteristics come prebuilt (e.g., `pcolor`, `pxcor`,`pycor`,`plabel`), but we can also define custom characteristics with the `patches-own` primitive such as `patches own [minerals water]`.
* We cannot create custom patch breeds.



In the model example below, we have a farm that is surrounded with a fence. The fence is represented with brown patches and the grassland is represented with green or lime patches. We also have a yellow square in the middle that represents a ranch and some cows who move around randomly and eat the grass on each patch until there is no grass left.

