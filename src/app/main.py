from fastapi import FastAPI

app = FastAPI(title="Data Quality Testing Service")

@app.get("/")
def health():
    return {"status": "ok", "message": "Data Quality Testing Service is running"}