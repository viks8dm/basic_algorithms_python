"""
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
"""
##############################
def mergesort_descending(arr):
    if len(arr)<=1:
        return arr

    mid = len(arr) // 2
    l = arr[:mid]
    r = arr[mid:]

    l = mergesort_descending(l)
    r = mergesort_descending(r)

    return merge(l, r)

##############################
def merge(left, right):
    merged = []
    left_idx = 0
    right_idx = 0
    
    while ((left_idx < len(left)) and (right_idx < len(right))):
        if (left[left_idx] < right[right_idx]):
            merged.append(right[right_idx])
            right_idx += 1
        else:
            merged.append(left[left_idx])
            left_idx += 1

    merged += left[left_idx:]
    merged += right[right_idx:]

    return merged

##############################
def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # corner case: 0 or 1 element
    if len(input_list) == 0:
        return [0, 0]
    if len(input_list) == 1:
        return [input_list[0], 0]

    # corner case: 2 elements

    # sort in descending order
    sorted_list = mergesort_descending(input_list)

    # print(sorted_list)

    # make sub-arrays
    n1_str = ""
    n2_str = ""
    for i in range(len(sorted_list)):
        if ((i % 2) == 0):
            n1_str += str(sorted_list[i])
        else:
            n2_str += str(sorted_list[i])

    n1 = int("".join(n1_str))
    n2 = int("".join(n2_str))

    return [n1, n2]

##############################
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


##############################
if __name__=="__main__":
    # test set - 1: given sample tests
    print('------- test set - 1: given test cases') 
    test_function([[1, 2, 3, 4, 5], [531, 42]])
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

    # test set - 2: corner cases
    print('=======================================')
    print('------- test set - 2: corner cases') 
    test_function([[], [0, 0]])     # no array
    test_function([[1], [1, 0]])     # 1-element array
    test_function([[1,8], [1, 8]])     # 2-elements array
    test_function([[1,1,1,1], [11, 11]]) # repeat digits - single, even
    test_function([[1,1,1,1,1], [111, 11]]) # repeat digits - single, odd
    test_function([[1,1,1,1,2,2,2,2,2], [22211, 2211]]) # repeat digits - multiple

    # test set - 3: more tests
    print('=======================================')
    print('------- test set - 3: more test cases') 
    test_function([[7,5,3,4,7,2], [753, 742]])      # repeat digits
    test_function([[2,3,4,5,1,2,7,5,3,4,7,2], [754322, 754321]])
    test_function([[0,1,2,3,4,5,6,7,8,9], [97531, 86420]])

