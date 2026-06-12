from fastapi import FastAPI


print("MAIN.PY LOADED")

from routes.content import (
    router as content_router
)

app = FastAPI()

app.include_router(
    content_router,
    prefix="/content",
    tags=["Content"]
)
@app.get("/")
def home():
    return {"message": "Brandforge API Running"}

print(app.routes)