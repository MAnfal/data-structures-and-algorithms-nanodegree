For union, we are going to create 1 set (sets always ignore the duplicated values) and iterate over both lists one by one to populate it.

For intersection, we are going to create 2 sets first to remove duplication then we are going to run a 3rd loop to create a 3rd set with only the common values between the 2 older sets.

Time complexity for union is O(n) and space complexity is O(n).

Time complexity for intersection is O(n) and space complexity is O(n).