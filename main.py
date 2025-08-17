from fastapi import FastAPI, UploadFile, Form
from api.routes import router

app = FastAPI(title="Speech Translation API")

# Register routes
app.include_router(router)

@app.get("/")
def root():
    return {"message": "✅ Speech Translation API is running!"}
