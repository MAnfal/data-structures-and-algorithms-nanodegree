from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)

    def find_words(self, prefix):
        matches = []
        if self.is_word:
            matches += [prefix]
        for (char, node) in self.children.items():
            matches += node.find_words(prefix + char)

        return matches


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]

        node.is_word = True

    def find(self, prefix):
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node

    def match(self, prefix):
        node = self.find(prefix)
        if node:
            return node.find_words(prefix)
        else:
            return []


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

# Test cases
print(MyTrie.match(""))  # Empty prefix - should return everything
print(MyTrie.match("ant"))
print(MyTrie.match("anth"))
print(MyTrie.match("f"))
print(MyTrie.match("fu"))
print(MyTrie.match("func"))
print(MyTrie.match("tri"))
print(MyTrie.match("trig"))
print(MyTrie.match("b"))  # Doesn't exist - should return empty list
