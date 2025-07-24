from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: str = ""
    completed: bool = False

class ToDoCreate(TodoBase):
    pass

class ToDoUpdate(TodoBase):
    pass

class ToDoOut(TodoBase):
    id: int

    class Config:
        form_attributes = True
