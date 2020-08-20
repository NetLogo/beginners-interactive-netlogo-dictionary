`Mean` reports the mean, or average, of the numeric values in a given list. (The mean is calculated by summing all the values, then dividing by the total number of values.) For example, 
```
ask turtles with [ size >= mean [ size ] of turtles ] [ 
    set color red ]
```
would turn all the turtles who are **larger than average** red. 