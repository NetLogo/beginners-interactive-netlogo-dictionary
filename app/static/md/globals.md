`globals` is a primitive that we use to define custom *global variables* in NetLogo. A global variable is a variable that has the same value for all the agents in the model accross all procedures. You can define your custom global variables by writing  `globals` followed by brackets `[]`.



```
globals [
	temperature
	oil-price
	usd-eur-exchange-rate
]
```



Once you define a global variable, you can then use the `set` primitive to change its value:



```
set usd-eur-exchange-rate 0.85
set temperature 36
```



And use its name to access its value in your code just like any other variable:



```
if oil-price < 1.5 and usd-eur-exchange-rate < 0.8 [
	buy-oil
]
```



Things to keep in mind when using `globals`: 

* When you create an interface element such as a *slider*, *switch*, or *chooser*, its name automatically becomes a global variable and you do not need to define it within the `globals` primitive. 
* You cannot have two global variables with the same name.
* You cannot start a variable name with a number. For example, the following code would show an error `globals [1st-offer]`.
* You should always define your global variables in the beginning of your NetLogo code.
* If you would like to create a variable that is only needed temporarily and within just one specific procedure, you should use the `let` primitive instead.
* If you need a variable that has a different value for each turtle, each patch, or each link, you should use one of the following primitives: `turtles-own`, `patches-own`,`links-own`.



In the model example below, we have some brown patches that represent the earth and some green patches that represent berries. We also have five turtles that represent the people who pick the berries. We use a global variable to keep track of the total number of the berries that are collected by all the people in the model. In the `setup` procedure, we set it to 0, and then in the `go` procedure, each time a person grabs a berry (turns a patch from green to brown), we increment the `berries-picked` global variable by one. We check the value of this global variable at each tick. If our pickers picked 60 or more berries, we stop the model. We also show the value of this variable through a monitor on the model's interface.