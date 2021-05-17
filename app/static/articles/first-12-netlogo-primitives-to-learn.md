# The First 12 NetLogo Primitives to Learn

&nbsp;

NetLogo has numerous [primitives](/article/what-is-a-primitive.html). If you are an absolute beginner to NetLogo, it may be overwhelming to look at the dictionary [page](/dictionary.html) and figure out where to begin. We compiled this list to help you get started with the very first 12 primitives you should learn to begin creating your own agent-based models in NetLogo.

&nbsp;

#### [`to`](/primitive/to.html) and [`end`](/primitive/)
[`to`](/primitive/to.html) and [`end`](/primitive/) are essential for creating custom procedures in NetLogo. [`to`](/primitive/to.html) begins a procedure, and [`end`](/primitive/) concludes it. 

Procedures are used to create  smaller blocks of code that do specific things, and will simplify and break up your code. Simply add all your code within `to procedure-name` and [`end`](/primitive/). You can then use these procedure names elsewhere in your code. Keep in mind that except some special keyword primitives (e.g., `globals`, `turtles-own`), all of your code in the Code Tab should exist within a procedure or NetLogo will show an error.

You can also use [`to`](/primitive/to.html) and [`end`](/primitive/) to define procedures that will run when a button is clicked in the interface tab. Many NetLogo models have at least two buttons: `setup` and `go`, which run the code of the corresponding procedures in the Code Tab. If you would like to learn more about how to create such buttons, you can watch the [video tutorials](/videos.html) in this website.

<a href="/primitive/to.html" class="btn btn-primary float-right"><i class="fas fa-chevron-right"></i> Read more about &nbsp;&nbsp;&nbsp; `to`</a>

&nbsp;

<a href="/primitive/end.html" class="btn btn-primary float-right"><i class="fas fa-chevron-right"></i> Read more about &nbsp; `end`</a>

&nbsp;

&nbsp;

---

&nbsp;

#### `turtles` and `patches`

`turtles` and `patches` are two of the three main agent-types in NetLogo that we can use to create our models.  Accordingly, each of these keywords also function as *reporters* that give us a *randomized* list of all the agents (called an agentset) in a model at any given time. We commonly use these primitives with the `ask` primitive to make our agents do things. 

<a href="/primitive/turtles.html" class="btn btn-primary float-right"><i class="fas fa-chevron-right"></i> Read more about &nbsp; `turtles`</a>

&nbsp;

<a href="/primitive/patches.html" class="btn btn-primary float-right"><i class="fas fa-chevron-right"></i> Read more about &nbsp; `patches`</a>

&nbsp;

&nbsp;

---

&nbsp;

#### `create-turtles`

`create-turtles` is how we make new turtles in our NetLogo models. Turtles are independent mobile agents in NetLogo. We mainly use turtles to model agents (e.g., people, animals, objects, institutions) that move around and interact with other or the world around them (i.e., patches). We can create any number of turtles in a model. 

<a href="/primitive/create-turtles.html" class="btn btn-primary float-right"><i class="fas fa-chevron-right"></i> Read more about &nbsp; `create-turtles`</a>

&nbsp;

&nbsp;

---

&nbsp;


#### [`ask`](/primitive/ask.html)

[`ask`](/primitive/ask.html) allows us to make agents and agentsets do things. This is how we accomplish almost all actions in NetLogo; for agents to do any action, we must *ask them* to do so using `ask`.  We use `ask` to make turtles change the way they look, move around the world, interact with each other, remember past events, make decisions based on their environment and so on. We also use `ask` to make patches change color, remember custom values (e.g., pollution, temperature), and interact with other patches and turtles.

<a href="/primitive/all.html" class="btn btn-primary float-right"><i class="fas fa-chevron-right"></i> Read more about &nbsp; `ask`</a>

&nbsp;

&nbsp;

---

&nbsp;

#### `forward`

`forward` makes a turtle simply move any units on a straight path. It is an indispensable primitive to create Netlogo models with agents moving around in all directions such as cars moving on a road, birds flying in the air, or electrons moving on a wire. If a turtle is heading east and we ask it to `forward 1`, it will move 1 unit to the right. We can use any number with `forward` such as `forward 0.01`, `forward 3`, or even `forward -1`, which would make the turtle move *backwards*.

<a href="/primitive/forward.html" class="btn btn-primary float-right"><i class="fas fa-chevron-right"></i> Read more about &nbsp; `forward`</a>

&nbsp;

&nbsp;

&nbsp;

---

&nbsp;

#### `right`

`right` makes a turtle change its direction (i.e., heading) any to the right. In other words, it makes a turtle turn right.

<a href="/primitive/right.html" class="btn btn-primary float-right"><i class="fas fa-chevron-right"></i> Read more about &nbsp; `right`</a>

&nbsp;

&nbsp;

&nbsp;

---

&nbsp;

#### `if`

`if` is used to conditionally run a command. If you want a portion of code to run only if a certain check passes, you would use `if`. For example, if you want turtles to move **only** if they are standing on a red patch, you could use `if` to say:

<a href="/primitive/if.html" class="btn btn-primary float-right"><i class="fas fa-chevron-right"></i> Read more about &nbsp; `if`</a>

&nbsp;

&nbsp;

&nbsp;

---

&nbsp;

#### `set`

`set` is used to set the value of a certain variable. A variable is a certain characteristic or value that belongs to an agent or the model. Each variable has a certain value, which can be changed. For example, turtles have the variables `color` whose value could be red, yellow, blue, etc., and  `xcor`, and `ycor` whose values could be any coordinate of the world.  This can be used for any type of variable: turtle variables, patch variables, locally defined and globally defined variables. `set` is used to change the value of a variable.

<a href="/primitive/set.html" class="btn btn-primary float-right"><i class="fas fa-chevron-right"></i> Read more about &nbsp; `set`</a>

&nbsp;

&nbsp;

&nbsp;

---

&nbsp;


#### 

#### `clear-all`

`clear-all` is used to clear out everything in your model. This is usually used in your `setup` procedure, to start your model off with a clean slate. `clear-all` clears any turtles and links, resets all variables, and sets patches back to black.

<a href="/primitive/clear-all.html" class="btn btn-primary float-right"><i class="fas fa-chevron-right"></i> Read more about &nbsp; `clear-all`</a>

&nbsp;

&nbsp;