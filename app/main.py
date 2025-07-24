from fastapi import FastAPI
from app.routers import todo
from app.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the ToDo API"}
app.include_router(todo.router, prefix="/todos", tags=["todos"])


