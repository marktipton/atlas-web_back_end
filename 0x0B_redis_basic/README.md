# Redis Python

- Redis is an open source in-memory data structure store. It operates like a NoSQL Key/Value Store but supports multiple data structures and types including:

  - strings
  - lists
  - sets
  - sorted sets
  - hashes
  - bitmaps
  - hyperlogs
  - geospatial indexes

- Redis can act as both a caching system and a database

- Redis can be used with virtually every programming language

- Redis allows storage of strings, bytes, numbers, and list. Whatever single elements are stored will be returned as a byte string. For example, if you store 'a' as a UTF-8 string it will be returned as 'b"a"' when retrieved from the server.

- the lrange method of Redis retrieves a range of elements from a redis list:
  - redis.lrange(name, start, end)
  - redis.lrange('mylist', 0, -1) would retrieve all of the elements from the list named 'mylist'

- zip is a built in python function that takes elements from two or more iterable objects and returns an iterator of tuples where the i-th tuple contains the i-th element from each of the input iterables.

