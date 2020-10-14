Similar to `any?`, `all?` is used to check if all agents of an agentset return **True** for a given true-or-false condition. If all agents return **True**, `all?` will return **True**, otherwise it will return **False**. Its syntax is:



``` all? agentset [ reporter ] ```



For example, `all? turtles [ size > 1]` would return **True** if and only if every turtle in the model had a size greater than one. 



In the model below, there is a flock of sheep. As the sheep move around, if they have not eaten yet and are on a green patch of grass, they will eat. We want the model to stop after all sheep have eaten, so we include the line:



``` if all? turtles [ have-eaten? = true ] [ stop ] ```

