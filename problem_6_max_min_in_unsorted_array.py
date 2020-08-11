"""
find smallest and largest integer from a given unsorted array
The code should run in O(n) time. 
Do not use Python's inbuilt functions to find min and max.
"""
# #############
# def get_min_max_recursive(arr, l, r):
#     if (l==r):
#         return (arr[l], arr[l])
    
#     if l + 1 == r:
#         if arr[l] <= arr[r]:
#             return (arr[l], arr[r])
#         return (arr[r], arr[l])

#     mid = (l + r) // 2
#     (l_min, l_max) = get_min_max_recursive(arr, l, mid)
#     (r_min, r_max) = get_min_max_recursive(arr, mid+1, r)

#     n_min = l_min if (l_min<=r_min) else r_min
#     n_max = l_max if (l_max>=r_max) else r_max
    
#     return (n_min, n_max)

# #############
# def get_min_max(ints):
#     """
#     Return a tuple(min, max) out of list of unsorted integers.

#     Args:
#        ints(list): list of integers containing one or more integers
#     """
#     # corner cases
#     if len(ints) == 0:
#         return (None, None)
    
#     return get_min_max_recursive(ints, 0, len(ints)-1)

#############
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return (None, None)

    min_val, max_val = ints[0], ints[0]

    for i in ints:
        if (i<min_val):
            min_val = i
        elif (i>max_val):
            max_val = i

    return (min_val, max_val)

#############
if __name__=="__main__":
    import random

    # test -1:
    print('------ test 1')
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)
    print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

    # test -2:
    print('------ test 2')
    print ("Pass" if ((None, None) == get_min_max([])) else "Fail")

    # test -3:
    print('------ test 3')
    print ("Pass" if ((8, 8) == get_min_max([8])) else "Fail")

    # test - 4 to 99: random cases
    for i in range(100-4):
        m = random.randint(1, 20)
        n = random.sample(range(-1000, 1000), m)
        
        print('------ test ' + str(i+4))
        print("array: " + str(n))
        print("min, max = " + str(get_min_max(n)))

        result = "PASS" if ((min(n), max(n)) == get_min_max(n)) else "FAIL"

        print(result)
        if result == "FAIL":
            break
