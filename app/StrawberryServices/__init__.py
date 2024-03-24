import strawberry
from app.StrawberryServices.schema import Query

schema = strawberry.Schema(query=Query)