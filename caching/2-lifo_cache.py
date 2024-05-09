#!/usr/bin/env python3
"""Last in first out cache"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Last in first out caching"""
    def __init__(self):
        """overload constructor"""
        super().__init__()
        self.insertion_order = []

    def put(self, key, item):
        """assigns item to key in dictionary if not none"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.insertion_order.append(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            self.cache_data.pop(last_key)
            print(f'DISCARD: {last_key}')

    def get(self, key):
        """gets the value in self.cache_data linked to a specified key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
