`ifelse`, much like `if`, is used to run certain commands conditionally, that is, based on some given true-or-false condition. `ifelse` is used when you want to run one set of commands *if* a condition is true and another set otherwise.

For instance, at the beginning of many sports matches, a coin is flipped to determine who gets the ball first. *if* team A wins, then they get the ball, *else* (otherwise), team B gets the ball. to put this into NetLogo code, we would say:
```
ifelse team-A-wins-flip [
	give-team-A-ball
] [
	give-team-B-ball
]
```

This example simulates cars driving down a road, stopping at a gas station to top up their tanks before moving on. Each tick, each car checks if they are at the gas station (if the patch they are on has an x coordinate of 0) and if they are at less than a full tank of gas. If so, they start filling up their tank, otherwise, they start driving. Each time a car drives, it loses a little bit of gas, so when it loops back around to the gas station again, it will fill itself up again.
