from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    name: str
    age: int

@app.post('/users')
def create_user(user: User):
    users.append(user)
    return {
        "message": "User Created",
        "data": users
    }


@app.put('/users/{user_id}')
def update_user(user_id: int, updated_user: User, notify: bool = False):
    for i, user in enumerate(users):
        if(i == user_id):
            users[i] = updated_user
            return {
                "message": "User Updated",
                "notify": notify,
                "data": users
            } 

    return {"message": "User not found"}