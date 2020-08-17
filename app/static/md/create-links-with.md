`create-links-with` is a turtle procedure that creates a link between the current turtle (self) to every member of a provided agentset. (compare with `create-link-with`, which creates a link from the current turtle to a *single* other turtle).

One important thing to keep in mind when using `create-links-with` is that a turtle creating a link to oneself will cause an error. For example, if you were to write:

```
ask turtles [
  create-links-with turtles in-radius 5
]
```

you would get an error, because the current "self" turtle would be included in `turtles in-radius 5`, causing a turtle to try to create a link with itself, which is not allowed. To avoid this issue, you will often see the command `other` used with `create-turtles-with` to ensure that no self-links are accidentally created. For example, to fix the above bug, you can instead write:

```
ask turtles [
  create-links-with other turtles in-radius 5
]
```

In this example, `create-links-with` is used to simulate contact tracing, wherein we track every pair of interacting individuals (in our case with a link) and then use that information to track down people who may have been exposed to an infectious illness. In our model, at each tick, every individual creates a link with all other individuals within a small radius of itself, representing a "contact". We can then use the trace back button to highlight every individual who has contacted a potentially infected individual by back tracking along those links.

