#!/usr/bin/env python3
"""Last recently used cache"""
BaseCaching = __import__('base_caching').BaseCaching

class LRUCache(BaseCaching):
    """Last recently used cache"""

    def __init__(self):
        """overload constructor"""
        super().__init__()
        self.use_order = []

    def put(self, key, item):
        """assigns item to key in dictionary if not none"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # get key for
            lru = self.use_order.pop(0)
            self.cache_data.pop(lru)
            print(f'DISCARD: {lru}')
        self.cache_data[key] = item
        self.update_use_order(key)

    def update_use_order(self, key):
        """tracks the most least recently used key"""
        if key in self.use_order:
            self.use_order.remove(key)
        self.use_order.append(key)

    def get(self, key):
        """gets the value in self.cache_data linked to a specified key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
