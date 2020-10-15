`or` is a primitive that is used to check if *either* of two conditions is true. Given two checks, or true-or-false statements, `or` will report **True** if 1) the first is true, 2) the second is true, or 3) both are true. It will only report **False** only if *both* of the conditions are false. For example, say you had a pig and you wanted it to eat the food on its patch, regardless if it was animal food or human food. You could model that with 



```ask pigs [ ```

 ```if animal-food-here or people-food-here [```

 ```eat] ```



Additionally, if you wanted to check more than just two conditions, you can just string together a series of `or` statements like : `if A or B or C or D [ do-something]`.



In this model, `or` is used to check if a soccer ball is within or outside of the net. Using the `check-if-miss` procedure, if the ball is outside of the boundaries of the net, we color it red, and if it is inside, we color it green. In the code, we check if the ball is too far to the right *or* too far to the left *or* too high. (In this model, the center of the world is set to be the center of the bottom edge to make the math easier.)



PS. Note that under the hood, in practice NetLogo often only has to check the first of the two conditions to see if the `or` will report true or not. Imagine we are checking two conditions, `condition1` and `condition2`. If we write `if condition1 or condition2` and `condition1` is true, regardless of whether `condition2` is true or false, the `or` will always report true, so why bother checking `condition2`. This is called "short-circuit or" and you will see it in most modern programming languages because it allows for faster code execution as well as some other benefits to advanced programmers. The takeaway for beginner programmers, however, is simpler: if you need to use `or` to combine two checks, place the less computationally expensive check first, because if it reports true, then you never have to waste the computer's time checking the expensive one.
