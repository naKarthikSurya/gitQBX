# main.py
from fastapi import FastAPI
from dotenv import load_dotenv
from settings import get_attribute

load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return "Hello World"

@app.get("/value/{variable}")
def read_variable(variable: str):
    value = get_attribute(variable)
    return {variable: value}

# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000)