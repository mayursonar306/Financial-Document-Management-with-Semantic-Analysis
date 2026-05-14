from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.document_model import Document

from app.utils.auth_bearer import verify_token

from app.services.pdf_service import (
    extract_text_from_pdf
)

from app.services.chunk_service import (
    chunk_text
)

from app.services.embedding_service import (
    generate_embedding
)

from app.rag.chroma_db import collection

router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)

# Index Document
@router.post("/index-document/{document_id}")
def index_document(
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

    text = extract_text_from_pdf(
        document.file_path
    )

    chunks = chunk_text(text)

    for index, chunk in enumerate(chunks):

        embedding = generate_embedding(chunk)

        collection.add(
            ids=[f"{document_id}_{index}"],
            embeddings=[embedding],
            documents=[chunk],
            metadatas=[
                {
                    "document_id": document_id,
                    "title": document.title
                }
            ]
        )

    return {
        "message": "Document indexed successfully",
        "chunks": len(chunks)
    }

# Semantic Search
@router.post("/search")
def semantic_search(
    query: str,
    user=Depends(verify_token)
):

    query_embedding = generate_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=20
    )

    documents = results["documents"][0]

    
    ranked_results = sorted(
        documents,
        key=lambda doc: doc.lower().count(query.lower()),
        reverse=True
    )

    top_results = ranked_results[:5]

    return {
        "query": query,
        "top_results": top_results
    }