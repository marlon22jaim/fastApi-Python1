from fastapi import FastAPI

app = FastAPI()


# path operation decorator
@app.get("/")
# path operation function
def home():
    return {"hello": "World"}
