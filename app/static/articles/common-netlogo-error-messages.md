# A list of Common NetLogo error messages and how to fix them

&nbsp;

It is inevitable to make errors when coding. That's why it is important to develop a good vocabulary of NetLogo error messages to avoid these errors from slowing us down or spoiling the fun of agent-based modeling with NetLogo. We compiled a list of the most common NetLogo error messages below. Each entry will tell you what the error message means, suggestions to fix it, and a code example that shows both the erroneous code and the corected code.

&nbsp;

----

&nbsp;

## <p class="badge badge-netlogoerror  text-wrap text-monospace text-left"><span class="badge badge-pill badge-danger"><i class="fas fa-hand-paper"></i></span> No closing bracket for this open bracket.</p>

This error occurs when you are missing a closing bracket. Each opening bracket must have a closing bracket, and vice versa; brackets always come in pairs. To be sure each bracket has its matching bracket, you can click the bracket and its pair will be highlighted. If no other bracket is highlighted, you know you are missing one!

For example, the following code would show this error because we forgot to close the bracket of the `if` statement:

```
ask turtles [
	if size < 3 [	set size size + 1
]
```

In contrast, the following code would not show any errors:

```
ask turtles [
	if size < 3 [	set size size + 1 ]
]
```



&nbsp;

----

&nbsp;

## <p class="badge badge-netlogoerror  text-wrap text-monospace text-left"><span class="badge badge-pill badge-danger"><i class="fas fa-hand-paper"></i></span> Expected Command</p>

This error occurs when you have one too many brackets. Each opening bracket must have a closing bracket, and vice versa; brackets always come in pairs. To be sure each bracket has its matching bracket, you can click the bracket and its pair will be highlighted. The error will either state which line the extra bracket is on, or will highlight the line. To fix the error, simply delete the extra bracket.



For example, the following code would show this error because we accidentally added one too many brackets after the `if` statement:

```
ask turtles [
	if size < 3 [	set size size + 1 ]
	]
]
```

In contrast, the following code would not show any errors:

```
ask turtles [
	if size < 3 [	set size size + 1 ]
	
]
```



&nbsp;

----

&nbsp;

## <p class="badge badge-netlogoerror  text-wrap text-monospace text-left"><span class="badge badge-pill badge-danger"><i class="fas fa-hand-paper"></i></span> Nothing names [NAME] has been defined.</p>

A button will turn red if it doesn’t have a matching procedure defined in the code tab. Often, this is because the procedure has a different name than the button, or something has been misspelled. To fix this error, make sure that your button name corresponds with a procedure name. 

For example, if we had a **setup** button in our interface, the following code would cause an error because we misspelled the procedure's name:

```
to seutp
	clear-all
end
```

The following code would not show an error:

```
to setup
	clear-all
end
```



&nbsp;

This error also occurs when you are trying to use a term, keyword, or variable that has not been defined. This can also happen with a global variable, a local variable, or a turtles-own or patches-own variable. To fix this error, make sure to define your variable. Depending on the situation, you can use `[globals]`, `turtles-own`, `patches-own`, or `let` to define the variable. Once your variable has been defined, you can use it in the preceding code without an error. 

For example, the following code would show an error because we did not define the `stress-level` characteristic for turtles anywhere in our code:

```
to go
	ask turtles [if stress-level > 100 [ rest ] ]
	tick
end
```

We can solve this issue by defining the `stress-level` variable at the top of the code tab:

```
turtles-own [ stress-level ]
...
to go
	ask turtles [if stress-level > 100 [ rest ] ]
	tick
end
```



&nbsp;

Lastly, this error can happen when you have accidentally misspelled something, usually a variable name or primitive. For example, writing `set-xy` instead of `setxy`, or `move-to` instead of `moveto` will get this error. Always check for typos!

&nbsp;

----

&nbsp;

## <p class="badge badge-netlogoerror  text-wrap text-monospace text-left"><span class="badge badge-pill badge-danger"><i class="fas fa-hand-paper"></i></span> END expected.</p>

This error occurs when we forget to add `end` to the end a procedure. NetLogo will either state which line the `end` is missing from, or will highlight the line in code. Because each procedure must conclude with the `end` primitive, simply add it after your procedure’s code to fix the error.

For example, the code below would show this error:

```
to go
   ask turtles [ forward 1 ]
```

While the following code would work just fine:

```
to go
	ask turtles [ forward 1 ]
end
```



&nbsp;

----

&nbsp;

## <p class="badge badge-netlogoerror  text-wrap text-monospace text-left"><span class="badge badge-pill badge-danger"><i class="fas fa-hand-paper"></i></span> OF expected this input to be a reporter block, but got a number instead. </p>

This error occurs when a reporter preceding the `of` primitive is not enclosed in brackets (`[]`). You can refer to the <a href="/primitive/of">of item of this dictionary</a> to learn more about how to use the `of` primitive correctly. 

For example, the following code would show this error because the `size` reporter that comes before the `of turtles` statement is not enclosed within brackets (`[]`):

```
ask turtles [
	if mean size of turtles > size [ set size size + 1 ]
]
```

To fix the error, simply add brackets around the reporter you want to access from the agentset, like:

```
ask turtles [
	if mean [size] of turtles > size [set size size + 1]
]
```



&nbsp;

----

&nbsp;

## <p class="badge badge-netlogoerror  text-wrap text-monospace text-left"><span class="badge badge-pill badge-danger"><i class="fas fa-hand-paper"></i></span> WITH expected this input to be a TRUE/FALSE block, but got a number instead</p>

This error occurs when we forget to add brackets around the true/false statement that follows the `with` primitive. You can refer to the <a href="/primitive/with">with item of this dictionary</a> to learn more about how to use the `of` primitive correctly. 

For example, the following code would show this error because the `size > 1` statement that comes after the `with` primitive is not enclosed within brackets:

```
ask turtles with size > 1 [
	forward 1
]
```


To fix the error, we can simply add brackets around the reporter as shown below:

```
ask turtles with [ size > 1 ] [
	forward 1
]
```

&nbsp;

----

&nbsp;

## <p class="badge badge-netlogoerror  text-wrap text-monospace text-left"><span class="badge badge-pill badge-danger"><i class="fas fa-hand-paper"></i></span> ASK expected this input to be an agent or agentset, but got NOBODY instead.</p>

This error occurs when we try to access an agent that does not exist. This may happen because the agent may have died, or may have never existed in the first place.  

For example, the following code would show an error because our model does not have any green turtles:

```
to setup
	clear-all
	create-turtles [ set color one-of [red blue] ]
	ask turtles with [color = green] [ forward 1]
end
```

There are two hypothetical fixes for this error. We either need to make some of our turtles green by writing the following code:

```
to setup
	clear-all
	create-turtles [ set color one-of [red blue green] ]
	ask turtles with [color = green] [ forward 1]
end
```

Or we need to change our ask statement and use either red or blue in the conditional as follows:

```
to setup
	clear-all
	create-turtles [ set color one-of [red blue green] ]
	ask turtles with [color = red] [ forward 1]
end
```

Note that a similar error may be shown for the same reason when using other primitives such as `one-of`, `in-radius`, `patch-ahead`, and `n-of`.

&nbsp;

----

&nbsp;

## <p class="badge badge-netlogoerror  text-wrap text-monospace text-left"><span class="badge badge-pill badge-danger"><i class="fas fa-hand-paper"></i></span> ... expected this input to be an ... here, but got a ... instead</p>

This is a more generic error that means you have a syntax error such as  giving a primitive the wrong type of input (a list instead of a number, an agentset instead of a reporter, etc). Because each primitive’s syntax is different, it’s a good idea to check the exact syntax in the <a href="/dictionary">dictionary</a>. 

For example, the following code would show this error because the `face` primitive requests just one agent, while the `neighbors` primitive reports 8 agents.

```
ask turtles [
	face neighbors
]
```

The following code would not show an error because the `one-of` primitive would report just one randomly picked neighbor to our `face` primitive:

```
ask turtles [
	face one-of neighbors
]
```



&nbsp;

----

&nbsp;

## <p class="badge badge-netlogoerror  text-wrap text-monospace text-left"><span class="badge badge-pill badge-danger"><i class="fas fa-hand-paper"></i></span> You can't use ... in a turtle context, because ... is observer only.</p>

This error occurs when we are trying to use a primitive in a context it is not meant for. Turtles have some primitives that are exclusive to them; there are also patch-specific, link-specific, and observer-specific primitives. 

For example, the following code would show this error because the `create-turtles` primitive is meant to be only used within the observer context. 

```
ask patches [
	create-turtles 1
]
```

In such circumstances, NetLogo has specific primitives. For example, patches can create new primitives using the `sprout` primitive, so the following code would not show an error:

```
ask patches [
	sprout 1
]
```

In addition, you may have simp forgotten to use the primitive within an `ask turtles [...]` or `ask patches [...]` context. Check the NetLogo Dictionary to find which agent types a primitive is compatible with. You may need to use a similar primitive that is used by a different type of agent. (`create-turtles`, `hatch`, and `sprout` all create new turtles, but are used by different agents.)

This error applies to other types of agent types such as links, patches, and observer.
Some examples are: 



<ul>
  <li>
  	<p class="badge badge-netlogoerror  text-wrap text-monospace text-left"><span class="badge badge-pill badge-danger"><i class="fas fa-hand-paper"></i></span> You can't use SETXY in a patch context, because SETXY is turtle only.</p>
  </li>
  <li>
    <p class="badge badge-netlogoerror  text-wrap text-monospace text-left"><span class="badge badge-pill badge-danger"><i class="fas fa-hand-paper"></i></span> You can't use DIE in a patch context, because DIE is turtle/link only.</p>
  </li>
  <li>
    <p class="badge badge-netlogoerror  text-wrap text-monospace text-left"><span class="badge badge-pill badge-danger"><i class="fas fa-hand-paper"></i></span> You can't use CREATE-TURTLES in a turtle context, because CREATE-TURTLES is observer only.</p>
  </li>
</ul>

&nbsp;

---

&nbsp;

## <p class="badge badge-netlogoerror  text-wrap text-monospace text-left"><span class="badge badge-pill badge-danger"><i class="fas fa-hand-paper"></i></span> Keyword expected.</p>

This error occurs when our code is not contained within a procedure. In the Code Tab, all code must be written within a procedure, except for defining global variables, breeds, turtle variables or patch variables. To fix this error, simply enclose your code within a procedure, beginning with `to` and ending with `end`. 

For example, the following code would show this error:

```
globals [stress-level]
clear-all
ask turtles [
	set stress-level 0
]
```

But the following code would work just fine:

```
globals [stress-level]
to setup
	clear-all
	ask turtles [
		set stress-level 0
	]
end
```

