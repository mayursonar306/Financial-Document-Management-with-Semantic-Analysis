# Financial Document Management System with Semantic Search

## Project Overview

This project is a FastAPI-based Financial Document Management System with AI-powered semantic search capabilities.

The system allows organizations to:

* Upload and manage financial documents
* Store document metadata in MySQL
* Implement JWT-based authentication and RBAC
* Perform semantic search using embeddings and vector databases
* Retrieve relevant financial insights from uploaded documents

The project follows a Retrieval-Augmented Generation (RAG) architecture using Sentence Transformers and ChromaDB.

---

# Features

## Authentication & Authorization

* User Registration
* User Login
* JWT Authentication
* Protected APIs
* Role-Based Access Control (RBAC)

Supported Roles:

* Admin
* Analyst
* Auditor
* Client

---

# Document Management

* Upload PDF financial documents
* Store document metadata
* Retrieve all documents
* Retrieve document by ID
* Delete uploaded documents

Document Metadata Includes:

* title
* company_name
* document_type
* uploaded_by
* created_at

---

# RAG & Semantic Search

Implemented semantic search using Sentence Transformers and ChromaDB with reranking logic.

RAG Pipeline:

Document → Text Extraction → Chunking → Embeddings → Vector Database → Semantic Search

Features:

* PDF text extraction
* Semantic chunking
* Embedding generation
* ChromaDB vector storage
* Semantic similarity search
* Lightweight reranking system

---

# Tech Stack

## Backend

* FastAPI
* Python
* SQLAlchemy
* MySQL

## Authentication

* JWT Tokens
* Passlib

## AI / RAG

* Sentence Transformers
* ChromaDB
* LangChain Text Splitters
* PyPDF

---

# Project Structure

```txt
project/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   ├── rag/
│   ├── database.py
│   └── main.py
│
├── uploads/
├── requirements.txt
├── README.md
└── .env.example
```

---

# Installation & Setup

## 1. Clone Repository

```bash
git clone <your-github-repo-link>
```

```bash
cd financial-document-management-rag
```

---

# 2. Create Virtual Environment

## Windows

```bash
python -m venv venv
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

---

# 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 4. Configure Environment Variables

Create a `.env` file in project root.

Example:

```env
DATABASE_URL=mysql+pymysql://root:password@localhost/financial_db

SECRET_KEY=mysecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

# 5. Create MySQL Database

Run in MySQL:

```sql
CREATE DATABASE financial_db;
```

---

# 6. Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

---

# API Documentation

Swagger UI:

```txt
http://127.0.0.1:8000/docs
```

---

# Main APIs

## Authentication APIs

| Method | Endpoint       |
| ------ | -------------- |
| POST   | /auth/register |
| POST   | /auth/login    |

---

## Document APIs

| Method | Endpoint          |
| ------ | ----------------- |
| POST   | /documents/upload |
| GET    | /documents        |
| GET    | /documents/{id}   |
| DELETE | /documents/{id}   |

---

## RAG APIs

| Method | Endpoint                 |
| ------ | ------------------------ |
| POST   | /rag/index-document/{id} |
| POST   | /rag/search              |

---

# Semantic Search Example

Example Query:

```txt
financial risk related to debt ratio
```

The system retrieves the most semantically relevant chunks from uploaded financial documents.

---
