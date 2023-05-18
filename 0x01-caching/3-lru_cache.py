#!/usr/bin/env python3
""" caching fnc
    """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ caching fnc:
    Args:
        LRUCache ([class]): [basic caching]
    """

    def __init__(self) -> None:
        """ initializing class """
        self.temp_list = []
        super().__init__()

    def put(self, key, item):
        """ Add an item to cache
        """
        if not (key is None or item is None):
            self.cache_data[key] = item
            self.temp_list.append(key)
            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                pop = self.temp_list.pop(0)
                self.cache_data.pop(pop)
                print(f"DISCARD: {pop}")

    def get(self, key):
        """ Get an item using  key
        """
        if (key is None) or not (key in self.cache_data):
            return None
        self.temp_list.insert(len(self.temp_list),
                              self.temp_list.pop(self.temp_list.index(key)))
        return self.cache_data.get(keyg
