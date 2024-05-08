#!/usr/bin/python3
"""module LFU Cache"""
from base_caching import BaseCaching
""" create a classs LFU cache that inherits from the BaseCaching class """


class LFUCache(BaseCaching):
    def __init__(self):
        """constructor"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            node = self.queue[self.queue.index(key)]
            node.value = item
            # move the accessed node to the front of queue
            self.queue.remove(node)
            self.queue.insert(0, node)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # discard the least frequency used item (LFU algorithm)
                lfu_key = self.queue[-1].key
                del self.cache_data[lfu_key]
                self.queue.pop()
                print("DISCARD:", lfu_key)

            # add the new item to the cache
            self.cache_data[key] = item
            self.queue.insert(0, key)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        # move the accessed node to the front of queue
        node = self.queue[self.queue.index(key)]
        self.queue.remove(node)
        self.queue.insert(0, node)

        return self.cache_data[key]
