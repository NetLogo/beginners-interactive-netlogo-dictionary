`count` is a primitive that reports the number of agents in a given agentset. For example, `show count turtles` would show the total number of all the turtles in a model, while  `show count turtles with [color = green]` would show the number of green turtles in the model. You can use count with turtles, patches, and links.



In the model example below, we have a dog park at the center and we have a bunch of turtles that represent the dogs in a neighborhood. Our dogs move around completely randomly. When there are more than 5 dogs in the playground at any given time, our model shows a *"Playground is too crowded"* message. 