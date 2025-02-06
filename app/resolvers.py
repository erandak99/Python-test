import strawberry
from sqlalchemy import select
from typing import List, Optional

from .models import Product
from .database import async_session


# Define separate output and input types
@strawberry.type
class RatingType:
    rate: float
    count: int


@strawberry.input  
class RatingInput:
    rate: float
    count: int


@strawberry.type
class ProductType:
    id: int
    title: str
    price: float
    description: str
    category: str
    image: str
    rating: RatingType


@strawberry.input 
class ProductInput:
    title: str
    price: float
    description: str
    category: str
    image: str
    rating: RatingInput 


@strawberry.type
class Query:
    @strawberry.field
    async def products(
        self, search: Optional[str] = None, limit: int = 10, offset: int = 0
    ) -> List[ProductType]: 
        async with async_session() as session:
            query = select(Product)
            if search:
                query = query.where(Product.title.contains(search))
            query = query.limit(limit).offset(offset)
            result = await session.execute(query)
            products = result.scalars().all()

            for product in products:
                if isinstance(product.rating, dict):
                    product.rating = RatingType(**product.rating)

            return products

    @strawberry.field
    async def product(self, id: int) -> Optional[ProductType]: 
        async with async_session() as session:
            result = await session.execute(select(Product).where(Product.id == id))
            product = result.scalars().first()

            if product and isinstance(product.rating, dict):
                product.rating = RatingType(**product.rating)

            return product


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_product(self, product_data: ProductInput) -> ProductType:
       async with async_session() as session:
        product_dict = product_data.__dict__.copy() 
        product_dict["rating"] = product_data.rating.__dict__ 
        # Create SQLAlchemy object
        product = Product(**product_dict) 
        session.add(product)
        await session.commit()
        await session.refresh(product)
        return product
    
    async def create_test_product(self, product_data: dict) -> Product:
     async with async_session() as session:
        product = Product(**product_data)
        session.add(product)
        await session.commit()
        await session.refresh(product)
        return product

    @strawberry.mutation
    async def update_product(
        self, id: int, product_data: ProductInput
    ) -> Optional[ProductType]:
        async with async_session() as session:
            result = await session.execute(select(Product).where(Product.id == id))
            product = result.scalars().first()

            if product:
                product_dict = product_data.__dict__.copy()

                product_dict["rating"] = product_data.rating.__dict__

                for key, value in product_dict.items():
                    setattr(product, key, value)

                # Commit the update to the database
                await session.commit()
                await session.refresh(product)

                return product
            return None


schema = strawberry.Schema(query=Query, mutation=Mutation)