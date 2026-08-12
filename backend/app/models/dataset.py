from sqlalchemy import Column, Integer, String, ForeignKey, DateTime #type: ignore[reportMissingImports]
from datetime import datetime

from app.database import Base

class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String, nullable=False)

    #File stored path in the server
    file_path = Column(String, nullable=False)

    file_type = Column(String, nullable=False)

    #File uploaded time 
    uploaded_at = Column(
        DateTime, 
        
        # datetime used for stored date and time
        default=datetime.utcnow #utcnow returns the current time accordinng UTC
    )
    #Which User owns the dataset
    user_id = Column(
        Integer, 
        ForeignKey("users.id"),
        nullable=False
    )