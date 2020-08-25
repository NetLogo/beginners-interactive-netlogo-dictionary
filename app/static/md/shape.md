`shape` is a turtle and link variable that represents the shape of each agent. New turtles and links are created with the default corresponding shapes unless a different shape has been specified using the syntax “set-default-shape”. Otherwise, you need to use the `set shape “shape-name”` format within an `ask` context to change turtles’ or links’ shapes. You can also use `shape` as a reporter, like any other agent characteristics, such as 

```
ask turtles [ 
if shape = “rabbit” [ 
forward 1  
]
 ] 
```
**Notice** that you must quotation marks (“”) for the shapes.

To view the list of available shapes in NetLogo, click on the Tools menu and choose the “Turtle Shapes Editor” or the “Link Shapes Editor” options. Each new NetLogo model comes pre-loaded with a small set of shapes (e.g., sheep, turtle, car, square) that you can directly use in your code. For example, the following code would work in any new NetLogo model: `ask turtles [set shape "person"]` but the following code would throw an error: `ask turtles [ set shape “person lumberjack”]`. 

You can use the “Import from library” option in the editor to find an extensive list of shapes that are used in other models. Additionally, you can create your own shapes in the editor.
