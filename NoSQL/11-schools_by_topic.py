#!/usr/bin/env python3
"""returns list of schools w/ given topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """returns list of schools w/ given topic"""
    return mongo_collection.find({"topics": topic})
