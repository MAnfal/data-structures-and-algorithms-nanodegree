We will follow binary search here. For 0 and 1, we will return back the number immediately. For higher values, we will
check the middle. If the middle value is the result, or if the answer is between the middle value's square and middle value + 1's square,
we will return the middle value of our result. This will take care of both whole results and in case we are dealing with fractions.
After that, if the result is not found, we will adjust either top or bottom value and run the code again.

Program runs in O(log n) complexity with O(1) space complexity.