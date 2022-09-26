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
        try:
            self._cache.pop(key)
        except KeyError:
            if len(self._cache) >= self._capacity:
                self._cache.popitem(last=False)

        self._cache[key] = value


our_cache = LRUCache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))
print(our_cache.get(2))
print(our_cache.get(9))

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))

our_cache = LRUCache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)


print(our_cache.get(1))

print(our_cache.get(2))

print(our_cache.get(3))

