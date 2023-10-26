#!/usr/bin/env python3
""" A class that follow the most recently used
(MRU) algoritm for removing items from a cache
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ A class that inherits from BaseCaching"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ A method that adds a key,item to an orderedDict"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded = list(self.cache_data.keys())[-1]
            print(f"DISCARD: {discarded}")
            self.cache_data.popitem()
        self.cache_data[key] = item

    def get(self, key):
        """ A method that retrieves an item from a Dict"""
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        return self.cache_data.get(key, None)
