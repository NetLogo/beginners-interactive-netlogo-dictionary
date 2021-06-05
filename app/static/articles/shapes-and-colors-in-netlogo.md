# Shapes and Colors in NetLogo

&nbsp;

For some phenomena, modeling the way agents look is almost as important as modeling how they behave. For others, creating pleasing and creative visualizations may simply augment our enjoyment of the modeling process and help us communicate our ideas better with others. 



NetLogo includes a Turtle Shapes Editor, a Link Shapes editor, and a Color Swatches panel that allow us to create agent-based models that do not only represent real-world phenomena conceptually, but also create powerful visualizations of our agents. If you would like to learn more about how to use the shapes editors and the color swatches, read along.

*Note: You can visit the NetLogo User Manual at <a href="https://ccl.northwestern.edu/netlogo/docs/" target="_blank">https://ccl.northwestern.edu/netlogo/docs/</a>* for more information on Shapes and Colors*

&nbsp;

---

&nbsp;

### Turtle Shapes

In NetLogo, turtle shapes are vector shapes. They are built up from basic geometric shapes; squares, circles, and lines, rather than a grid of pixels. This way, when we resize a turtle, its image does not loose quality (i.e., does not become *pixelated*). 

&nbsp;

##### Default Shapes

NetLogo already has a lot of pre-designed shapes for us to use. Some of these shapes, called *default shapes* are embedded within each new NetLogo model. These shapes are:



<img src="https://ccl.northwestern.edu/netlogo/docs/images/shapes/shapes.gif" alt="Default NetLogo Shapes" style="zoom:75%;" />



And the names of these shapes are:

* First row: default, airplane, arrow, box, bug, butterfly, car
* Second row: circle, circle 2, cow, cylinder, dot, face happy, face neutral
* Third row: face sad, fish, flag, flower, house, leaf, line
* Fourth row: line half, pentagon, person, plant, sheep, square, square 2
* Fifth row: star, target, tree, triangle, triangle 2, truck, turtle
* Sixth row: wheel, x

&nbsp;

##### Turtle Shapes Library

NetLogo has way more turtle shapes than the default ones for us to choose from. All we need to do is to click the **Import From Library** button, which will bring up a long list of shapes to choose from. 



<img src="https://ccl.northwestern.edu/netlogo/docs/images/shapes/library.gif" alt="Shapes Library" />

&nbsp;

##### Creating new shapes and editing existing ones

If none of the shapes in the library fits our model, we can create new shapes from scratch by clicking the **New** button and drawing our own shape. 

![New Shape Designer](../static/articles/img/newshape.png)

&nbsp;

A few things to keep in mind while using the New Shape Editor:

* You can pick a color that represents a *changing color*. That is, if you draw an object with this color, you can override this color with the <a href="../primitive/set">`set`</a> and <a href="../primitive/color">`color`</a> primitives. This color is gray by default.
* You can uncheck the *Snap the grid* option to draw shapes with higher precision.
* You can uncheck the *Rotatable* option to prevent your shape from being rotated when a turtle's heading changes.
* The name of your new shapes have to be unique. For example, if you create a tree shape, you should either name it with a different name such as *"tree 2"* or you should first delete the default tree shape from your model.
* We can also **Duplicate** an existing shape and **Edit** the copied one. 



&nbsp;

For more detailed information, visit the <a href="https://ccl.northwestern.edu/netlogo/docs/shapes.html" target="_blank">Shapes Editor</a> section of the NetLogo User Manual at <a href="https://ccl.northwestern.edu/netlogo/docs/shapes.html" target="_blank">https://ccl.northwestern.edu/netlogo/docs/shapes.html</a>.

&nbsp;

---

&nbsp;

### Colors

NetLogo has a custom way of representing colors that makes it easier to remember how to use them in code and how to manipulate color. Each color is assigned a number in the range 0 to 140, with the exception of 140 itself. The best way to familiarize ourselves with NetLogo colors is to click the **Tools** menu and pick the **Color Swatches** option, which will bring up a window that contains an interactive version of the following image that shows the corresponding number for each color and it's shades:

&nbsp;

![NetLogo Colors](https://ccl.northwestern.edu/netlogo/docs/images/colors.jpg)

&nbsp;

Things to keep in mind while using NetLogo colors in code:

* You can use the actual name of the main colors in your code such as `set color green` or `set color violet`.
* You can use arithmetic with color names to achieve shades of a color such as `set color green + 1` or `set color yellow - 2`. As a rule of thumb, if you add to a color, you will get a lighther shade, and if you deduct from a color, you will get a darker shade.
* You can use decimal points for more shades such as `set color green + 2.735` or `set color yellow - 3.336`.
* If you are familiar with technical aspects of color representation in computing, you can use the `approximate-rgb` and `approximate-hsb` primitives to get a specific color shade. 
* You can change the increment of colors between 1, 0.5, and 0.1 using the radio buttons at the bottom of the Color Swatches window.
* Every named color except black and white has a number ending in 5.
* On either side of each named color are darker and lighter shades of the color.
* 0 is pure black. 9.9 is pure white.
* 10, 20, and so on are all so dark they are very nearly black.
* 19.9, 29.9 and so on are all so light they are very nearly white.

&nbsp;

For more detailed information, visit the <a href="https://ccl.northwestern.edu/netlogo/docs/programming.html#colors" target="_blank">Colors</a> section of the NetLogo User Manual's Programming Guide Section at at <a href="https://ccl.northwestern.edu/netlogo/docs/programming.html#colors" target="_blank">https://ccl.northwestern.edu/netlogo/docs/programming.html#colors</a>.

&nbsp;

---

&nbsp;

### Link Shapes

NetLogo also allows us to go beyond the simple straight lines and define a variety of custom link shapes for our models. To create new link shapes, click the **Tools** menu and click the **Link Shapes Editor** item. You will 

&nbsp;

![Link Shape Designer](../static/articles/img/linkshapes.png)

&nbsp;

In contrast to turtle shapes, NetLogo only has one standard link shape and there is no library, either. If we want to use a link shape other than straight line, we either need to create it from scratch by clicking the **New** button or import it from a previously developed model by clicking the **Import from Model** button.



Things to keep in mind while using the Link Shapes Editor:

* You can change the *curviness* value of a link shape to make it non-linear.
* You can design a link with one, two, and three lines using the *left line*, *middle line*, and *right line* parameters. 
* You cannot make a link thick by default. You need to use the `thickness` primitive in your code to change a link's thickness such as `ask links [ set thickness 4 ]`.

&nbsp;

For more detailed information, visit the <a href="https://ccl.northwestern.edu/netlogo/docs/shapes.html#creating-and-editing-link-shapes" target="_blank">Shapes Editor</a> section of the NetLogo User Manual at <a href="https://ccl.northwestern.edu/netlogo/docs/shapes.html#creating-and-editing-link-shapes" target="_blank">https://ccl.northwestern.edu/netlogo/docs/shapes.html#creating-and-editing-link-shapes</a>.

