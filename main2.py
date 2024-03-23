from fastapi import Response, status
from fastapi.responses import JSONResponse

class ProfessionModel:
    id = 1
    data = {}
    def __init__(self, name, email, work):
        self.name = name
        self.email = email
        self.work = work

    def save():
        data[id] = {}
        data[id]['name']=self.name
        data[id]['email']=self.email
        data[id]['work']=self.work
        id+=1

class Professionals:

    @app.get('/professional/{id}', status_code=302)
    async def method_name(id: int, response: Response):

        if ProfessionModel.data[id] == id:
            json_compatible_item_data = jsonable_encoder(item)
            return JSONResponse(content=json_compatible_item_data, statuscode=status.HTTP_302_FOUND)
        else:
            return JSONResponse(content=json_compatible_item_data, statuscode=status.HTTP_404_NOT_FOUND)

