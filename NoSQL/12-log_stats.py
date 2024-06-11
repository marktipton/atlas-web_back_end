#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
nginx_collection = client.logs.nginx

def log_stats():
    """log for nginx stats"""
    num_logs = nginx_collection.count_documents({})
    print(f"{num_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    status_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_count} status check")

log_stats()
