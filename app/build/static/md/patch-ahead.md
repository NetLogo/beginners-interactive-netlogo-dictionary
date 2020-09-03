
`patch-ahead` reports the single patch that is the given distance *ahead* of this turtle. *Ahead* in this context means towards the turtle’s current heading. You can think of it as the turtle looking at a patch in front of it. The syntax of this reporter is `patch-ahead *insert distance here*`. The distance can be an integer or a decimal number (e.g., 1, 3, 2.5, 5.5).  For example: 
```
ask patch-ahead 1 [ set pcolor green ] 
```
This line turns the patch 1 unit in front of this turtle **green**.

**Note**: This reporter will report `nobody` if the patch does not exist (i.e. if the patch is outside the given coordinates of NetLogo).
