`links` are a special category of agents (like turtles and patches) in NetLogo to represent connections between turtles. A link itself is just a connection between any two (distinct) turtles with some information attached. With just this simple tool of connections between turtles, we can represent very sophisticated relationships between turtles such as family trees, "friend" relationships on social media (commonly referred to as a "social graph"), or even road maps for navigation software like Google Maps or Waze.



You can create new links between turtles using the `create-link-with ` and `create-links-with ` primitives. Notice that `create-link-with ` creates only one link between two turtles and it requires a specific turtle, while  `create-links-with ` creates multiple turtles at once and requires an agentset.



```
ask turtles [
	create-link with one-of other turtles
	create-links-with other turtles with [color = green]
]
```



Things to keep in mind when using `links`: 

* NetLogo has a *Link Shapes Editor* under the *Tools* menu. You can use this editor to design custom link shapes such as dotted lines, multiple parallel lines, or curved lines.
* In the same way that you can refer to all of the turtles in the world with the keyword `turtles`, you can refer to all of the links in the world with the keyword `links`. For example, you can use this keyword to change the color or thickness of links' visual representation such as `ask links [set color grey]`.
* You can create custom link characteristics using the `links-own` primitive (similar to `turtles-own` and `patches-own`). For example, if you are creating a model of rural internet infrastructure, your links may have a *bandwidth* characteristic: `links-own [ bandwidth ]`.
* You can create custom link breeds with the `undirected-link-breed` primitive. For example, if your model is going to have two types of links such as `cables` and `satellite-connection`, you can create separate breeds such as `undirected-link-breed [cables cable]` and `undirected-link-breed [satellite-connections satellite-connection]` .



In the model example below, we have a computer network represented with a server at the center and other terminal computers arranged in a circle layout. Each computer is connected to the server with a gray dashed link that represents a passive connection. At each tick, our server initiates an active connection to a random terminal. We represent the active connections with a green link. We also use two different link shapes for active connections: a simple straight link indicating an information retrieval and a curved three-line connection indicating a file download. 