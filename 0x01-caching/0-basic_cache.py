#!/usr/bin/python3
""" implement put and get function """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ A basicCache class that inherits from BasicCaching """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Function that adds an item """
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """ Function to get an item from the dictionary """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
