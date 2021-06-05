# What is a primitive?

&nbsp;

*Primitives* are the building blocks in NetLogo programming. They are the simplest and smallest pieces of pre-defined NetLogo keywords that can be used to put together longer algorithms to construct complex agent-based models. As this Beginner's Interactive NetLogo Dictionary is all about some of the most commonly used primitives in NetLogo, it is helpful to understand what is a primitive and what is not a primitive.



Most primitives are one word terms (e.g., `forward`, `to`) except some multi-word ones (e.g., `clear-all`, `scale-color`, `create-links-with`) and some arithmetic operators  (e.g., `>=`, `+`,`/`).



Some examples to NetLogo primitives are:

```
forward
color
turtles-own
+ / - 
mod
nobody
ifelse
globals
neighbors
```



Notice how each primitive has a specific color. These colors give us hints on the function of each primitive. You can [click here to learn more about these color codes.](/article/code-colors-in-netlogo.html)



Each primitive requires a specific structure to properly function in code, which is called ***the syntax of the primitive***. Some primitives *just work*, while others require us to provide more information. For example, the `clear-all` primitive just works. Wherever we write `clear-all` in our code, everything in our model is wiped out. Similarly, the `max-pxcor` primitive just works. Wherever we write `max-pxcor` in our code, it reports the `pxcor` of the rightmost patches in our model. On the other hand, the `forward` primitive requires us to provide it with a number such as `forward 5` or `forward 0.375`. If we wrote just `forward` in our code, NetLogo would show an error as follows: <span class="badge badge-netlogoerror  text-wrap text-monospace text-left"><span class="badge badge-pill badge-danger"><i class="fas fa-hand-paper"></i></span> FORWARD expected 1 input, a number.</span>



Some primitives may require additional information to be provided after writing the keyword, while others may require information before writing the keyword. For example, the `facexy` primitive requires two numbers as x and y coordinates after the keyword such as `facexy -3 5`. On the other hand, the `in-radius` primitive requires us to provide an agentset before it and a number after it such as `turtles in-radius 3`.



&nbsp;



[<i class="fas fa-link"></i>  Click here to find a list of all primitives that are in this Beginner's Dictionary](../dictionary.html)



[<i class="fas fa-link"></i>  Click here to find an exhaustive list of all NetLogo primitives](http://ccl.northwestern.edu/netlogo/docs/dictionary.html) 

&nbsp;

Lastly, you may be wondering: "*If all of the examples above are primitives, what is not a primitive in NetLogo programming?*" There are multiple ways for us to extend the vocabulary of our models by defining:

* New global variables using the `globals` primitive such as `globals [ temperature ]`.
* New global variables by creating interface elements such as sliders.
* New local variables using the `let` primitive such as `let target one-of other turtles`.
* New agent characteristics using `turtles-own`, `patches-own`, and `links-own` primitives such as `turtles-own [ energy ]`.



For example, let's consider the following piece of code:

```
globals [ temperature ]
turtles-own [ energy ]

to setup
	clear-all
	create-turtles 100 [
		set energy random 10
	]
	set temperature 40 + random 50
	reset-ticks
end
to go
	ask turtles [
		forward 1
		ifelse temperature > 80 [
			set energy energy - 2
		][
			set energy energy - 1
		]
	]
	tick
end
```



In this code, we create some turtles in the *setup procedure* and make the turtles move around the world in the *go procedure*. In addition, we set a random temperature every time the *setup procedure runs*; if the temperature is higher than 80 degrees, our turtles use more energy every time they move forward. The following pieces of this code are primitives:

```
globals
turtles-own
to
end
clear-all
create-turtles
set
random
reset-ticks
ask
turtles
forward
ifelse
>
-
tick
```

But the following pieces are <u>not</u> primitives:

```
temperature
energy
```

Instead, these are custom *variables* that we defined for different purposes.