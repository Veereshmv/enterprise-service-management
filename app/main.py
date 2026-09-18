from fastapi import Depends, FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models import Ticket

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Enterprise Service Desk",
    version="1.0.0"
)


app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)


class TicketCreate(BaseModel):
    title: str
    description: str
    ticket_type: str
    priority: str


class TicketUpdate(BaseModel):
    status: str
    support_update: str


@app.get("/", include_in_schema=False)
def root():
    return FileResponse("app/static/index.html")


@app.get("/support", include_in_schema=False)
def support_page():
    return FileResponse("app/static/support.html")


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/tickets")
def create_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db)
):
    new_ticket = Ticket(
        title=ticket.title,
        description=ticket.description,
        ticket_type=ticket.ticket_type,
        priority=ticket.priority,
        status="NEW"
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return new_ticket


@app.get("/tickets")
def get_tickets(db: Session = Depends(get_db)):
    return db.query(Ticket).order_by(Ticket.id.desc()).all()


@app.put("/tickets/{ticket_id}")
def update_ticket(
    ticket_id: int,
    ticket_update: TicketUpdate,
    db: Session = Depends(get_db)
):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    if not ticket:
        return {
            "error": "Ticket not found"
        }

    ticket.status = ticket_update.status
    ticket.support_update = ticket_update.support_update

    db.commit()
    db.refresh(ticket)

    return ticket