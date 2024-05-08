#!/usr/bin/python3
"""
wewill create a class that will
cache useing python
"""
BaseCaching = __import__('base_caching').BaseCaching
from collections import defaultdict
from datetime import datetime

class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching.

    Implements a Least Frequently Used (LFU) cache eviction policy.
    """

    def __init__(self):
        """Intialise the constructor"""
        super().__init__()
        self.frequency = defaultdict(int)
        self.last_used = {}

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
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Find the LFU item(s)
                min_frequency = min(self.frequency.values())
                lfu_items = [k for k, v in self.frequency.items() if v == min_frequency]

                # If more than one item has the minimum frequency, use LRU
                if len(lfu_items) > 1:
                    lfu_items.sort(key=lambda x: self.last_used[x])
                
                # Discard the LFU/LRU item
                discard_key = lfu_items[0]
                del self.cache_data[discard_key]
                del self.frequency[discard_key]
                del self.last_used[discard_key]
                print(f"DISCARD: {discard_key}")

            del self.cache_data[discard_key]
            del self.frequency[discard_key]
            del self.last_used[discard_key]
            print(f"DISCARD: {discard_key}")

        # Add the new item
        self.cache_data[key] = item
        self.frequency[key] += 1
        self.last_used[key] = datetime.now()

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
