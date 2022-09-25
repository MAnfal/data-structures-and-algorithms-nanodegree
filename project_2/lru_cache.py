import collections


class LRUCache(object):

    def __init__(self, capacity):
        # Initialize class variables

        # Initialize class variables _capacity and _cache
        self._capacity = capacity
        self._cache = collections.OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        try:
            # Getting value from cache by key and returning it
            value = self._cache.pop(key)
            self._cache[key] = value
            return value
        except KeyError:
            # If there was KeyError caught, returning -1
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        try:
            # Removing existing cache value by key
            self._cache.pop(key)
        except KeyError:
            # If there was KeyError caught and if length of cache is greater or equal capacity, removing oldest item
            # from cache
            if len(self._cache) >= self._capacity:
                self._cache.popitem(last=False)

        # Assigning value to the key
        self._cache[key] = value


our_cache = LRUCache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))      # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values
our_cache = LRUCache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)

# Test Case 1
print(our_cache.get(1))  # returns 1
# Test Case 2
print(our_cache.get(2))  # returns 2
# Test Case 3
print(our_cache.get(3))  # return -1
# tests
