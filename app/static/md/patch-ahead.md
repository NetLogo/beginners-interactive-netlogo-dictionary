`patch-ahead` reports the single patch that is the given distance *ahead* of the asking turtle. You can think of it as the turtle looking at a patch in front of it. For example, if we were creating a highway traffic model and wanted our cars to only move if there was no other car in front of them, we would write the following code:



```
ask cars [
	set heading 90
	if count turtles-on patch-ahead 1 = 0 [
		forward 1
	]
]
```



Things to keep in mind when using `patch-ahead`:

* In some cases when a model's world *is not wrapping*, `patch-ahead` may report `nobody` and lead to an error because a patch may not exist. We can avoid this error by using an if statement like `if patch-ahead 1 != nobody [ forward 1 ]`.
* We can provide floating point numbers to `patch-ahead`, as well as integers, such as `patch ahead 2.76`.



In the model example below, we have some gray patches that represent a road and a red patch that represents a stop sign. Our car moves on the road towards east as long as the `pcolor` of the `patch-ahead 1` is gray. If not, our car does not move, which means that it stops at the stop sign.