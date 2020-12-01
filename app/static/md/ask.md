`ask` is a command that we use to make all the agents in a given agentset follow a set of rules. Its syntax is: 



```ask <agentset/agent> [insert command here] ```



When `ask` is used with an agentset, each agent will take its turn in a random order. For example, 



```
ask turtles [ fd 1 ] 
ask patches [set pcolor pink]
```



Each time this is run in the observer a random turtle will move forward, then a random patch will become pink. It is random every time!



In the model below, we want the fish to swim, the plants to wiggle, and all the turtles to move forward. To make them do their actions, we just `ask` !