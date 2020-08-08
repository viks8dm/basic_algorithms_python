"""
find index of target number from a list of rotated & sorted array
Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
"""
##########################
def find_pivot_idx(arr, l, r):
    if (l>r):
        return -1

    mid_idx = (l + r) // 2
    # mid_idx or mid_idx-1 is pivot point
    if (mid_idx < r) and (arr[mid_idx+1] < arr[mid_idx]):
        return mid_idx
    if (mid_idx > l) and (arr[mid_idx] < arr[mid_idx-1]):
        return (mid_idx-1)

    # use binary search to find rotation pivot index
    if (arr[l] >= arr[mid_idx]):
        return find_pivot_idx(arr, l, mid_idx-1)
    
    return find_pivot_idx(arr, mid_idx+1, r)

##########################
def binary_search_recursive_soln(array, target, idx_left, idx_right):
    if idx_left>idx_right:
        return -1
    
    idx_mid = (idx_left+idx_right)//2
    elem = array[idx_mid]
    
    if elem==target:
        return idx_mid
    elif target<elem:
        return binary_search_recursive_soln(array, target, idx_left, idx_mid-1)
    else:
        return binary_search_recursive_soln(array, target, idx_mid+1, idx_right)


##########################
def rotated_array_search(input_list, target):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # empty list
    if len(input_list) == 0:
        # print("ERROR: input list is empty")
        return -1

    l = 0
    r = len(input_list) - 1
    # one element list
    if (l==r):
        if input_list[l] == target:
            return l
        else:
            return -1

    # find rotation pivot index
    pivot_idx = find_pivot_idx(input_list, l, r)
    # corner case: array is not rotated
    if (pivot_idx == -1):
        return binary_search_recursive_soln(input_list, target, l, r)

    # rotated array
    if input_list[pivot_idx] == target:
        return pivot_idx
    
    if input_list[0]<=target:
        return binary_search_recursive_soln(input_list, target, l, pivot_idx-1)
    return binary_search_recursive_soln(input_list, target, pivot_idx+1, r)



##########################
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

##########################
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

##########################
if __name__=="__main__":
    # given test cases
    print('------- test set - 1: given test cases')
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])

    print('=======================================')
    print('------- test set - 2: some corner cases')
    test_function([[], -1])     # empty
    test_function([[5], 0])     # 1 element
    test_function([[5, 6, 7, 8, 1, 2, 3, 4], None]) # invalid target data
    test_function([[1, 2, 3, 4, 5, 6, 7, 8], 5])    # no rotation
    test_function([[6,7,8,'',2,3,4], 4])    # invalid data
    test_function([[6,7,8,0,2,3,4], ''])    # invalid data

    print('=======================================')
    print('------- test set - 3: more cases')
    test_function([[1,2,3,4,5, -5, -4, -2], 4])
    test_function([[6,7,8,1,2,3,4], 6])
    test_function([[6,7,8,1,2,3,4], 7])
    test_function([[6,7,8,1,2,3,4], 8])
    test_function([[6,7,8,1,2,3,4], 1])
    test_function([[6,7,8,1,2,3,4], 2])
    test_function([[6,7,8,1,2,3,4], 3])
    test_function([[6,7,8,1,2,3,4], 4])