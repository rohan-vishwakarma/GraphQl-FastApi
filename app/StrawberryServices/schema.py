import typing
import strawberry
def get_books_for_author(root)->"Author":
    return [Author(name="Micheal Chandler")]

@strawberry.type
class Book:
    title : str
    author : "Rohan"

@strawberry.type
class Author:
    name : str
    books : typing.List[Book] = strawberry.field(resolver=get_books_for_author)

def get_authors(root) -> typing.List[Author]:
    return [Author(name="Michael Crichton")]
    
#-----------------------------------------------------------------------------------------------------------------------------------------


@strawberry.type
class Query:
    authors: typing.List[Author] = strawberry.field(resolver=get_authors)
    books: typing.List[Book] = strawberry.field(resolver=get_books_for_author)