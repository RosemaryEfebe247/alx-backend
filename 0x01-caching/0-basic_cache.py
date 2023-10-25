#!/usr/bin/env python3
""" implement put and get function
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ A baseCache class that inherits from BasicCaching
    with methods that gets or put a function
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Function that adds an item
        """
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Function to get an item from the dictionary
        """
        return self.cache_data.get(key, None)
