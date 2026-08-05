from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/contact")
def contact():
    return {"message": "Contact us at balakoyyamani@gmail.com"}

@app.get("/about")
def about():    
    return {"message": "This is a sample FastAPI application."}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}