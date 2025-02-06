
# Product API Service

**Author**: Eranda Ekanayake  
**Date**: 02/05/2025

---

## Setup

### Required Python Version: 3.1 or later

### 1. **Create a Virtual Environment**

For Linux/Mac:

```bash
python3 -m venv venv  
source venv/bin/activate
```

For Windows:

```bash
python -m venv venv  
venv\Scriptsctivate
```

### 2. **Install Dependencies**

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

### 3. **Start the Application**

Start the API server with the following command:

```bash
uvicorn app.main:app --reload
```

Once the server is up, you can access the GraphQL playground at:  
[http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql)

### 4. **Run Test Cases**

To run the tests, use:

```bash
PYTHONPATH=. pytest tests/
```

---

## Queries & Mutations

### **Mutation 1: Create a New Product**

This mutation creates a new product with the provided data.

```graphql
mutation {
  createProduct(productData: {
    title: "New Phone",
    price: 699.99,
    description: "A powerful new smartphone",
    category: "electronics",
    image: "http://example.com/phone.jpg",
    rating: { rate: 4.5, count: 120 }
  }) {
    id
    title
    price
    category
  }
}
```

### **Mutation 2: Update an Existing Product**

This mutation updates an existing product by its `id`.

```graphql
mutation {
  updateProduct(id: 1, productData: {
    title: "Updated Laptop",
    price: 1099.99,
    description: "Updated high-performance laptop",
    category: "electronics",
    image: "http://example.com/laptop.jpg",
    rating: { rate: 4.7, count: 250 }
  }) {
    id
    title
    price
  }
}
```

### **Query 1: Retrieve a Single Product by ID**

This query retrieves a single product by its `id`.

```graphql
query {
  product(id: 1) {
    id
    title
    price
    description
    category
    image
    rating {
      rate
      count
    }
  }
}
```

### **Query 2: Retrieve All Products (With Search & Pagination)**

This query retrieves a list of products with search and pagination options.

```graphql
query {
  products(search: "Laptop", limit: 5, offset: 0) {
    id
    title
    price
    description
    category
    image
    rating {
      rate
      count
    }
  }
}
```
