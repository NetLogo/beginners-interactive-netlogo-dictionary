### **let** variable-name initial-value
`Let` is used to create a new **local variable** and set its value. A local variable, unlike a global variable, can only be used by the code that comes *after* its declaration, and only exists within the enclosing brackets `[ ]` it was created in. If `let` is used to create a variable that is not within any brackets, it only exists within that procedure. 

For example, 

``` 
let my-blue-friends turtles with [ color = blue and shape = “person” ] 
ask my-blue-friends [ forward 1 ]
```

 creates a new variable called `my-blue-friends` and sets its value to all the blue and person-shaped turtles. Then, asking `my-blue-friends` to move forward moves all blue person-shaped turtles forward. To change the value of the variable after creating it, use `set`. 