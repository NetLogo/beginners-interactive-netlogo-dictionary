`neighbors` is used to report an agentset containing the agent's eight surrounding patches in the north, northeast, east, southeast, east, southwest, west, and northwest directions. Both turtles and patches are allowed to use this reporter. For example, to set turtle 1's neighboring patches red we would say: 



``` ask turtle 1 [ ``` 

 ```ask neighbors [ set pcolor red ] ] ```



`neighbors4` is used to report an agentset containing only the four neighboring patches in the north, east, south, and west directions (also called cardinal directions). Both turtles and patches are allowed to use this reporter. For example, to change to yellow only the patches directly above, below, to the right of, and to the left of turtle 1, we would say: 



```ask turtle 1 [```

 ```ask neighbors4 [ set pcolor yellow ] ] ```



In the model below, there is a fire spreading in a forest. A patch on fire will spread to its neighboring patches that contain trees. Depending on if the switch is on `neighbors` or `neighbors4`, the fire will spread to all neighboring trees or to only trees in the cardinal directions, respectively. 