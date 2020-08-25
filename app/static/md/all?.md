Similar to `any?`, `all?` checks if all agents of a given agentset reports true for a given reporter. It takes the form `all? agentset [ reporter ]`, where reporter is a **true-or-false condition**. For example, `all? turtles [ size > 1]` would return **True** if and only if every turtle in the model had a size greater than one. `All?` reports as **False** if a single agent reports **False** for the **true-or-false condition**. 
