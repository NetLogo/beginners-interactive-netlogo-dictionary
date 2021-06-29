`count` is a primitive that reports the number of agents in a given agentset. For example, `count turtles` reports the total number of all the turtles in a model, while  `count turtles with [color = green]` reports the number of green turtles in the model. You can use `count` with turtles, patches, and links. 



We can also use `count` with turtle breeds and link breeds such as `count dogs` or in combination with other reporter agents primitives such as `count turtles-here`.



In the model example below, we have a dog park at the center and we have a bunch of turtles that represent the dogs in a neighborhood. Our dogs move around completely randomly. When there are more than 5 dogs in the playground at any given time, our model shows a *"Playground is too crowded"* message.