#!/usr/bin/env python3
""" caching function
    """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ caching function:

    Args:
        FIFOCache ([class]): [basic caching]
    """

    def put(self, key, item):
        """ Add an item to cache
        """
        if not (key is None or item is None):
            self.cache_data[key] = item
            temp_list = list(self.cache_data.keys())
            if len(temp_list) > self.MAX_ITEMS:
                self.cache_data.pop(temp_list[0])
                print(f"DISCARD: {temp_list[0]}")

    def get(self, key):
        """ Get an item using key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
