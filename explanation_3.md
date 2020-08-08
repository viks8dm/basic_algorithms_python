## Rearrange Array Elements

### Problem Statement

Given:
* an array with elements in [0, 9]

Return:
* two numbers formed from given array, so that their sum is maximum possible
* number of digits in both numbers cannot differ by more than 1
* don't use any python sorting function
* expected time complexity O(nlog(n)).
* e.g:
    * given array --> [1, 2, 3, 4, 5]
    * answer --> [531, 42] or [542, 31] (any one solution is ok)

### Implementation

* To get the maximum sum, both numbers should start with the two largest digits present in the array. Hence, I try to sort the array in descending order and put alternate elements in two different arrays and form a number out of these sub-arrays.

* For sorting, merge-sort has been used

### Efficiency

* time complexity is same as that of merge-sort, O(n-logn). two most time consuming sections of the implementation are:
    * mergesort with time complexity O(n-logn)
    * for loop to form array with time complexity O(n)

* space complexity is also saame as that of merge-sort, O(n)