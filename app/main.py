from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from .resolvers import Query, Mutation
from .database import init_db

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

app = FastAPI()

# Initialize the database & Create the initial tables
@app.on_event("startup")
async def on_startup():
    await init_db() 

app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
def read_root():
    return {"message": "Product API is running!"}
