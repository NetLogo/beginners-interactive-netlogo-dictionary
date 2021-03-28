`facexy` makes a turtle change its direction (`heading`) to point towards a given coordinate (x,y). For example,  `ask turtles [ facexy 0 0 ]`  turns all turtles in a model to face the center of the model. 



Things to keep in mind when using `facexy`: 

* `facexy` doesn't change a turtle's position, only its heading. 
*  If a turtle is already on the given point (x, y), it will not change change its heading.



In the model example below, there are some fish and a single patch of food. When the ***add food*** button is clicked, we change the `pcolor` of the the patch at (3, -3) to white, which indicates a food and we ask the fish to look at this coordinate in order to indicate that they turn to the food.