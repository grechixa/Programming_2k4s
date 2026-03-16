from fastapi import FastAPI

app = FastAPI()

@app.post("/users/")
def create_user(username: str, email: str):
    return {

    }