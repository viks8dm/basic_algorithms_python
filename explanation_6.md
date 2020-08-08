## Max and Min in a Unsorted Array

### Problem Statement

Given:
* unsorted array of integers

To do:
* Find smallest and largest integer from a given unsorted array
* The code should run in O(n) time. 
* Do not use Python's inbuilt functions to find min and max.

### Implementation

The implementation is based on divide and conquer strategy where unsorted array is recursively divided into left and right parts around the mid-element, till one or two elements remain in the array, in which case determination of minimum or maximum is done using one comparison operation at most.

### Efficiency

* Time efficiency is O(n) since for any length n array:
    * one part takes T(floor(n/2))
    * second part will take T(ceil(n/2))
    * additional 2 comparison operations will have to be performed
