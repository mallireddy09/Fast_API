# 🛍️ Product Recommendation API using FastAPI & PostgreSQL

A lightweight RESTful API to manage and fetch product recommendations, built using **FastAPI**, **PostgreSQL**, and **SQLAlchemy**.

---

## 📚 Table of Contents

- [🔗 References](#-references)
- [📡 API Endpoints](#-api-endpoints)
- [🛠️ Database Schema](#-database-schema)
- [✅ Setup Instructions](#-setup-instructions)
- [📝 FastAPI App](#-fastapi-app)
- [🧪 Testing via Swagger UI](#-testing-via-swagger-ui)
- [📬 Testing via Postman](#-testing-via-postman)
- [🧰 Tools Used](#-tools-used)


---

## 🔗 References

- **FastAPI Docs**: [fastapi.tiangolo.com](https://fastapi.tiangolo.com/tutorial/sql-databases/)
- **SQLAlchemy Docs**: [sqlalchemy.org](https://docs.sqlalchemy.org/en/20/)
- **PostgreSQL Download**: [postgresql.org](https://www.postgresql.org/download/)
- **Python venv**: [python.org/venv](https://docs.python.org/3/library/venv.html)
- **FastAPI Virtual Envs**: [fastapi.tiangolo.com/virtual-environments](https://fastapi.tiangolo.com/virtual-environments/)
- **Visual Studio Code**: [code.visualstudio.com](https://code.visualstudio.com/)
- **Postman Download**: [postman.com](https://www.postman.com/downloads/)

---

## 📡 API Endpoints

### ✅ GET /getProductRecommendations

Returns a list of product recommendation IDs for a given model.

- **URL**: `http://localhost:8000/getProductRecommendations?modelname=ModelX`
- **Response**:

```json
{
  "productRecs": ["P1", "P2", "P3"]
}
```

---

### ✅ GET /getProductRecommendationDetails

Returns full product details for recommendations related to a given model.

- **URL**: `http://localhost:8000/getProductRecommendationDetails?modelname=ModelX`
- **Response**:

```json
{
  "recommendations": [
    { "id": "P1", "name": "Product 1", "description": "Description of Product 1" },
    { "id": "P2", "name": "Product 2", "description": "Description of Product 2" },
    { "id": "P3", "name": "Product 3", "description": "Description of Product 3" }
  ]
}
```

---

### ✅ PUT /addProduct

Adds a new product to the database.

- **URL**: `http://localhost:8000/addProduct`
- **Body**:

```json
{
  "id": "P6",
  "name": "Product 6",
  "description": "A sample product"
}
```

- **Validation**: All fields are required (`id`, `name`, `description`)

---

## 🛠️ Database Schema

### 📂 Database: `Recommendations`

#### 📄 Table: `products`

| Column      | Type | Description            |
|-------------|------|------------------------|
| id          | TEXT | Primary Key            |
| name        | TEXT | Product Name (Required)|
| description | TEXT | Description (Required) |

#### 📄 Table: `product_recommendations`

| Column        | Type | Description                            |
|---------------|------|----------------------------------------|
| model_name    | TEXT | Primary Key                            |
| list_of_recs  | TEXT | JSON array string (e.g., '["P1","P2"]') |

---

## ✅ Setup Instructions

### 1. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\\Scripts\\activate
```

### 2. Install Required Packages

```bash
pip install fastapi[all] sqlalchemy psycopg2
```

### 3. Create PostgreSQL Database

Using `psql` or `pgAdmin`:

#### 🔸 Create Database

```sql
CREATE DATABASE "Recommendations";
```

#### 🔸 Create Tables

```sql
-- Product Table
CREATE TABLE products (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL
);

-- Product Recommendations Table
CREATE TABLE product_recommendations (
    model_name TEXT PRIMARY KEY,
    list_of_recs TEXT NOT NULL  -- Store as JSON string like '["P1", "P2"]'
);
```

#### 🔸 Insert Sample Data

```sql
-- Insert Products
INSERT INTO products (id, name, description) VALUES
('P1', 'Product 1', 'Description of Product 1'),
('P2', 'Product 2', 'Description of Product 2'),
('P3', 'Product 3', 'Description of Product 3'),
('P4', 'Product 4', 'Description of Product 4'),
('P5', 'Product 5', 'Description of Product 5');

-- Insert Recommendations
INSERT INTO product_recommendations (model_name, list_of_recs) VALUES
('ModelX', '["P1", "P2", "P3"]'),
('ModelY', '["P3", "P4"]'),
('ModelZ', '["P5"]');
```

---

## 📝 FastAPI App

Create a file `main.py` and implement your FastAPI logic there.

```python
# main.py
# -------
# (Insert your FastAPI logic here)
```

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

---

## 🧪 Test URLs via Swagger UI

### 1. Start FastAPI Server

```bash
uvicorn main:app --reload
```

### 2. Open Swagger UI

Open your browser and navigate to:

```
http://localhost:8000/docs
```

### 3. Test the APIs

#### 🔹 PUT `/addProduct`

- Click **"Try it out"**
- Example request body:

```json
{
  "id": "P6",
  "name": "Product 6",
  "description": "Another test product"
}
```

- Click **"Execute"**

---

#### 🔹 GET `/getProductRecommendations`

- Click **"Try it out"**
- Enter:

```
modelname = ModelX
```

- Click **"Execute"**
- Expected response:

```json
{
  "productRecs": ["P1", "P2", "P3"]
}
```

---

#### 🔹 GET `/getProductRecommendationDetails`

- Click **"Try it out"**
- Enter:

```
modelname = ModelX
```

- Click **"Execute"**
- Expected response:

```json
{
  "recommendations": [
    { "id": "P1", "name": "Product 1", "description": "Description of Product 1" },
    { "id": "P2", "name": "Product 2", "description": "Description of Product 2" },
    { "id": "P3", "name": "Product 3", "description": "Description of Product 3" }
  ]
}
```

---

## 📬 Test the API in Postman

### 1. Make Sure the FastAPI Server is Running

```bash
uvicorn main:app --reload
```

Access the app at: [http://localhost:8000](http://localhost:8000)

---

### 2. Test Endpoints

#### 🔹 PUT `/addProduct`

- **URL**: `http://localhost:8000/addProduct`
- **Method**: `PUT`
- **Body** (raw JSON):

```json
{
  "id": "P10",
  "name": "Product 10",
  "description": "Test product added via Postman"
}
```

- **Expected response**:

```json
{
  "message": "Product added successfully"
}
```

---

#### 🔹 GET `/getProductRecommendations`

- **URL**: `http://localhost:8000/getProductRecommendations?modelname=ModelX`
- **Method**: `GET`
- **Expected response**:

```json
{
  "productRecs": ["P1", "P2", "P3"]
}
```

---

#### 🔹 GET `/getProductRecommendationDetails`

- **URL**: `http://localhost:8000/getProductRecommendationDetails?modelname=ModelX`
- **Method**: `GET`
- **Expected response**:

```json
{
  "recommendations": [
    { "id": "P1", "name": "Product 1", "description": "Description of Product 1" },
    { "id": "P2", "name": "Product 2", "description": "Description of Product 2" },
    { "id": "P3", "name": "Product 3", "description": "Description of Product 3" }
  ]
}
```


---

## 🧰 Tools Used

- **FastAPI**: A modern web framework for building APIs with Python. It uses Python’s type hints to validate data and automatically generates interactive documentation, making API development faster and easier.
- **SQLAlchemy**: A popular Object-Relational Mapping (ORM) library for Python that makes it easier to work with databases. Instead of writing a lot of SQL code, you can use Python classes and objects to interact with your data. It works with many types of databases, so you can easily switch between them if needed.
- **PostgreSQL**: Open-source relational database management system that is used for storing and managing data.

---

> 💡 Feel free to fork, clone, or contribute to this project!
