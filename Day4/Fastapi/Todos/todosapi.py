from fastapi import FastAPI
import json
from pydantic import BaseModel
app=FastAPI()
newtodos={
    "id":5,
    "title":"Go to market"
}
class Todo(BaseModel):
    title:str

def load_todos():
    with open('todos.json', 'r') as file:
       data = json.load(file)
       return data


def save_todos(newdata):
    data=load_todos()
    data.append(newdata)
    with open('todos.json', 'w') as file:
        json.dump(data,file,indent=2)
         
save_todos(newtodos)
@app.get("/gettodos")
def get_todos():
    data=load_todos()
    return data


@app.post("createtodos")
def create_todos(newtodos:Todo):
    todos = load_todos()
    new_id = max([t["id"] for t in todos], default=0) + 1
    new_todo = {"id": new_id, "task": newtodos.task}
    todos.append(new_todo)
    save_todos(todos)
    return new_todo

