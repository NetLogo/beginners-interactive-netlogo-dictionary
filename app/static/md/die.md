`Die` is used by turtles and links to remove it from the model. When a turtle or link is asked to `die`, it no longer exists in the model, will not execute any more code, and will disappear from any agentset it was in. For example, if `count turtles` returned 10, then `ask one-of turtles [die]` was called, now `count turtles` would return 9.



In the model below, a flock of sheep move around and eat grass to gain energy. As a sheep moves, it loses energy; if a sheep ever has 0 energy it should die. So we include

``` if energy <= 0 [ die ] ```

to remove those sheep from the model.

