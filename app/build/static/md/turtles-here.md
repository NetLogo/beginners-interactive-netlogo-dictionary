`Turtles-here` returns the **agentset** of all the turtles on the caller’s patch, including itself if the caller is a turtle. For example, `
```
create-turtles 3 
ask turtles [ show count turtles-here ]
```
would return `3`. You can also specify a breed by using `<breed>-here`; if there were some cats and mice in a model together, `ask cats [ if any? mice-here [ chase ]  ]` would make a cat chase the mice if they are on the same patch.