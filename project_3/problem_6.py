import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if not ints:
        return

    _min = float('inf')
    _max = -float('inf')

    for _int in ints:
        if _int > _max:
            _max = _int

        if _int < _min:
            _min = _int

    return _min, _max


l = [i for i in range(0, 10)]

random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
