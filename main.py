from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_demo():
    return "This is FastAPI!"
