`repeat` allows you to execute any set of commands *n* amount of times. It takes the form of:



``` repeat n [ commands ]```



For example, if you ask a turtle to  `repeat 10 [ forward 1 ]` it will execute those commands 10 times back-to-back-to-back, which will result in the turtle moving forward 10 units forward.  You can use `repeat` in any context as long as it is within an ask command or outside an ask command. `repeat` can come especially handy when drawing shapes. For example, the following code would make the turtles draw a square:

``` 
 ask turtles [ 
  pen-down
  	repeat 4 [ 
    forward 10
    right 90
  ]
]
```

