`die` is a primitive that we use to remove turtles and links from a model. When a turtle or link is asked to `die`, it no longer exists in the model, it will not execute any more code, and it will disappear from any agentset it was in. For example, the following model would have 9 turtles.



```
create-turtles 10
ask one-of turtles [ die ]
```



In the model example below, a flock of cows move around on a grassland. Every time they are on a green patch, they eat the grass there and gain energy. Every time they move, they loose some energy. If a grass ever has 0 energy, it dies and removes itself from the model. 

