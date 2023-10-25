#!/usr/bin/env python3
""" The fuction that gets and put an item in FIFO 
format
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ A class that initializes the put and get
    in First in first format
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Appends key value to cache_data
        Discards the first item if Max is reached
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded = list(self.cache_data.keys())[0]
            print(f"DISCARD: {discarded}")
            del self.cache_data[discarded]
        self.cache_data[key] = item

    def get(self, key):
        """ Funtion to get a key from cache_data
        """
        return self.cache_data.get(key, None)
