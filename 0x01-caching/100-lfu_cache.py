#!/usr/bin/python3
"""
wewill create a class that will
cache useing python
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching.

    Implements a Least Frequently Used (LFU) cache eviction policy.
    """

    def __init__(self):
        """Intialise the constructor"""
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key of the item.
            item: The item to be added.

        Returns:
            None
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_freq = min(self.frequency.values())
            least_freq_keys = [
                k for k, v in self.frequency.items() if v == min_freq]
            if len(least_freq_keys) > 1:
                least_recent_key = min(
                    self.last_used.keys(), key=self.last_used.get)
                least_freq_keys.remove(least_recent_key)
            least_freq_key = least_freq_keys[0]
            del self.cache_data[least_freq_key]
            del self.frequency[least_freq_key]
            del self.last_used[least_freq_key]
            print("DISCARD:", least_freq_key)

        self.cache_data[key] = item
        self.frequency[key] = self.frequency.get(key, 0) + 1
        self.last_used[key] = self.current_time

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the key, or None if the key is not found.
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.last_used[key] = self.current_time
        return self.cache_data[key]
