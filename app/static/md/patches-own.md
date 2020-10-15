`Patches-own` defines variables that belong exclusively to the patches of a model. (See its counterpart `turtles-own` for defining turtles’ variables.) The variables are usually a trait or characteristic of the patches; for example if your patches are representing soil in your model, you might use `patches-own [ nutrients ] `.  It has the form:



 ```patches-own [ variable1 variable2 ... ]```



and can include multiple variables, as long as they are within the brackets. Like global variables and other agent variables, it must be defined at the top of your code, before any procedure definitions. **Note** : Patch variables can also be accessed by a turtle that is standing on that patch.



In the model below, we are modeling a garden with flowers. Flowers will grow depending on how much nutrients its patch of soil has, so we create a patches variable called `nutrients` using `patches-own`.

