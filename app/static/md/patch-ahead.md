`patch-ahead` reports the single patch that is the given distance *ahead* of this turtle. You can think of it as the turtle looking at a patch in front of it. The syntax of `patch-ahead` is 



``patch-ahead distance ``



The distance can be an integer or a decimal number, and is how far away the patch that `patch-ahead` reports will be.  For example, to turn the patch 3 units in front of a turtle green, we would say: 



```
ask patch-ahead 4 [ set pcolor green ] 
```


**Note**: This reporter will report `nobody` if the patch does not exist (i.e. if the patch is outside the given coordinates of NetLogo). In the model below, we want the car to drive only on gray patches and not red ones. So we use `patch-ahead` to make the car stop, if the patch ahead is red.

