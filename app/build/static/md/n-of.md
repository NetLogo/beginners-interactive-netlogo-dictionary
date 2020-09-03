`n-of` is used when you want to randomly select exactly n elements out of an agent set.

For example, imagine you were trying to pick teams of a certain size for a soccer match. You want the individuals on these teams to be randomly selected, but do you want to be sure that the size of each team is fixed. In the model below, `n-of` is first used to pick members for the red team out of all 20 possible members. Then, `n-of` is used again to pick members for the blue team out of all not already chosen individuals.
