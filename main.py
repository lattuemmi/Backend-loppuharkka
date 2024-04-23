from fastapi import FastAPI

app = FastAPI()

players = {
    
}

@app.get("/players")
def root():
    return {"message": "Hello World"}

