`scale-color` is a primitive that reports a shade of a color proportional to the value of a given number. For example, in a traffic model, one might use `scale-color` to color cars with a full tank of gas brighter than those with an emptier tank of gas, or, in a model of a flock of sheep, color more lush patches of grass brighter than those that have already been eaten. 

In practice, you use `scale-color` like so:



 ```scale-color color number range1 range2``` 



where `color` is the desired base hue (red, blue, green, etc.), `number` is the value you wish to scale by (usually a turtle or patch variable), and `range1` and `range2` are parameters for describing the minimum and maximum  values of `number`. If `range1` is less than `range2`, then larger numbers result in brighter colors, but if `range2` is less than `range` , larger numbers result in darker colors. If the `number` is outside of the range, then either the lightest or darkest shade is chosen. 

In this model, `scale-color` is used to model cell-tower signal strength. Patches closer to the cell towers have better signal strength and are therefore colored brighter than those too far away from a tower to get any signal. 
