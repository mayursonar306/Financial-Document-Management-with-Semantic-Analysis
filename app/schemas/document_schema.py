from pydantic import BaseModel
from datetime import datetime

class DocumentResponse(BaseModel):

    id: int
    title: str
    company_name: str
    document_type: str
    file_path: str
    uploaded_by: str
    created_at: datetime

    class Config:
        from_attributes = True