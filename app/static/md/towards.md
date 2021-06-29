`towards` reports the angle that would be the heading value of a turtle if it were to face another turtle or patch. `towards` reports the absolute angle between the point coordinates of the two agents, and will change as the agents move around, but will not change if the headings of the agents change. 



In the model example below, we have a hawk and a butterfly. The hawk is trying to catch the butterfly, while the butterfly is trying to run away from the person. We use the `towards` primitive to make the hawk turn to the butterfly at every tick before moving one step closer to the butterfly. We also use the `towards` primitive to make the butterfly turn to the opposite direction by making it look at the hawk first and then turn 180 degrees (and add a bit of randomness to simulate the erratic flight of a butterfly) at each tick before moving 1 step forward.

