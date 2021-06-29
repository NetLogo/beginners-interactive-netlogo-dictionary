`ifelse-value` is a primitive that allows us to quickly and concisely check a number of conditions and pick a value accordingly. This primitive helps us not write many consecutive `if` or `ifelse` statements. 



For example, if we wanted to check which of the four quadrants of the world a given turtle is in, our first option is to write a code as follows:

```
to-report where-am-i
  if xcor > 0 and ycor > 0 [
    	report "upper-right"
  ]
  if xcor < 0 and ycor > 0 [
    	report "upper-left"
  ]
  if xcor < 0 and ycor < 0 [
    	report "lower-left"
  ]
  if xcor > 0 and ycor < 0 [
    	report "lower-right"
  ]  
end
```



However, this many `if` statements make it hard to read the code. Instead, we can use the `ifelse-value` primitive as follows to make a much more concise code:



```
to-report where-am-i
  report (ifelse-value
    	xcor > 0 and ycor > 0 ["upper-right"]
    	xcor < 0 and ycor > 0 ["upper-left"]
    	xcor < 0 and ycor < 0 ["lower-left"]
    	["lower-right"] ; if none of the conditions are true
  )
end
```



Things to keep in mind when using `ifelse-value`: 

* You should wrap the whole `ifelse-value` within parentheses `()`.
* You can provide a last set of commands within brackets but without any preceding condition(s). This last set of commands will be treated like an `else` statement, specifying what will happen if none of the conditions are true. You can also omit this final condition.



In the model example below, we have six dice shapes. Every time we click the *roll-all* button, each turtle picks a random number between 1 to 6. Then, we use the `ifelse-value` primitive to pick the correct turtle shape to represent the corresponding die value.