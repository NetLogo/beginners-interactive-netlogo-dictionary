# A list of Common NetLogo error messages and how to fix them



**“No closing bracket for this open bracket.”**
This error occurs when you are missing a closing bracket. Each opening bracket must have a closing bracket, and vice versa; brackets always come in pairs. To be sure each bracket has its matching bracket, you can click the bracket and its pair will be highlighted. If no other bracket is highlighted, you know you are missing one!

#### <span class="bg-warning"> <i class="fas fa-hand-paper text-danger"></i> “Expected command.”</span>
This error occurs when you have one too many brackets. Each opening bracket must have a closing bracket, and vice versa; brackets always come in pairs. To be sure each bracket has its matching bracket, you can click the bracket and its pair will be highlighted. The error will either state which line the extra bracket is on, or will highlight the line. To fix the error, simply delete the extra bracket.

**If a button turns red and you see a “Nothing named [word] has been defined” error when you click the button**
A button will turn red if it doesn’t have a matching procedure defined in the code tab. Often, this is because the procedure has a different name than the button, or something has been misspelled. To fix this error, make sure that your button name corresponds with a procedure name.

**“END expected”**
This error occurs when you have forgotten to add `end` to the end of your procedure. NetLogo will either state which line the `end` is missing from, or will highlight the line in code. Because each procedure must conclude in `end`, simply add it after your procedure’s code to fix the error.
For example, the code below would get this error:

```To go   ```

```   Ask turtles  [  ```

```   	Forward 1   ] ```

While this code would fix the error:

```To go   ```

```Ask turtles [  ```

```   Forward 1   ]```

```end ```



**“Nothing named [word] has been defined”**
This error occurs when you are trying to use a term, keyword, or variable that has not been defined. This error can happen on a global variable, a local variable, or a turtles-own or patches-own variable. To fix this error, make sure to define your variable. Depending on the situation, you can use `[globals]`, `turtles-own`, `patches-own`, or `let` to define the variable. Once your variable has been defined, you can use it in the preceding code without an error. 
This error can also happen when you have accidentally misspelled something, usually a variable name or primitive. For example, writing `set-xy` instead of `setxy`, or `move-to` instead of `moveto` will get this error. Always check for typos!


**“OF expected this input to be a reporter block, but got anything instead”**
This error occurs when the reporter preceding `of` is not enclosed in brackets. The syntax of `of` must be : [ reporter ] of agent/agentset. For example, the following code would get the error:
Ask turtles [ Show energy of turtles]
To fix the error, simply add brackets around the reporter you want to access from the agentset, like:

```ask turtles [ ```

```show [ energy ] of turtles ] ```



**“WITH expected this input to be a TRUE/FALSE block, but got a number or list instead”**
This error occurs when you have forgotten to add brackets around the boolean characteristic following `with`. `with` must have the following syntax: `agentset with [ desired-characteristic ]`. `with` is used to narrow down an agentset by a specific characteristic. For example, the following code will get the error:
```ask turtles with size > 1 [ Fd 1 ] ```
Because of the missing brackets. To fix the error, simply add brackets around the reporter:
```ask turtles with [ size > 1 ] [ Fd 1 ]```

**“ASK expected input to be an agent or agentset but got NOBODY instead”**
This error occurs when you try to access an agent that does not exist. This could have happened because the agent died, or never existed in the first place. This error also only occurs when using `one-of`; if you simply `ask turtles` the error will not occur. For example, 
``` ask one-of turtles with [  size > 2  ] [```

```Fd 1 ]```
Will call the error if there are no turtles with a size greater than 2. To fix the error, add in a check using `nobody` to avoid the problem:
```if one-of turtles with [ size > 2 ] != nobody [```

```Fd 1 ]```


**“Expected an X here, rather than Y”**
This is a more generic error that means you have a syntax error. Because each primitive’s syntax is different, it’s a good idea to check the exact syntax in the NetLogo Dictionary. This may be a case of missing brackets, or you have given a primitive the wrong type of input (a list instead of a number, an agentset instead of a reporter). 
For example, `ask cats [ face mice ]` would get the error “Face expected this input to be a turtle or patch, but got a turtle agentset instead”. This is because `face` takes a single turtle or a single patch as its input, and we gave it the entire agentset of `mice`. 

**When pressing GO or another button, nothing happens**
When you try to run a model and nothing seems to happen or update, you may have forgotten to add `tick` in your Go procedure. If your model is using “tick based” updates, you must include `tick` for your displays to update. (See `tick` for more information.) 


**You can't use [COMMAND] in a turtle context, because [COMMAND] is** **observer-only.** 

This error occurs when you are trying to use a primitive in a context it is not meant for. Turtles have some primitives that are exclusive to them; there are also patch-specific, link-specific, and observer-specific primitives. For example, asking turtles to `sprout` new turtles (or using `sprout` within an `ask turtles [ … ]` context) will result in this error, because only patches can use `sprout`. 
To fix this error, make sure you are using the primitive correctly and by the correct agent type. You may have forgotten to use the primitive within an `ask turtles [...]` or `ask patches [...]` context. Check the NetLogo Dictionary to find which agent types a primitive is compatible with. You may need to use a similar primitive that is used by a different type of agent. (`create-turtles`, `hatch`, and `sprout` all create new turtles, but are used by different agents.)
This error applies to other types of agent types such as links, patches, and observer.
Some examples are: 

**You can't use SETXY in a patch context, because SETXY is turtle-only.**	

You may be wrongly asking the patches to move, which they cannot. Make sure your code is within an ask turtles or ask [breed-name] block. Only turtles and turtle breeds can change their position.

**You can’t use DIE in a patch context, because DIE is turtle or link-only.**

 You may be asking turtles to `die` within an `ask patches [...]` context, which is not allowed. Only turtles can make turtles `die`. If you were hoping to clear a patch, use `clear-patches` instead of `die`.

**You can’t use CREATE-TURTLES in a turtle context, because CREATE-TURTLES is observer-only.**	 

If you are within an `ask turtles [...]` context, you are not allowed to use `create-turtles` to make more turtles. `create-turtles` is an observer-only primitive, which means it is not used within any `ask … [...]` context. If you were wanting to create more turtles from existing turtles, use `hatch`. If you were wanting to create more turtles from a patch, use `sprout`.

