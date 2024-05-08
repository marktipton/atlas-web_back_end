#!/usr/bin/env python3
"""Creates FIFO caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """First in first out caching"""
    def __init__(self):
        """overload constructor"""
        super().__init__()
        self.insertion_order = []

    def put(self, key, item):
        """assigns item to key in dictionary if not none"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            print(f'DISCARD: {first_key}')
            del self.cache_data[first_key]

    def get(self, key):
        """gets the value in self.cache_data linked to a specified key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
