`breed` is a special primitive that can only be placed in the top of a netlogo code tab. Using `breed`, you can define custom kinds or *breeds* of turtles. It is most useful when we have different groups of turtles that each need to have their own behavior and we want to have an easy way to reference each group within your code.  



To create a new type of turtle, we use the `breed` primitive followed by an opening square bracket `[`, the plural version of the breed, a space, the singular version of the breed, and a closing square bracket `]` . For example, `breed [dogs dog]`, `breed [buildings building]`, and `breed [cars car]`. 



NetLogo requires both the plural and singular versions of a breed because: 

* Different spoken languages may have different conventions for plural and singular words
* Some things may have non-conventional forms for plural and singular such as `breed [cacti cactus]`, `breed [mice mouse]`, or `breed [leaves leaf]`.



`breed` is also special in that it creates other related commands that can be used later on in your code. For example, if we create a **dogs** breed, we can use primitives such as `create-dogs`, `dogs-here`, `hatch-dogs`, `sprout-dogs` and so on. 



We can create as many breeds as you wish in your model. We can also use the `link-breed` primitive to create different groups of links.



In the example model example below, we use `breed` to create two types of turtles with very different behavior: trees and lumberjacks. Trees just sit there, while lumberjacks wander around and cut down the trees if they happen upon a patch with a tree. While it wouldn't be too difficult to create a version of this model without `breed` using custom turtle properties defined with the `turtles-own` primitive, `breed` allows us to easily differentiate between different types of turtles. Using breeds also makes it easier to read the code.