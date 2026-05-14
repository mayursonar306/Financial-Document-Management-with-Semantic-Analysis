from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    Form,
    HTTPException
)

from sqlalchemy.orm import Session

import shutil
import os

from app.database import get_db

from app.models.document_model import Document

from app.utils.auth_bearer import verify_token

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

UPLOAD_FOLDER = "uploads"

# Upload Document
@router.post("/upload")
def upload_document(
    title: str = Form(...),
    company_name: str = Form(...),
    document_type: str = Form(...),
    file: UploadFile = File(...),
    user=Depends(verify_token),
    db: Session = Depends(get_db)
):

    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files allowed"
        )

    file_location = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    new_document = Document(
        title=title,
        company_name=company_name,
        document_type=document_type,
        file_path=file_location,
        uploaded_by=user["email"]
    )

    db.add(new_document)
    db.commit()
    db.refresh(new_document)

    return {
        "message": "Document uploaded successfully",
        "document_id": new_document.id
    }

# Get All Documents
@router.get("/")
def get_documents(
    user=Depends(verify_token),
    db: Session = Depends(get_db)
):

    documents = db.query(Document).all()

    return documents

# Get Document By ID
@router.get("/{document_id}")
def get_document(
    document_id: int,
    user=Depends(verify_token),
    db: Session = Depends(get_db)
):

    document = db.query(Document).filter(
        Document.id == document_id
    ).first()

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return document

# Delete Document
@router.delete("/{document_id}")
def delete_document(
    document_id: int,
    user=Depends(verify_token),
    db: Session = Depends(get_db)
):

    document = db.query(Document).filter(
        Document.id == document_id
    ).first()

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    if os.path.exists(document.file_path):
        os.remove(document.file_path)

    db.delete(document)
    db.commit()

    return {
        "message": "Document deleted successfully"
    }