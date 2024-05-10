#!/usr/bin/env python3
"""Most recently used cache"""
BaseCaching = __import__('base_caching').BaseCaching


#!/usr/bin/env python3
"""Last recently used cache"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Most recently used cache"""

    def __init__(self):
        """overload constructor"""
        super().__init__()
        self.use_order = []

    def put(self, key, item):
        """assigns item to key in dictionary if not none"""
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.update_use_order(key)

        if len(self.cache_data) > self.MAX_ITEMS:
            # get key for
            mru = self.use_order.pop()
            self.cache_data.pop(mru)
            print(f'DISCARD: {mru}')

    def update_use_order(self, key):
        """tracks the most key usage recency"""
        if key in self.use_order:
            self.use_order.remove(key)
        self.use_order.append(key)

    def get(self, key):
        """gets the value in self.cache_data linked to a specified key"""
        if key is None or key not in self.cache_data:
            return None
        self.update_use_order(key)
        return self.cache_data.get(key)
