We will check if a user exists in the current user list. If not, we will iterate over the available group list and recursively traverse them to find the user.

Time complexity of this process is O(depth * users) and space complexity is O(depth * users)