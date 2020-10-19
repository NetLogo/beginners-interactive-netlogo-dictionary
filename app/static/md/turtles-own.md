`Turtles-own` defines variables that belong to all turtles in a model. The variables are usually a trait or aspect specific to the turtle, like *is-hungry?* or *energy*. Its syntax is :



``` turtles-own [ variable1 variable2 ... ]```



Like global variables and other agent variables, it must be defined at the top of your code, before any procedure definitions. You can define one variable or multiple, but they must all be within the brackets. 



If you have defined multiple breeds of turtles, `turtles-own` will apply the variable to all breeds. However, you can define a variable for a specific breed by using `<breed>-own`, where **<breed>** is the name of your breed. For example, if you have already defined a breed of turtles by `breed [birds bird]`, you can create a variable for only birds by using `birds-own [wing-size]`. 



In the model below, cars are driving with a certain amount of gas in their tanks. We use `turtles-own` to define the variable `gas`, which represents how much gas a car has. Later, we use the `gas` variable to determine if a car can keep driving or not.