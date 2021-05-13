`sprout` is a patch-only primitive that allows us to ask patches to create new turtles. It must be used within an `ask patches [...]` context.  For example, if we wanted to create a model in which each patch sprouted a flower once it was watered enough, we would write the following code:



```
ask patches [
	if water-level > 10 [
		sprout 1 [
			set shape "flower"
			set color yellow
			set size 0.1
		]
	]
]
```



Things to keep in mind when using `sprout`:

* A patch can sprout as many turtles as provided.
* `sprout` will result in an identical outcome to `create-turtles`, but it will automatically assign the new turtles' coordinates to the center of the sprouting patch.
* as in `create-turtles`, you can pass optional rules for the new turtles to follow by simply adding the brackets (`[ ]`) at the end of a `sprout` statement as shown above.
* `sprout` can also be used with breeds. For example, if we had a *plants* breed, we could use `sprout-plants 3`.
* Unless specified in the commands, the new turtles will have random headings and colors.
* Only `patches` can *sprout* new turtles. If you need your turtles to create new turtles, you should use `hatch`.



In the model example below, we have an empty garden and a farmer. Our farmer moves around randomly and fertilizes each patch. When a patch is fertilized, its `pcolor` turns into a lighter brown. Once a patch reaches a certain level of fertilization, it sprouts a new plant. If the farmer fertilizes a patch that already has a plant there, the fertilizer helps the plant grow.

