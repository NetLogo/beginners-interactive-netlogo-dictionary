`Nobody` is a special value used to indicate that the agent you were looking for does not exist. When a turtle dies, it becomes equal to `nobody`. `Nobody` is often used to check that there is an agent in an agentset, to avoid an error. For example, you might include 
```
if one-of turtles with [color = red] != nobody [ 
   ask turtles with [color = red ] forward 1 ]
```
 so in the case that there weren’t any red turtles, you would prevent an error.

It is important to note that an empty agentset is not equal to `nobody`; `nobody` is only used when looking for a single agent, usually in the context of `turtle`, `one-of`, or `max-one-of`. 