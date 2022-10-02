def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int)|None: Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None:
        return -1

    if number < 0:
        return -1

    if number in [0, 1]:
        return number

    bottom, top = 0, number

    while bottom <= top:
        mid = (bottom + top) // 2
        if mid ** 2 == number or mid ** 2 <= number < (mid + 1) ** 2:
            return mid
        elif mid ** 2 > number:
            top = mid
        else:
            bottom = mid


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (-1 == sqrt(None)) else "Fail")
print("Pass" if (-1 == sqrt(-10)) else "Fail")
