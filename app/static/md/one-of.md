`one-of` reports one randomly selected member from a provided agentset or list. For example, if we were creating a forest fire model in which a fire broke out at a random patch, we would write the following code:



```
create-trees 100 [
	set shape "tree"
	set color green
	move-to one-of patches
]
ask one-of trees [
	set color red
]
```



Things to keep in mind when using `one-of`:

* We can also use `one-of` with lists. For example, if we wanted each of our turtles to pick a random color from a predetermined list, we can write the following code: `ask turtles [set color one-of [red green blue yellow]]`.

* If `one-of` is used on an empty agentset or list, NetLogo will show an error and your model will not work.

  

In the model example below, we have a small population of blue turtles representing healthy people. We use `one-of` to turn one randomly picked turtle red, which indicates an infected agent (i.e., patient zero).

