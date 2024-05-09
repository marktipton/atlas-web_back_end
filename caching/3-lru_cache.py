#!/usr/bin/env python3
"""Last recently used cache"""
BaseCaching = __import__('base_caching').BaseCaching

class LRUCache(BaseCaching):
    """Last recently used cache"""

    def put(self, key, item):
        """assigns item to key in dictionary if not none"""

    def get(self, key):
        """gets the value in self.cache_data linked to a specified key"""
