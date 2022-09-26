In this solution we will fetch the current listing under the given directory. We will iterate over it 1 by 1 and see if the file
matches our pattern. If the file under test turns out to be a dir, we will recursively go in and repeat the procedure.

Time complexity is N * (N - 1) or N^2 - 1 or N^2 where N - 1 represents the number of directories we may have to traverse. Space complexity is O(n).