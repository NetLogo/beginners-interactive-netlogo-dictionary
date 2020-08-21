`in-cone` is a primitive that allows for simulating a "cone of vision" in front of a turtle. This allows us to simulate an agent having some sight or other sense in front of them, but not behind or to the side of them.

The cone is constructed with two inputs: how far the agent can see (the radius), and how wide the agent can see (the number of degrees, anywhere from 0 to 360). For instance, if we wanted some rabbits to eat if there were carrots in front of them, but not behind or to the side, we could say 

```
ask rabbits [
  if any? carrots in-cone 3 45 [ eat ]
]
```

Note that like `in-radius`, `in-cone` can end up reporting itself. Be sure to account for that in your models if need be with the `other` primitive. 

In this example model, `in-cone` is used to simulate 4 motion-activated wildlife cameras. When a camera detects that there are `any? animals in-cone 8 50`, it will turn yellow to simulate taking a picture. (Note that the highlighted patches are just to better visually show the cone of vision. In actuality none of the `in-cone` turtle detection has anything to do with which patch a turtle is standing on.)
