`ifelse-value` is a primitive that allows the user to quickly and concisely check a number of conditions and execute different code depending on the results. There is nothing that you can do with `ifelse-value` that you could not already do with a series of `if` or `ifelse` statements, but the strength of `ifelse-value` is in its syntactic efficiency. For example, say you wanted to check which of the four quadrants of the world a given turtle is in. Compared to the `if` version, the `ifelse-value` one is arguably much cleaner.

```
to-report report-quadrant-if
  if xcor > 0 and ycor > 0 [
	report 1
  ]
  if xcor < 0 and ycor > 0 [
	report 2
  ]
  if xcor < 0 and ycor < 0 [
	report 3
  ]
  if xcor > 0 and ycor < 0 [
	report 4
  ]  
end

to-report report-quadrant-ifelse-value
  report (ifelse-value
	xcor > 0 and ycor > 0 [1]
	xcor < 0 and ycor > 0 [2]
	xcor < 0 and ycor < 0 [3]
                      	[4] ; else
  )
end
```

One important thing to note about using `ifelse-value` is that you must wrap the whole thing with parentheses if you use more than one condition. In addition, know that you can omit the final condition and the last set of brackets that you write will be treated like an `else` statement, specifying what will happen if none of the conditions are true.

The following example shows a place where `ifelse-value` can be used to make code more succinct and, one you are familiar, more readable: choosing one of six die icons for a six
