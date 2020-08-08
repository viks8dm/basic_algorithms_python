"""
find square root of given integer
- find floor value of square root
- e.g:
    for 16 --> 4
    for 27 --> 5

expected time complexity: O(logn)
"""

##########################
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # corner cases
    if number==0 or number==1:
        return number

    # find sqaure root using binary search
    l = 0
    r = number/2
    while l<=r:
        mid = (l+r)//2
        mid_sq = mid*mid
        if mid_sq == number:
            return mid

        if mid_sq < number:
            l = mid + 1
            result = mid
        else:
            r = mid-1

    return result

##########################
if __name__=="__main__":
    # given test cases
    print("------- given tests ------------")
    print ("Pass" if  (3 == sqrt(9)) else "Fail")
    print ("Pass" if  (0 == sqrt(0)) else "Fail")
    print ("Pass" if  (4 == sqrt(16)) else "Fail")
    print ("Pass" if  (1 == sqrt(1)) else "Fail")
    print ("Pass" if  (5 == sqrt(27)) else "Fail")

    # additional tests
    from random import randint
    import math
    print("------- additional tests ------------")
    for i in range(100):
        n = randint(0, 1000)
        result = "Pass" if  (int(math.sqrt(n)) == sqrt(n)) else "Fail"
        print("Test - " + str(i) + " --> sqrt(" + str(n) + ") = " + str(sqrt(n)) + " : " + result)
