import strawberry

@strawberry.type
class RatingType:
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
    rating: RatingType
