`ask` is a command that is used to make the agents in the agentset do something. The syntax of this command is `ask *agentset/agent* [insert command here] `. When `ask` is used with an agentset, each agent will take its turn in a random order. For example, 

```
ask turtles [ fd 1 ] 
ask patches [set pcolor pink]
```

Each time this is run in the observer, *either* the turtles will move forward first *or* the patches will turn pink first. It is random every time!