`member?` can be used with **lists** or **agentsets**, but is more commonly used with lists. `member?` reports `true` if the given value or agent appears in the given list or agentset. For example, `member? 3 [12 -5 3 6 1]` would report `true`, while  `member? 5 [12 -5 3 6 1]` would report false. 



In the model example below, we have a building that represents a library and some turtles who represent patrons. While the turtles move around randomly, our library checks at each tick if there is any patron nearby. If there is a patron, our library checks if the patron is a member of the library. If the patron is a member, our library asks them to change their shape to indicate that this patron either picked or dropped a book. 