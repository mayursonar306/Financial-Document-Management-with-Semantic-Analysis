from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from datetime import datetime

from app.database import Base

class Document(Base):

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255))

    company_name = Column(String(255))

    document_type = Column(String(100))

    file_path = Column(String(500))

    uploaded_by = Column(String(100))

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )