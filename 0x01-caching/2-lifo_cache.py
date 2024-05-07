#!/usr/bin/env python3
"""module to make clas last in last out"""
from base_caching import BaseCaching
"""_summary_

    Returns:
        _type_: _description_
"""


class LIFOCache(BaseCaching):
    """_summary_

    Args:
        BaseCaching (_type_): _description_
    """


def __init__(self):
    """constructor
    """
    BaseCaching.__init__(self)
    self.queue = []


def put(self, key, item):
    """Put function"""
    if key is None or item is None:
        return

    if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
        last_item_key = self.cache_data.popitem(last=False)[0]
        print("DISCARD:", last_item_key)

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

    return self.cache_data[key]
