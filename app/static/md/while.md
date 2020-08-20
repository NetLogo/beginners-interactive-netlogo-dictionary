### **while** [ reporter ] [ commands ]
`While` begins a loop that executes a **block of commands**, as long as a given **reporter** returns **True**. If the reporter reports **False** , the loop is exited.  For example, in 
```
ask turtle 0 [ 
    while [ any? Other turtles-here ] [ forward 1] ]
```
**turtle 0** would keep moving forward until it comes to a patch that has no other turtles on it, then it would stop. 

Note: while loops and other loops are not used often in NetLogo models. 
