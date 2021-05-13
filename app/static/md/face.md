`face` makes a turtle change its heading to point towards a specific patch or another turtle. For example,  `ask turtles [ face patch 0 0 ]`  turns all turtles in a model to face the center of the model. 



In the model example below, we have a person and a butterfly. The person is trying to catch the butterfly, while the butterfly is trying to run away from the person. We use the `face` primitive to make the person turn to the butterfly at every tick before moving one step closer to the butterfly. We also use the `face` primitive to make the butterfly turn to the opposite direction by making it look at the person first and then turn 180 degrees (and add a bit of randomness to simulate the flight of the butterfly) at each tick before moving 1 step forward.

