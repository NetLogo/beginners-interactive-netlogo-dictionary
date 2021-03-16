`diffuse` is an observer command that acts on every patch in the model. It causes each of them to diffuse (or spread around) the value of a given patch variable to their 8 [neighboring](/primitives/neighbors) patches. For example, if every patch had a "heat" variable that kept track of how hot that patch was, you could call (as the observer, i.e., not inside of an `ask patches` block) `diffuse heat .5` and every patch would equally distribute half of its heat to its 8 surrounding neighbors (each neighbor would get 1/8th of the 1/2 of the original heat, resulting in each neighbor's heat increasing by 1/16th of the original heat.) The original patch would keep the other 50% of the original heat.

This primitive is used when you want to simulate processes where diffusion happens such as heat transfer or diffusion in liquids and in the air.

See the related command `diffuse4` which does the same exact thing with the 4 cardinal direction neighbors.

In the example below, `diffuse` is used to model air pollution from a factory. Each tick, the factory releases some pollutant into the air. `diffuse` is then used to model how that pollutant would spread through the air, creating zones and hotspots of pollution.
