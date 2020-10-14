`Let` is used to create a new **local variable** and set its value. A **local variable** is a variable that only exists within the brackets `[...]` or procedure it was created in, unlike a global variable. It can only be used in the code that comes *after* its declaration, and takes the form of: 



```let variable-name initial-value```



For example, to create a new local variable called `my-blue-friends` and to set its value to all the blue person-shaped turtles, we would say:



``` 
let my-blue-friends turtles with [ color = blue and shape = “person” ] 
ask my-blue-friends [ forward 1 ]
```



 Then, asking `my-blue-friends` to move forward moves all blue person-shaped turtles forward. To change the value of the variable after creating it, use `set`. 

