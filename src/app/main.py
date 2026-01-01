from fastapi import FastAPI

app = FastAPI(title="Schema Migration Service")

@app.get("/")
def health():
    return {"status": "ok"}
