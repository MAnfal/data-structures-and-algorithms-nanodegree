import collections


class LRUCache(object):

    def __init__(self, capacity):
        self._capacity = capacity
        self._cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self._cache.pop(key)
            self._cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        if value is not None:
            try:
                self._cache.pop(key)
            except KeyError:
                if len(self._cache) >= self._capacity:
                    self._cache.popitem(last=False)

            self._cache[key] = value


our_cache = LRUCache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(7, 1234)
our_cache.set(8, 123)
our_cache.set(6, 101)  # least recently used not deleted
our_cache.set(3, 900)
our_cache.set(10, None)

print(our_cache.get(1))  # returns -1 because it got popped out since it was not used and more values were introduced.
print(our_cache.get(2))  # returns 2
print(our_cache.get(3))  # return 900

# Additional test cases
print(our_cache.get(5))  # return -1
print(our_cache.get(6))  # return 101
print(our_cache.get(10))  # return -1
