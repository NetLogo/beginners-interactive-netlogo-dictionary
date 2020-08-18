`Max` reports the maximum value in a given list. It takes the form of `max some-list`. For example, `show max [1 2 3]` will return 3. 

`Max` is commonly used on a specific variable of an agentset, which would look like `max [variable] of agentset`. So the following code 

```
ask turtles with [max [size] of turtles] [ 
    set color white 
]
```

would change the color of the largest turtle or turtles to white. 
