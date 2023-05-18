#!/usr/bin/env python3
""" caching function
    """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ caching function:
    Args:
        BasicCachey ([class]): [basic caching]
    """

    def put(self, key, item):
        """ Add an item to cache
        """
        if not (key is None or item is None):
            self.cache_data[key] = item

    def get(self, key):
        """t item using keys
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
