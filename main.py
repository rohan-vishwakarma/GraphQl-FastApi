from fastapi import FastAPI, status, Response
from enum import Enum
from main2 import Professionals
app = FastAPI()

app.add_api_route('/professional', Professionals.method_name)


user = {}

#  Using enum package

class User(Enum):
    user_id = 1
    name = "rohan"
    age = 21
    profession = "Software Engineer"

class ApiRoutes:

    @app.get("/user/{user_id}", status_code=302)
    async def read_item(user_id: int, response: Response):
        if User.user_id.value == user_id:
            response.status_code=status.HTTP_302_FOUND
            return {
                "status_code": response.status_code,
                "payloads" : {
                    "name" : User.name.value,
                    "profession" : User.profession.value
                }
            }
        else:
            response.status_code=status.HTTP_404_NOT_FOUND
            return {
                "status_code": response.status_code
            }
