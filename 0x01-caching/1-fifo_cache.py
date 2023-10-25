elf.cache_data.key()[-1]IFOCache(BaseCaching):
    """ A class that initializes the put and get
    in First in first format
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ appends key value to cache_data
        Discards the first item if Max is reached
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded = list(self.cache_data.keys())[-1]
            print(f"DISCARD: {discarded}")
            self.cache_data.pop(discarded)
        self.cache_data[key] = item

    def get(self, key):
        """ Funtion to get a key from cache_data
        """
        return self.cache_data.get(key, None)
