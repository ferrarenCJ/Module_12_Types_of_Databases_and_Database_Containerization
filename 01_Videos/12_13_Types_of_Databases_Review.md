# Video 12.13: Types of Databases: Review

## Overview

This video serves as the conclusion to Module 12 and reviews the major database technologies covered throughout the module. Dr. Sanchez emphasizes that while MySQL, MongoDB, Redis, Cassandra, and Firebase represent important database categories, they are only a small subset of the many database technologies available today.

The video also introduces **The Apache Software Foundation**, an organization that supports numerous open-source software projects, including many widely used data engineering and database technologies.

---

## Video Information

**Video 12.13: Types of Databases: Review**

**Duration:** 02:51

---

# Module 12 Database Review

During this module, five different database technologies were explored:

## 1. MySQL

### Database Type

```text
Relational Database
```

### Data Model

```text
Tables
Rows
Columns
Relationships
```

### Access Method

```sql
SQL
```

### Typical Use Cases

- Financial systems
- Customer relationship management
- Inventory management
- Enterprise applications

### Key Strengths

- Structured data
- ACID transactions
- Strong data integrity
- Mature SQL ecosystem

---

## 2. MongoDB

### Database Type

```text
Document Database
```

### Data Model

```json
{
  "name": "John Smith",
  "department": "Engineering"
}
```

### Storage Format

```text
JSON/BSON Documents
```

### Typical Use Cases

- Web applications
- Content management systems
- Product catalogs
- Mobile applications

### Key Strengths

- Flexible schema
- Rapid development
- Easy scalability

---

## 3. Redis

### Database Type

```text
Key-Value Database
```

### Data Model

```text
Key → Value
```

Example:

```text
user:1001
     ↓
John Smith
```

### Typical Use Cases

- Caching
- Session storage
- Real-time analytics
- Messaging systems

### Key Strengths

- Extremely fast performance
- In-memory storage
- Simplicity

---

## 4. Cassandra

### Database Type

```text
Distributed Scalable Database
```

### Characteristics

- Distributed architecture
- Fault tolerance
- Horizontal scaling
- High availability

### Typical Use Cases

- Telecommunications
- IoT platforms
- Large-scale analytics
- Time-series applications

### Key Strengths

- Massive scalability
- No single point of failure
- High availability

---

## 5. Firebase

### Database Type

```text
Serverless Cloud Database
```

### Characteristics

- Managed infrastructure
- Automatic scaling
- Real-time synchronization
- Cloud-hosted

### Typical Use Cases

- Mobile applications
- Web applications
- Real-time collaboration
- Field data collection systems

### Key Strengths

- No server management
- Rapid development
- Real-time updates

---

# Database Categories Covered

```text
MySQL
    ↓
Relational Database

MongoDB
    ↓
Document Database

Redis
    ↓
Key-Value Database

Cassandra
    ↓
Distributed Database

Firebase
    ↓
Serverless Cloud Database
```

---

# Choosing the Right Database

A major lesson from Module 12 is that there is no single database that is best for every scenario.

Database selection depends on:

### Data Structure

- Structured
- Semi-structured
- Unstructured

### Performance Requirements

- Transaction volume
- Query complexity
- Response times

### Scalability Requirements

- Vertical scaling
- Horizontal scaling

### Availability Requirements

- Fault tolerance
- Disaster recovery
- Geographic distribution

### Administration Requirements

- Self-managed
- Containerized
- Serverless

---

# The Apache Software Foundation

The video introduces:

```text
The Apache Software Foundation (ASF)
```

### Purpose

A nonprofit organization that supports open-source software projects.

Website:

```text
https://www.apache.org
```

---

## Why Apache Matters

The Apache Software Foundation hosts many technologies used by:

- Data engineers
- Data scientists
- Software developers
- Cloud architects

Many industry-standard tools originated from Apache projects.

---

# Examples of Apache Projects

## Apache Cassandra

Already studied in Module 12.

Type:

```text
Distributed Database
```

---

## Apache Hadoop

Type:

```text
Big Data Processing Framework
```

Purpose:

- Distributed storage
- Large-scale data processing

---

## Apache Spark

Type:

```text
Distributed Data Processing Engine
```

Purpose:

- Batch processing
- Streaming analytics
- Machine learning

---

## Apache Kafka

Type:

```text
Event Streaming Platform
```

Purpose:

- Real-time data pipelines
- Messaging systems

---

## Apache Airflow

Type:

```text
Workflow Orchestration Platform
```

Purpose:

- Data pipeline scheduling
- Workflow automation

---

# Importance for Data Engineers

The Apache ecosystem provides many of the technologies used in modern data platforms.

Examples include:

```text
Storage
Processing
Streaming
Scheduling
Analytics
Databases
```

Many future topics in data engineering build upon Apache projects.

---

# Module 12 Technology Comparison

| Technology | Category | Primary Strength |
|------------|------------|------------|
| MySQL | Relational | Structured transactions |
| MongoDB | Document | Flexible schema |
| Redis | Key-Value | High performance |
| Cassandra | Distributed | Scalability and availability |
| Firebase | Serverless Cloud | Managed infrastructure and real-time updates |

---

# Key Takeaways

- Module 12 introduced five major categories of databases.
- Different databases are optimized for different business and technical requirements.
- Relational databases remain important for structured transactional systems.
- NoSQL databases provide flexibility and scalability for modern applications.
- Distributed databases support very large-scale environments.
- Serverless databases reduce infrastructure management responsibilities.
- The Apache Software Foundation supports many influential open-source projects used throughout the data engineering industry.
- Learning one database technology provides a foundation for understanding many others.

---

# Module Theme

> Successful data engineers understand that different database technologies solve different problems. Selecting the appropriate database requires evaluating data structure, scalability, performance, operational requirements, and business needs while leveraging modern open-source technologies such as those available through The Apache Software Foundation.