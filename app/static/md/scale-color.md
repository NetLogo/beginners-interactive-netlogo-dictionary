`scale-color` is a primitive that reports a shade of a color proportional to the value of a given number. For example, if we wanted to create a traffic model in which cars with fuller tanks were brighter than those with emptier tanks, we would write the following code:



```
ask cars [
	set color scale-color white tank-level 0 100
]
```



Or if we wanted to model a flock of sheep where more lush patches of grass were brighter than those that have already been eaten, we would write the following code:



```
ask patches [
	set pcolor scale-color green lushness 0 100
]
```



Things to keep in mind when using `scale-color`: 

* The syntax of `scale-color` can be hard to remember. It is as follows `scale-color base_color exact_point lowest_value highest_value`. 
* You can think of the *base_color* value as the middle point in the provided range. For example, if we wrote `scale-color green 50 0 100`, we would get exactly green.
* Don't forget that the desired base color comes first, then comes the exact value ,  `number` is the value you wish to scale by (usually a turtle or patch variable), and `range1` and `range2` are parameters for describing the minimum and maximum  values of `number`. If `range1` is less than `range2`, then larger numbers result in brighter colors, but if `range2` is less than `range` , larger numbers result in darker colors. If the `number` is outside of the range, then either the lightest or darkest shade is chosen. 
* By default, `scale-color` produces darker shades for smaller values and lighter shades for larger values. However, it is possible to reverse this by writing the maximum value as `range1` and minimum value as `range2` such as `scale-color lushness 50 100 0`. We are doing exactly this in the model example below for the nutrition level of each patch.



In the model example below, we use `scale-color` to adjust the color of each patch to reflect its nutrition level (1 being lowest, 5 being highest). Each time our farmer moves onto a patch, it checks the nutrition level there. If the nutrition level is above 3, the farmer plants a vegetable. We also color the vegetables using `scale-color` based on the nutrition level of its patch. The vegetables that get more nutrition have a brighter green color.