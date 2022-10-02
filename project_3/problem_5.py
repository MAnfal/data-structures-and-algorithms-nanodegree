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
        if prefix:
            node = self.find(prefix)

            if node:
                return node.find_words(prefix)

        return []


populated_trie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    populated_trie.insert(word)

# Test cases
print(populated_trie.match(""))  # Empty prefix - should return everything
print(populated_trie.match("ant"))
print(populated_trie.match("anth"))
print(populated_trie.match("f"))
print(populated_trie.match("fu"))
print(populated_trie.match("func"))
print(populated_trie.match("tri"))
print(populated_trie.match("b"))  # Doesn't exist - should return empty list
print(populated_trie.match("trig"))

# Edge case
empty_trie = Trie()

print(empty_trie.match("ant"))

# this condition will work for both empty and populated trie so checking it here will be sufficient.
print(empty_trie.match(None))
