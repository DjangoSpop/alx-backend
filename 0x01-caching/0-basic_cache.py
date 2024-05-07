 #!/usr/bin/env python3
from base_caching import BaseCaching

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
    