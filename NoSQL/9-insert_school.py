#!/usr/bin/env python3
""" Inserts a new document into a collection """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document into a collection
        returns: new _id
    """
    post_id = mongo_collection.insert_one(kwargs).inserted_id
    return post_id
