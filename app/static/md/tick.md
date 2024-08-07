A **tick** is a measure of time in NetLogo models (like seconds or minutes). Ticks are used instead of seconds, minutes, or hours because ticks are standardized across all models and computers; some models and computers run slower than others, but ticks are always the same! 



The primitive `tick` advances the **tick counter** by one, and updates the plots and monitors of a model. If you are using *tick-based* updates and include `tick` in your code, you must remember to reset the ticks before running the model by adding `reset-ticks` into the setup procedure, or else an error will occur. See `reset-ticks` for more. 



When creating a model, you have the option of choosing *continuous* or *tick-based* updates. This changes how often the view updates; *continuous* displays every change as it happens, and *tick-based* updates the entire model after one tick. Most models in the Models Library use *tick-based* updates. If your model is using *tick-based* updates, it must include `tick`, usually placed at the end of the `go` procedure. 



In the model example below, we have a bike and 5 houses. Our bicycle goes between the houses during the day (between the ticks 10 to 15) and delivers newspapers. At night, it goes back to the center. Every time the tick counter hits 24, we reset the ticks.