`globals` keeps track of information that should be common to the entire model. Global variables are always declared at the very top of your code, and its syntax is:



``` globals [ variable-name ] ```



In the same way that the value of a slider can be accessed anywhere in NetLogo code, any bit of your code can both set (using the `set` command) and read (by typing the name of the global) the value of a global. This fact makes globals useful for defining model-wide constants that you don't want the user to be able to change from a slider. It also makes them useful for keeping track of variable model-wide information that any agent can modify, for instance, the total accumulated volume of transactions in an economy model or the number of times that a predator caught their prey in an ecological model.

`Update: when you create interface elements such as sliders, switchers and choosers, their values are stored in a global variable.`

In this example, a global is used to keep track of a model-wide variable, the total patches of grass eaten by all the 20 sheep in the model. In the `setup` procedure, we set it to 0, and then in the `go` procedure, each time a sheep eats a patch of grass, we increment it by one by setting its value to what its value used to be plus one, i.e. `set total-food-eaten total-food-eaten + 1`.