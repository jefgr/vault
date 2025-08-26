Scheme is een dialect van Lisp, Lisp oorspronkelijk gebruikt voor AI


# Search Optimisations
## Sentinel Search
Add the value you seek to the end of the list, this allows us to skip the peek ahead to make sure you don't go out of bounds, but has to add a check if you found the value if you found the real one or the sentinel. You also need to detach-last at the end. This is only faster if detach-last in O(1) is (this is the case in vectorial and 2nd double linked list implementations (where you can call tail in O(1)))

## Sorted Lists
When traversing the list if (current value > search value) you can stop searching.

## Binairy Search
Requires indexing in O(1) and sorted list, so only works in our sorted vectorial implementation.
Look at the middle element, then repeat with the first/second half if it is greater/lesser than the search element.
This results in a O(log(n)) search algorithm.

# Ring
