`Max-n-of` reports an agentset that contains a **specified number of agents** with the **highest value of a given reporter**. It takes the form of:



 ```max-n-of number agentset [ reporter ]```



For example, `max-n-of 3 patches [ count turtles-here ]` would return an agentset of the three patches that have the most turtles on them. If there are less than the specified number of turtles in a given agentset, `max-n-of` will return the entire agentset. For example, if we have only 5 turtles in a model and run `max-n-of 10 turtles [ size ]`, all 5 turtles would be returned. Ties are broken randomly. 



In the model below, there are a group of people in a footrace. We want to be able to identify the leaders in the race, and will turn the 3 furthest people to a different color using `max-n-of`.

