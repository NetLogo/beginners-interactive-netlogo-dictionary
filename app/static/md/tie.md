`tie` is a link primitive that "ties" two turtles at the ends of the link together, almost like the two turtles were attached with a rigid stick. If the link is *directed*, then the *to* turtle follows the *from* turtle, but not the other way around. If the link is *undirected*, then both turtles will try to mimic the movements of the other, which can often become chaotic. A tied turtle will not only follow the movement of the other, but will also pivot around the rotating turtle when it turns and copy its new heading.



Because `tie` is a link primitive, it needs to be executed within a link context, such as `ask links [tie]` or, more commonly, `create-links-to turtles [tie]`. Note that since the tie is applied to the link, when the link is destroyed or either of the turtles at the ends of the link dies, the tie is destroyed as well.



In the model example below, we use `tie` to model the symbiotic relationship between whales and whale barnacles. In this relationship, the whale barnacles attach themselves to whales as they swim around. Since these barnacles passively filter food from the ocean water, it is highly beneficial for them to hitch a ride with these fast moving whales as they travel through the ocean. To model this attachment, we use `tie` along with a directed link to make the barnacles, once attached, follow the whales movement.
