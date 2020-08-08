## Search in a Rotated Sorted Array

### Problem Statement

Given: 
* A sorted array which is rotated at some random pivot point.
    * Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
* A target value to search. If found in the array return its index, otherwise return -1.
* assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n)

Example:
Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

### Implementation

* Initial part of the implementation looks at corner cases and tries to find the pivot of rotation using binary-search to recursively half the sample-array in which to look for change in sorting sequence
* once the pivot point is found, the array is divided into two sub-arrays on both sides of this pivot point and depending on which one target belongs to, binary search is used on that particular sub-array


### Efficiency

* time efficiency is same as that of binary search, O(log-n)
* space efficiency is O(1) as no extra storage is used