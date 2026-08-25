from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    title: str
    completed: bool


@app.post('/todos')
def create_todo(todo: Todo):
    todos.append(todo)
    return {
        "message": "Todo Created",
        "data": todo
    }

@app.get('/todos')
def get_todos():
    return todos

@app.get('/todos/{todo_id}')
def get_todo(todo_id: int):
    for todo in todos:
        if(todo.id == todo_id):
            return todo

    return {"message": "Todo not found"}

@app.put('/todos/{todo_id}')
def update_todo(todo_id: int, updated_todo: Todo):
    for i, todo in enumerate(todos):
        if(todo.id == todo_id):
            todos[i] = updated_todo
            return updated_todo

    return {"message": "Todo not found"}

@app.delete('/todos/{todo_id}')
def delete_todo(todo_id: int):
    for i, todo in enumerate(todos):
        if(todo.id == todo_id):
            todos.pop(i)
            return {"message": "Todo deleted"}

    return {"message": "Todo not found"}