# NoSQL

- NoSQL differs from traditional relational database management systems (RDBMS). SQL is a query language used by RDBMS. Relational databases rely on tables, columns, rows, or schemas to organize and retrieve data. NoSQL is useful for storing unstructured data such as session data, user data, chat data, messaging data, IoT device data, and large objects such as video and images.

- There are four main categories of NoSQL databases:
  - Key-value: emphasize simplicity and are very useful in accelerating an application to support high-speed read and write processing of non-transactional data. Stored values can be any type of binary object (text, video, JSON document, etc.) and are accessed via a key.

  - Document stores: Document databases typically store self-describing JSON, XML, and BSON documents. They are similar to key-value stores, but in this case, a value is a single document that stores all data related to a specific key. Popular fields in the document can be indexed to provide fast retrieval without knowing the key. Each document can have the same or a different structure.

  - Wide-column stores: Wide-column NoSQL databases store data in tables with rows and columns similar to RDBMS, but names and formats of columns can vary from row to row across the table. Wide-column databases group columns of related data together. A query can retrieve related data in a single operation because only the columns associated with the query are retrieved. In an RDBMS, the data would be in different rows stored in different places on disk, requiring multiple disk operations for retrieval.

  - Graph stores: A graph database uses graph structures to store, map, and query relationships. They provide index-free adjacency, so that adjacent elements are linked together without using an index.

- Some NoSQL databases can be multi-modal meaning that they use some combination of the four main types of NoSQL db.

- Advantages of NoSQL of traditional RDBMS include scalability, performance, availability, and flexibility

- sources:
  - https://riak.com/resources/nosql-databases/