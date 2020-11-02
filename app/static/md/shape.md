`shape` is a turtle and link variable that represents the shape of an agent. New turtles and links are created with the default corresponding shapes, and can be changed using `set shape “shape-name”` format within an `ask` context to change turtles’ or links’ shapes. You can also use `shape` as a reporter, like any other agent characteristics, such as 

```
ask turtles [ 
if shape = “rabbit” [ 
forward 1  
]
 ] 
```
**Note** you must quotation marks (“”) for the shapes.

To view the list of available shapes in NetLogo, click on the Tools menu and choose the “Turtle Shapes Editor” or the “Link Shapes Editor” options. Each new NetLogo model comes pre-loaded with a small set of shapes (e.g., sheep, turtle, car, square) that you can directly use in your code. For example, the following code would work in any new NetLogo model: `ask turtles [set shape "person"]` but the following code would throw an error: `ask turtles [ set shape “person lumberjack”]`. You can use the “Import from library” option in the editor to find an extensive list of shapes that are used in other models. Additionally, you can create your own shapes in the editor.



In the model below, there are sheep and wolves wandering around. Only the sheep eat grass and not wolves, so we can distinguish between them by using `shape` to narrow down the agentset to only `turtles with [ shape = "sheep" ]` . 