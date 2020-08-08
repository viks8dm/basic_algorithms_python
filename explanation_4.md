## Dutch National Flag Problem

### Problem Statement

Given:
* An input array consisting on only 0, 1, and 2

To do:
* Sort the array in a single traversal.
* Do not use any sorting function that Python provides.

### Implementation

* The implementation uses dummy indices for 0 and 2 values which should be at the start or end of the array respectively, after sorting is completed. 
* to complete sorting in single traversal, 0-value elements are accummulated from the start-index end of array and 2-value elements are accummulated from the end-index end of array. In the process, 1-value elements are sorted by themselves, due to swap operation for 0 and 2 value elements

### Efficiency

* time complexity is O(n), as all elements are accessed within a while loop
* space complexity is O(1) since no extra space is required