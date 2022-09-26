Instead of going for a traditional binary tree, I am going for building a dict that represents every character in the given sentence as a unique string. We will assign values like 01, 001, 0001, 00001 etc.
Once assigned, we will replace the original chars with these values and since they take up less space, we will be successfully perform a lossless encoding using huffman method. Decoding is the exact reverse.
We will build our code if we encounter a 0 and if we encounter a 1, we will perform a lookup in the dict to figure out the character and so on.

Time complexity for this is O(nlogn) and space complexity is O(logn).