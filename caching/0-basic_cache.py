#!/usr/bin/env python3
"""Creates basic cache"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Child class BasicCache of parent BaseCaching"""
    def __init__(self, key, item):
        """initialize child class"""
        super().__init__()

    def put(self, key, item):
        """add cache data w/ key value pair"""
        self.cache_data(key) = item

    def get(self, key):
        """retrieve cache data using key value pair"""
        for key in sorted(self.cache_data.keys()):