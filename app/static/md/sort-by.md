`sort-by` allows us to sort lists or agentsets using a user-defined comparison. `sort-by` is best used in the specific circumstance that you are sorting a list and you need very specific control of how the elements in that list are sorted. As an example of how to use `sort-by`, consider the example of sorting a list of strings according to their length:



```
to-report smaller-length [a b]
  report (length a) < (length b)
end

show sort-by smaller-length ["xyz", "abcd" "12345"]
=> ["xyz" "abcd" "1234"]
```


The exact syntax is `sort-by <reporter> <list>`, so in the example above, `smaller-length` is the reporter. For a reporter to be used by `sort-by` it must (1) take in two inputs and (2) report true or false. Given two inputs `A` and `B`, if the reporter reports true, then `A` is placed before `B`, and if it reports false, then `B` is placed before `A`. Or, put more intuitively, working left to right in the sorted output list, the reporter will be true for every pair of numbers. That is, in the list `["xyz" "abcd" "1234"]`, length "xyz" < length "abcd", length "abcd" < "1234".



Things to keep in mind when using `sort-by`:

* `sort-by` will always sort in ascending order, so if you want the results in descending order, you can pass the output into `reverse` such as `reverse sort-by [size] smaller-length ["xyz", "abcd" "12345"]`. 
* The output to `sort-by` is always a list, even if the input is an agentset. When sorting agentsets, ties are broken randomly. When sorting lists however, the sort is "stable" which means that if two "equal" elements are in a certain order in the input list, they will stay in that order in the sorted list.
* Although `sort-by` does work on agentsets as well as lists, you will almost always want to use `sort-on` because  it is significantly easier to use to sort agentsets.