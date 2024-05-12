#!/usr/bin/env python3
"""Helper function to get tuple of size"""


def index_range(page, page_size):
    """return start index and end index for pagination"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
