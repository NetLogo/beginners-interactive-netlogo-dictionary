`diffuse` is an observer primitive that acts on every patch in the model. It causes each patch to diffuse (or spread around) the value of a given patch variable to their 8 [neighboring](/primitives/neighbors) patches. This primitive is very useful when we want to simulate processes where diffusion happens such as the diffusion of a smell or pollution in the air.



For example, if every patch owned a *pollution* variable that kept track of how polluted that patch was, you could use (as the observer, not inside of an `ask patches` block) `diffuse heat 0.5` and every patch would equally distribute half of its heat to its 8 surrounding neighbors. Each neighbor would get 1/8th of the 1/2 of the original heat, resulting in each neighbor's heat increasing but the original patch's heat halving.



Things to keep in mind when using `diffuse`: 

* You cannot use `diffuse` inside within `ask` block. It is an observer-only primitive.
* You can also use the `diffuse4` primitive if you would like to achieve the same exact outcome but with the 4 cardinal direction neighbors.



In the model example below, we use `diffuse` to model air pollution from a factory. At each tick, the factory releases some pollutant into the air by increasing the pollution variable of the patch there by 1. Then, the pollution diffuses from this original patch to its neighbors, and then from its neighbors to its neighbors' neighbors, and so on. As a result, the pollutant spreads through the air, creating zones and hotspots of pollution.