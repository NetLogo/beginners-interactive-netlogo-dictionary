`Count` returns the number of agents in a specified agentset. (Note: you can use `with` to narrow down a given agentset.) For example, `show count turtles` would show the total number of turtles in a model, and  `show count turtles with [color = green]` would show the number of green turtles in the model. 



In the model below, a group of players is trying to organize a game of basketball. Because 10 players are needed for a game of basketball, if there are less than 10 players no one can play. So we use `if count players < 10` to make sure there are enough players for the game.