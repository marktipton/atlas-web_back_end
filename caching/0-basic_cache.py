#!/usr/bin/env python3
"""Creates basic cache"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Child class BasicCache of parent BaseCaching"""
    def __init__(self, key, item):
        """initialize child class"""
        super().__init__()
        self.cache_data(key) = item

    def put(self, key, item):
        """add cache data w/ key value pair"""
        if (key or item is None) {
            return
        } else {
            self.cache_data(key) = item
        }

    def get(self, key):
        """retrieve cache data using key value pair"""
        if (key is None or key not in self.cache_data) {
            return None
        } else {
            return self.cache_data(key)
        }
