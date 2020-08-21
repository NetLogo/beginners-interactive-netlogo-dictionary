Links are a tool in NetLogo to represent connections between turtles. A link itself is just a connection between any two (distinct) turtles with some information attached. Once created, we can use links to reference connected turtles, for example, sending commands to all the turtles connected to a given turtle. With just this simple tool of connections between turtles, we can represent very sophisticated relationships between turtles such as family trees, "friend" relationships on social media (commonly referred to as a "social graph"), or even road maps for navigation software like google maps or waze.

In the same way that you can refer to all of the turtles in the world with the keyword `turtles`, you can refer to all of the links in the world with the keyword `links`. You can use this keyword to, for example, change the color or thickness of a link's visual representation, like so: `ask links [set color grey]`

While even basic uses of links can be quite powerful, there area few optional extra layers of complexity that can be applied to links if needed, specifically "directed" links and link properties.

First, "directed" links are exactly like normal links except that there is an inherent direction or order embedded within them. For example, in a road map, a one-way street might be represented as a directed link because you can travel from one end to the other, but not the other way. 

Second, link properties are just variables that are "owned" by each link in the same way that a turtle or a patch can "own" a variable. Each link has its own distinct copy of a link-owned variable.

In this example, links are used to represent air travel routes between four cities, Chicago, New York, and Boston, across their six major airports, Chicago Midway (MDW), Chicago O'Hare (ORD), New York John F. Kennedy (JFK), New York LaGuardia (LGA), Boston Logan (BOS), and Seattle-Tacoma International Airport (SEA). By changing the "airport-choice" picker, you can see which airports are connected to which, in other words, what airports you can fly to directly from which.
