from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import ValidationError

from app.core.database import engine, SessionLocal, Base
from app.services.ticket.schema import TicketCreate
from app.services.ticket.service import TicketService

app = FastAPI()
Base.models.create

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    

@app.get('/')
def health_check():
    return {
        'project': "SupportMind AI",
        'status': "Running"
    }

@app.post('/create_ticket')
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):

    try:
        ticket_service = TicketService()

        new_ticket = ticket_service.create_ticket(
            session=db,
            title=ticket.title,
            description=ticket.description
        )

        return new_ticket
    
    except ValidationError:
        raise HTTPException(400, detail='Ticket inválido. Verifique se todos os campos foram preenchidos adequadamente.')

