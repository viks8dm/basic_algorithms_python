## Finding the Square Root of an Integer

### problem statement:
* Find the square root of the integer without using any Python library. You have to find the floor value of the square root.
* For example if the given number is 16, then the answer would be 4.
* If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.
* The expected time complexity is `O(log(n))`

### Implementation:
* Starting from smallest positive integet 0, the square of all integers `i*i` forms a monotonically increasing sequence, hence, I have used binary search for this implementation.
* First corner cases are addressed using if statement and then binary search implementation is used for finding the floor of the square root.
* Further, I have used `number/2` as the upper limit rather than using the `number`

### Efficiency

* Since binary search is O(log-(n)) the time complexity requirement is automatically satisfied, however, since I am using `number/2` as upper limit, actual time complexity is `O(log(n/2))`
* Space complexity is O(1)