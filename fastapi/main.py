from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime
from pathlib import Path
import json

from utils import add_to_file, open_file


class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    text: str | None = Field(None, max_length=500)
    priority: int = Field(3, ge=1, le=5)
    is_done: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)


class TodoUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=100)
    text: str | None = Field(None, max_length=500)
    priority: int | None = Field(None, ge=1, le=5)
    is_done: bool | None = None


app = FastAPI()

next_id = 1

if not Path('data.json').exists():
    with open("data.json", 'w', encoding="utf-8") as f:
        json.dump({}, f, ensure_ascii=False, indent=4)

@app.post('/todos')
async def post_todo(todo: TodoCreate):
    global next_id
    await add_to_file(todo.model_dump(mode='json'), next_id)
    next_id += 1
    return todo

@app.get('/todos')
def get_todos():
    data = open_file()
    return list(data.values())


@app.get('/todos/{todo_id}')
def get_todo(todo_id):
    data = open_file()
    if todo_id not in data:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return data[todo_id]

@app.patch('/todos/{todo_id}')
async def patch_todo(todo_id, todo_update: TodoUpdate):
    data = open_file()

    if todo_id not in data:
        raise HTTPException(status_code=404, detail="Задача не найдена")

    todo = data[todo_id]
    update_data = todo_update.model_dump(exclude_unset=True)

    for k, v in update_data.items():
        if v is not None:
            todo[k] = v

    await add_to_file(todo, todo_id)

    return {"message": f"Задача с id = {todo_id} обновлена"}

@app.delete('/todos/{todo_id}')
async def delete_todo(todo_id):
    data = open_file()

    if todo_id not in data:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    del data[todo_id]
    await add_to_file(data)

    return {"message": f"Задача с id = {todo_id} удалена"}