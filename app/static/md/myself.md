Though `self` and `myself` sound similar, they are used in different situations and must not be confused. `Myself` is used when an agent needs to refer itself while trying to address a different agent or agentset within an `ask` command or a reporter (e.g., of, with). For example, if you wanted a house door to open its door only when a person has the correct keycode, you can write 
```
ask person 1 [ 
    ask houses [ 
        if keycode = [keycode] of myself [ open-front-door ] ] ]
```
where `myself` refers to **person 1**. `Myself` is often used with `of` to report or set variables of the asking agent (`ask turtles with [pcolor = [pcolor] of myself]` or `ask turtles with [size < [size] of myself ]`). See **Myself Example** in the Models Library for more examples. 

`Self` is used when there is a single `ask` command, and the turtle, link, or patch is trying to refer to themselves. For example, 

```
let my-turtle nobody 
create-turtles 1 [ set shape “turtle” set my-turtle self] 
ask my-turtle [ forward 2]
```
would set the variable `my-turtle` to be the newly created turtle.  It is rarely used, because  `[color] of self` is equivalent to just saying `color`. 



In the model below, we use `myself` to make the people only enter the house that is their same color, by `if color = [ color ] of myself [ stay home ]`