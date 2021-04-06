`reset-ticks` sets the tick counter back to zero. It is only used in models that use *tick-based* updates. `reset-ticks` is usually found at the end of a setup procedure. 



Things to keep in mind when using `reset-ticks`:

* If you are unsure what a `tick` means, refer to the [`tick`](/primitive/tick.html) item in this same dictionary.
* If you run the `tick` primitive without resetting the ticks first with the `reset-ticks` primitive, NetLogo will show an error.
* Notice that some NetLogo models, including the model example below, have their *go* buttons disabled until the *setup* button is clicked. This is achieved by choosing the `disable until ticks start` option when a button is created.



In the model example below, we have a bike and 5 houses. Our bicycle goes between the houses during the day (between the ticks 10 to 15) and delivers newspapers. At night, it goes back to the center. Every time the tick counter hits 24, we reset the ticks.

