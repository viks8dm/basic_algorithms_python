## Max and Min in a Unsorted Array

### Problem Statement

Given:
* unsorted array of integers

To do:
* Find smallest and largest integer from a given unsorted array
* The code should run in O(n) time. 
* Do not use Python's inbuilt functions to find min and max.

### Implementation

* The implementation is based on defining min-val and max-val variables, setting them to equal 1st element of the input list and then comparing with all other elements within a for loop.
* If min-val is greater than any test-element in the for loop, the min-val is set to that element's value.
* If max-val is less than any test-element within the for-loop, then max-val is set to that element's value.

### Efficiency

* Tiem complexity is O(n) since entire input list is checed within the for-loop setting
* Space complexity is O(1) since no extra space is used
