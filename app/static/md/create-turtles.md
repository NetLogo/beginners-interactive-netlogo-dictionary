`create-turtles` is a primitive that creates turtles with random colors and headings in the default shape of a triangle. `Crt` is the shorthand version of create-turtles. The syntax is

 ```create-turtles number-of-turtles [ optional-commands ]```

By using brackets [   ] you can choose to pass commands to those new turtles. For example, you can write

```create-turtles 100 [ ```

  ```set shape “person” ```		

​          ```forward 10 ] ```

which creates 100 turtles in the shape of a person and moves them forward. Only the observer can use this command!  For patches creating turtles, see [*sprout*](http://ccl.northwestern.edu/netlogo/docs/dictionary.html#sprout). For turtles creating new turtles, see [*hatch*](http://ccl.northwestern.edu/netlogo/docs/dictionary.html#hatch). 

