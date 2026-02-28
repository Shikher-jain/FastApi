from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Shikher"}

@app.get("/about")
def about():
    return {"message": "This is the about page"}