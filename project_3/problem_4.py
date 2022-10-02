def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list)|None: List to be sorted
    """
    if not input_list:
        return []

    try:
        _frequency = [0] * 3
        for num in input_list:
            _frequency[num] += 1
        new_list = []
        for i in range(3):
            new_list.extend([i] * _frequency[i])
        return new_list
    except Exception as e:
        print("Error => {}".format(e))
        return []


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)

    # sorted will throw an error on edge case None so the comparison is not possible.
    if test_case is not None:
        if sorted_array == sorted(test_case):
            print("Pass")
        else:
            print("Fail")
    else:
        return print('Edge case provided, cannot proceed.')


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([])
test_function(None)
