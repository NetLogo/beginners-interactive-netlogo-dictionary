`Die` is used by turtles and links. When a turtle or link is asked to `die`, it no longer exists in the model, will not execute any more code, and will disappear from any agentset it was in. For example, if `count turtles` returned 10, then `ask one-of turtles [die]` was called, now `count turtles` would return 9.