from fastapi import FastAPI

app=FastAPI()
@app.get("/hello")
def say_hello():
    return{"Message":"Hello world"}