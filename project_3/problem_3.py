def mergesort(items):
    if len(items) <= 1:
        return items

    idx_m = len(items) // 2
    left = items[:idx_m]
    right = items[idx_m:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    idx_l = 0
    idx_r = 0

    while idx_l < len(left) and idx_r < len(right):
        if left[idx_l] < right[idx_r]:
            merged.append(right[idx_r])
            idx_r += 1
        else:
            merged.append(left[idx_l])
            idx_l += 1

    merged += left[idx_l:]
    merged += right[idx_r:]

    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.
    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None or len(input_list) < 2:
        return [-1]

    sorted_list = mergesort(input_list)
    num1 = ''
    num2 = ''

    for i in range(len(sorted_list)):
        if i % 2 == 0:
            num1 += str(sorted_list[i])
        else:
            num2 += str(sorted_list[i])

    return [int(num1), int(num2)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[], [-1]])
test_function([None, [-1]])
