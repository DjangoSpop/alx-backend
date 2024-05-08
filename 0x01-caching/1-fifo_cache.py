#!/usr/bin/env python3
"""crate a class FIFOCache"""
from base_caching import BaseCaching


class FIFOCache (BaseCaching):
    """FIFOCache class. Inherits from BaseCaching."""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add an item in the cache.

        Args:
            key: Key of the item.
            item: Item to be added.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                key_discarded = self.queue.pop(0)
                del self.cache_data[key_discarded]
                print("DISCARD: {}".format(key_discarded))
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """Get an item by key.

        Args:
            key: Key of the item.

        Returns:
            The item associated with the key, or None if not found.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
