The primitive `mod` completes the **modulo operation**, which takes two numbers, divides them, and returns the remainder. The remainder of `(number1 / number2)` is the value reported. Its syntax is:



``` number1 mod number2 ```



For example, `show 17 mod 4` would report 1, because 17 divided by 4 has a quotient of 4 and a remainder of 1. `Show 9 mod 3` would report 0, because 9 divided by 3 leaves a remainder of 0.



In the model below, we use `mod` to do something intermittently. When we say `if ticks mod 10 = 1`, that makes the action happen every 10 ticks. 