#!/usr/bin/env python3
""" Lists all documents in a collection """
import pymongo


def list_all(mongo_collection):
    """lists all documents in given collection"""
    return mongo_collection.find({})
