`mod` is a mathematics primitive that completes the **modulo operation**, which takes two numbers, divides them, and returns the *remainder*. For example, `17 mod 7` would report 3 because $17 = 2 * 7 + 3$. 



`mod` is very useful in some interesting NetLogo modeling applications such as creating grids. For example, the following code would create a checkerboard pattern like a chess board:



```
ask patches [
  if (pxcor + pycor) mod 2 = 1 [
    set pcolor white
  ] 
]
```





Things to keep in mind when using `mod`: 

* `mod` works with floating point numbers, too. For example, `5 mod 1.5` would report 0.5.
* Using `mod` with negative numbers may be counterintuitive. For example, while `5 mod 3` would report 2, `5 mod -3` would report -1.



In the model example below, we use `mod` to create a maze in which 3 mice compete for the pieces of food scattered around randomly. Without `mod`, creating this maze would be extremely tedious.