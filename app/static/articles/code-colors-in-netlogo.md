# What does each color indicate in NetLogo code?

&nbsp;

Whenever we write a piece of code in NetLogo, the editor automatically highlights each primitive. Some primitives become green, some blue, some brown, and some purple. Below is a list of colors and what they indicate.

&nbsp;

Green with bold text indicates *<u>definition primitives</u>*  that allow us to define new things in NetLogo.  Some examples to definition primitives are: 

```
globals
turtles-own
patches-own
links-own
to
to-report
end
```

&nbsp;

Blue text indicates *<u>action primitives</u>*  that allow us to ask our agents to do things. Some examples to action primitives are: 

```
create-turtles
ask
set
let
if
ifelse
forward
fd
back
bk
die
reset-ticks
tick
clear-all
facexy
diffuse
```

&nbsp;

Purple text indicates *<u>reporter primitives</u>*  that reports a value, but does not change anything in the world themselves. The built-in agent characteristics such as `color`, `pcolor`, `xcor`, `size`, and `thickness` are also reporters, so they turn purple in code. Lastly, the basic agent breed primitives such as `turtles`, `patches`, `links`, `turtle`, `patch`, and `link` are reporters, too, so they turn purple in code.  Some examples to reporter primitives are: 

```
one-of
neighbors
any?
max
turtles-here
myself
random
random-float
turtles
patches
color
pcolor
size
+
/
>
<
=
```

&nbsp;

Brown text indicates *<u>a specific value</u>*, not a primitive, in NetLogo code. Numbers, any text that is wrapped around quotation marks (`""`), and names of the built-in NetLogo colors (e.g., `green, yellow, black, red`) will all turn brown in code. NetLogo also includes some handy keywords for mathematical constants such as `pi` and `e`. These constants, too, will turn brown in code. Some examples to specific values are: 

```
pi
127.36
"this is a random text"
e
green
brown
nobody
true
false
```



