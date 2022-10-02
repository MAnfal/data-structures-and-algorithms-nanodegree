Again in this problem we are going to use a conventional trie but instead of just adding characters in the dictionary, we will add parts of the path.

Time complexity of operations is as follows.

* Insert: O(n) where n is the length of the word.
* Find: O(m) where m is the length of the provided word.

The space complexity

* Insert: O(n) where n is the total number of nodes in trie.
* Find: O(n) where n is the total  number of nodes in trie.