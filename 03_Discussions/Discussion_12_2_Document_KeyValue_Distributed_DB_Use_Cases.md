# Required Discussion 12.2: Use Cases for Document, Key-Value, and Distributed Scalable Databases

## Overview

Different types of databases are designed to meet different business needs. Three common NoSQL database types are document databases, key-value databases, and distributed scalable databases.

A **document database**, such as MongoDB, stores data in flexible documents instead of rows and columns. Its main advantage is schema flexibility, allowing documents to have different structures. This makes it useful when data requirements change frequently. A disadvantage is that it can be more challenging to manage complex relationships than in relational databases.

A **key-value database**, such as Redis, stores information as simple key-value pairs. Its biggest advantage is speed because data is stored in memory, allowing extremely fast reads and writes. However, key-value databases are not well suited for complex queries or relationships between data.

A **distributed scalable database**, such as Cassandra, stores data across multiple servers. This provides high availability, fault tolerance, and scalability. The tradeoff is increased complexity in deployment and administration.

For a document database example, a gas utility company could store inspection records in MongoDB because different assets may require different inspection attributes. For a key-value database example, Redis could store customer web-session information to provide fast login and authentication services. For a distributed scalable database example, Cassandra could store millions of IoT sensor readings from utility assets because it can scale across multiple servers while remaining highly available.

Choosing the right database depends on the structure, volume, and access requirements of the data.

---

## Learning Outcome

**Describe applications of various types of databases.**

### Databases Discussed

- MongoDB (Document Database)
- Redis (Key-Value Database)
- Cassandra (Distributed Scalable Database)

### Key Takeaways

- MongoDB offers schema flexibility for evolving data structures.
- Redis provides extremely fast access to data through in-memory storage.
- Cassandra delivers scalability, fault tolerance, and high availability across distributed systems.
- Different business requirements call for different database technologies.

### Word Count

Approximately 220 words.