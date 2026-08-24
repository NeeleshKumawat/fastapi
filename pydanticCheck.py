from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Address(BaseModel):
    city: str
    pincode: int
 
class User(BaseModel):
    name: str
    age: int
    email: str
    address: Address

@app.post("/createuser")
def  createUser(user: User):
      return {
        "message": "User Created",
        "data": user
      }

@app.post("/create_user")
def create_user(user: User):
  return {
    "data": User
  }