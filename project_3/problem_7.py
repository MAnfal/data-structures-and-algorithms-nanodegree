from collections import defaultdict


class RouteTrieNode:
    def __init__(self):
        self.handler = None
        self.children = defaultdict(RouteTrieNode)


class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode()

    def insert(self, parts, handler):
        node = self.root
        for part in parts:
            node = node.children[part]

        node.handler = handler

    def find(self, prefix):
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node


class Router:
    def __init__(self, not_found_handler):
        self.trie = RouteTrie()
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        parts = self.split_path(path)
        self.trie.insert(parts, handler)

    def lookup(self, path):
        parts = self.split_path(path)
        node = self.trie.find(parts)
        if node and node.handler:
            return node.handler

        return self.not_found_handler

    @staticmethod
    def split_path(path):
        return ["root"] + list(filter(lambda x: x != '', path.split('/')))


# Test cases

router = Router("Not Found handler")  # create the router
router.add_handler("/home/about", "About handler")  # add a route
router.add_handler("/home/", "Home handler")  # add a route with trailing slash

# some lookups with the expected output
print(router.lookup("/"))  # should print 'Not Found handler'
print(router.lookup("/home"))  # should print 'Home handler'
print(router.lookup("/home/about"))  # should print 'About handler'
print(router.lookup("/home/about/"))  # should print 'About handler'
print(router.lookup("/home///about/"))  # should print 'About handler'
print(router.lookup("/home/about/me"))  # should print 'Not Found handler'

router.add_handler("/", "Root handler")
print(router.lookup("/"))  # should print 'Root handler'
print(router.lookup(""))  # should print 'Root handler'
