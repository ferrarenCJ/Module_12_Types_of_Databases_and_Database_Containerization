# Video 12.1: Introduction and Information

## Overview

Module 12 introduces several database technologies commonly used in modern data engineering environments. Throughout this module, students learn how different database architectures solve different business and technical challenges, how databases can be deployed within containers, and when each database type should be used.

The module focuses on five database technologies:

- MySQL (Relational Database)
- MongoDB (Document Database)
- Redis (Key-Value Database)
- Cassandra (Distributed Scalable Database)
- Firebase (Serverless Cloud Database)

In addition, students learn fundamental concepts related to database containerization and perform hands-on activities using various containerized databases.

---

## Video Information

**Video 12.1: Introduction**

**Duration:** 04:34

Dr. Sanchez introduces the growing importance of data and discusses several major database technologies widely used in industry.

Examples discussed include:

- MySQL
- MongoDB
- Redis
- Cassandra

The video highlights how organizations generate massive amounts of data across industries and why different types of databases have emerged to address different storage, scalability, and performance requirements.

---

## Why Different Database Types Exist

Modern organizations generate data from sources such as:

- Transportation systems
- Energy infrastructure
- Financial services
- E-commerce platforms
- Mobile applications
- Internet of Things (IoT) devices

No single database design is ideal for every use case.

Different database technologies provide advantages depending on:

- Data structure
- Query patterns
- Scalability requirements
- Performance needs
- Availability requirements

---

## Database Technologies Covered

### Relational Databases (MySQL)

Relational databases store structured data in tables using rows and columns.

Characteristics:

- Structured schema
- SQL-based queries
- ACID transactions
- Strong data consistency

Common use cases:

- Banking systems
- ERP systems
- Inventory management
- Customer records

---

### Document Databases (MongoDB)

Document databases store data as JSON-like documents.

Characteristics:

- Flexible schema
- Semi-structured data
- Easy horizontal scaling

Common use cases:

- Content management systems
- Product catalogs
- User profiles
- Web applications

---

### Key-Value Databases (Redis)

Key-value databases store information as key-value pairs.

Characteristics:

- Extremely fast
- In-memory storage
- Simple data retrieval

Common use cases:

- Caching
- Session management
- Real-time applications
- Leaderboards

---

### Distributed Scalable Databases (Cassandra)

Distributed databases spread data across multiple nodes.

Characteristics:

- High availability
- Fault tolerance
- Horizontal scalability

Common use cases:

- IoT platforms
- Large-scale analytics
- Time-series data
- Global applications

---

### Serverless Cloud Databases (Firebase)

Serverless databases are managed cloud services.

Characteristics:

- No server administration
- Automatic scaling
- Managed infrastructure

Common use cases:

- Mobile applications
- Web applications
- Real-time collaboration tools

---

## Database Containerization

A major focus of this module is database containerization.

Containerization allows databases to run inside isolated environments called containers.

Benefits include:

- Consistent deployment environments
- Portability between systems
- Simplified testing
- Easier development workflows
- Faster deployment processes

Students will learn how to:

- Run database containers
- Connect to containerized databases
- Execute queries against containerized environments
- Modify data within containers

---

## Tools Required

Students should verify installation of the following tools before beginning Module 12:

### MySQL

Used for relational database activities.

### Docker

Used for containerization exercises.

### Git Bash (Windows)

May be required for command-line exercises when using Windows.

### Visual Studio Code

Used for database scripts and Python development.

---

## Program Learning Outcomes

This module supports the following program outcomes:

1. Explain key data science and data engineering concepts.
2. Develop and analyze databases using SQL, Python, and modern data engineering tools.

---

## Module Learning Outcomes

By the end of Module 12, students will be able to:

1. Describe applications of various database types.
2. Identify key concepts related to database containerization.
3. Update and delete data in different containerized databases.
4. Identify key concepts