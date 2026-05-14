from fastapi import FastAPI

from app.database import engine, Base

from app.models import (
    test_model,
    user_model
)

from app.routes.auth_routes import router as auth_router
from app.routes.user_routes import router as user_router
from app.routes.role_routes import router as role_router
from app.routes.test_routes import router as test_router
from app.routes.document_routes import router as document_router
from app.routes.rag_routes import router as rag_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(role_router)
app.include_router(test_router)
app.include_router(document_router)
app.include_router(rag_router)

@app.get("/")
def home():
    return {
        "message": "Financial API Running"
    }