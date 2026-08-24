from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

# Home route
@app.get('/')
def home():
    return {"message": "Welcome to the FastAPI application!"}

# About route
@app.get('/about')
def about():
    return {"message": "This is a simple about page."}

# Users Route
@app.get('/users/{user_id}')
def get_users(user_id: int):
    return {
        "user_id": user_id,
        "name": f"User {user_id}"
    }

@app.get('/usersquery')
def get_users_query(name: str = "Guest"):
    return {
        "name": f"User {name}"
    }

@app.get('/products')
def get_products(limit: int = 10):
    return {
        "limit": limit
    }

@app.get('/items')
def get_items(name: str, price: int = 0):
    return {
        "name": name,
        "price": price
    }

@app.post('/create-user')
def create_user(name: str, age: int):
    return {
        "name": name,
        "age": age
    }

@app.post('/createuser')
def create_user(user: User):
    return {
        "message": "User Created",
        "data": user
    }


