# Product API Service

# Author: Eranda Ekanayake
# Date: 02/05/2025

## Setup

1. **Create a virtual environment**  
   ```bash
   python3 -m venv venv  # On Windows use `python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate

2. **Install Dependancies**  
pip install -r requirements.txt

3. **Start Application**  
uvicorn app.main:app --reload
goto: http://127.0.0.1:8000/graphql


4. **Run Test Case**
PYTHONPATH=. pytest tests/

5. **Queries & Mutations**

Mutation 1: Create a New Product

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

Mutation 2: Update an Existing Product

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

Query 1: Retrieve a Single Product by ID

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

Query 2: Retrieve All Products (With Search & Pagination)


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

