`turtles-here` reports an **agentset** that contains all the turtles on the same patch with the original turtle, including the original turtle itself. For example, if we wanted to create a contagious disease model where red turtles passed the disease to all the turtles on the same patch, we would write the following code:



```
ask turtles with [color = red][
	ask turtles-here [
		set color red
	]
]
```


Things to keep in mind when using `turtles-here`:

* It is often undesirable to have the original turtle in the agentset that `turtles-here` reports. It may even cause errors in rare occasions. For example, the following code would show an error `ask turtles [ create-links-with turtles-here ]` because the original turtle would try to create a link with itself. In such cases, we can use the `other` primitive. For example, the following code would not show an error: `ask turtles [ create-links-with other turtles-here ]`
* We can always use the `with` primitive to narrow down the agentset that is reported by `turtles-here`. For example, the following code would only report the red turtles that are on the same patch with the original turtle: `turtles-here with [color = red]`.
* You can also use `turtles-here` with custom breeds by changing the term *turtles* with the plural name of the breed as `<breed>-here`. For example: `ask goats [ if any? plants-here [ eat ] ]`.



In the  model example below, we have three white patches that represent hospitals and some turtles that represent people. Some of our turtles are green, which indicates that they are healthy, and some are violet/purple, which indicates sickness. We use `turtles-here` to ask white patches to heal violet people.