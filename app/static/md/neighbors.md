`neighbors` is used to report an agentset containing the agent's eight surrounding patches in the north, northeast, east, southeast, east, southwest, west, and northwest directions. Both turtles and patches are allowed to use this reporter. For example, to set turtle 1's neighboring patches red we would say: 



``` ask turtle 1 [ ``` 

 ```ask neighbors [ set pcolor red ] ] ```



`neighbors4` is used to report an agentset containing only the four neighboring patches in the north, east, south, and west directions (also called cardinal directions). Both turtles and patches are allowed to use this reporter. For example, to change to yellow only the patches directly above, below, to the right of, and to the left of turtle 1, we would say: 



```ask turtle 1 [```

 ```ask neighbors4 [ set pcolor yellow ] ] ```

