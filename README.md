# Financial Document Management System with Semantic Search

## Project Overview

This project is a FastAPI-based Financial Document Management System with AI-powered semantic search capabilities.

The system allows organizations to:

* Upload and manage financial documents
* Store document metadata in MySQL
* Implement JWT-based authentication and RBAC
* Perform semantic search using embeddings and vector databases
* Retrieve relevant financial insights from uploaded documents
---

# Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/mayursonar306/Financial-Document-Management-with-Semantic-Analysis.git
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
