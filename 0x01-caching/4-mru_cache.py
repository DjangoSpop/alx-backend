#!/usr/bin/python3
from base_caching import BaseCaching
""" create a classs MRU cache that inherits from the BaseCaching class """


class MRUCache(BaseCaching):
    """ create a classs MRU cache that inherits from the BaseCaching class """

    def __init__(self):
        """constructor"""
        BaseCaching.__init__(self)
        self.queue = []

    def put(self, key, item):
        """Put function"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.queue.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_item_key = self.queue.pop()
            self.cache_data.pop(last_item_key)
            print("DISCARD:", last_item_key)
        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Get the value associated with the given key from the cache.
        Args:
            key (Any): The key to retrieve the value for.
        Returns:
            Any: The value associated with the given key, or None if the key is not found in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache_data[key]
