import pytest
from app.resolvers import Mutation
from app.database import async_session, Base, engine
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Product
from sqlalchemy import text

@pytest.fixture(autouse=True)
async def setup_db():
    # Create the tables in the database
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    yield
    
    # Drop the tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.mark.asyncio
async def test_create_product():
    mutation = Mutation()
    
    # Define the product data that you want to use for the test
    product_data = {
        "title": "Test Product",
        "price": 9.99,
        "description": "A test product",
        "category": "test",
        "image": "http://test.com/image.jpg",
        "rating": {"rate": 4.5, "count": 100}
    }
    
    # Call the mutation to create the product
    result = await mutation.create_test_product(product_data)
    
    # Assertions to ensure the product was created
    assert result is not None  
    assert result.title == "Test Product" 
    assert result.price == 9.99  
    assert result.description == "A test product" 
    assert result.category == "test"  
    assert result.image == "http://test.com/image.jpg"  
    assert result.rating['rate'] == 4.5  
    assert result.rating['count'] == 100 

    # Check if the product is saved in the database
    async with async_session() as session:
        query = await session.execute("SELECT * FROM products WHERE title = :title", {"title": "Test Product"})
        product_in_db = query.fetchone()
        assert product_in_db is not None 
        assert product_in_db.title == "Test Product"
        assert product_in_db.price == 9.99
        assert product_in_db.description == "A test product"
        assert product_in_db.category == "test"
        assert product_in_db.image == "http://test.com/image.jpg"
        assert product_in_db.rating == '{"rate": 4.5, "count": 100}'  
