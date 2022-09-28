import os
import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    list_of_paths = []

    if os.path.exists(path):
        for file in os.listdir(path):
            file_path = "{0}/{1}".format(path, file)

            if os.path.isdir(file_path):
                list_of_paths += find_files(suffix, file_path)
            elif file_path.endswith(suffix):
                list_of_paths.append(file_path)

    return list_of_paths


# Test Case 1
print(find_files('.c', './testdir'))  # ['./testdir/subdir5/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir1/a.c', './testdir/t1.c']

# Test Case 2
print(find_files('.h', './testdir'))  # ['./testdir/subdir5/a.h', './testdir/t1.h', './testdir/subdir3/subsubdir1/b.h', './testdir/subdir1/a.h']

# Test Case 3
print(find_files('.c', ''))  # []

# Additional test cases
print(find_files('.h', './testdir/abc'))  # []
