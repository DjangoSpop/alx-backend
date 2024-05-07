"""Module for BasicCache class."""
from base_caching import BaseCaching

"""Module for BasicCache class."""


class BasicCache(BaseCaching):
    """BasicCache class. Inherits from BaseCaching."""

    def put(self, key, item):
        """Add an item in the cache.

        Args:
            key: Key of the item.
            item: Item to be added.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                key_discarded = sorted(self.cache_data.keys())[0]
                del self.cache_data[key_discarded]
                print("DISCARD: {}".format(key_discarded))

    def get(self, key):
        """Get an item by key.

        Args:
            key: Key of the item.

        Returns:
            The item associated with the key, or None if not found.
        """
        if key is None:
            return None
        return self.cache_data[key]
    
