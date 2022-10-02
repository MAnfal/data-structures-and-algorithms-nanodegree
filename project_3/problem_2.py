def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    _len = len(input_list)

    bottom, top, pivot_point = 0, _len, 0

    while bottom <= top:
        pivot_point = (bottom + top) // 2
        if input_list[0] < input_list[_len - 1] or pivot_point == _len - 1:
            pivot_point = 0
            break
        if input_list[pivot_point - 1] > input_list[pivot_point]:
            break
        elif input_list[0] < input_list[pivot_point]:
            bottom = pivot_point
        elif input_list[0] > input_list[pivot_point]:
            top = pivot_point

    if input_list[pivot_point] <= number <= input_list[_len - 1]:
        bottom = pivot_point
        top = _len
    else:
        bottom = 0
        top = pivot_point

    while bottom <= top:
        pivot_point = (bottom + top) // 2
        if input_list[pivot_point] == number:
            return pivot_point
        elif input_list[pivot_point] < number:
            bottom = pivot_point + 1
        else:
            top = pivot_point - 1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
