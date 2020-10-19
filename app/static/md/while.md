`While` begins a loop that executes a **block of commands**, as long as a given **reporter** returns **True**. If the reporter reports **False** , the loop is exited.  It takes the form:



 ```while [ reporter ] [ commands ]```



For example, to make turtle 0 keep moving forward until it comes to a patch that has no other turtles on it, we could say:

```
ask turtle 0 [ 
    while [ any? Other turtles-here ] [ 
    	forward 1] ]
```


Note: while loops and other loops are not used often in NetLogo models. In the model below, we use a `while` loop to make a turtle draw a square.

