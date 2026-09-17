from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text

from app.database import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    ticket_type = Column(String(50), nullable=False)
    priority = Column(String(20), nullable=False)
    status = Column(String(30), nullable=False, default="NEW")
    support_update = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)