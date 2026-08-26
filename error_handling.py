from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app =FastAPI()

class UserNotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(UserNotFoundException)
async def user_not_found_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": f"User '{exc.name}' not found."},
    )

@app.get('/getuser/{user_id}')
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=404, detail="User not found")

    return {"user_id": user_id, "name": "John Doe"}

@app.get('/getuser_custom/{name}')
def get_user_custom(name: str):
    if name != "John Doe":
        raise UserNotFoundException(name=name)

    return {"user_id": 1, "name": name}
