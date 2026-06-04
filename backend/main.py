from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import ValidationError

from backend.app.core.database import engine, SessionLocal, Base
from backend.app.services.ticket.schema import TicketCreate, TicketUpdate
from backend.app.services.ticket.service import TicketService
from backend.app.services.ticket.model import Ticket
from backend.app.services.ticket.exceptions import *

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    

### Routes

@app.get('/health')
def health_check():
    return {
        'project': "SupportMind AI",
        'status': "ok"
    }

@app.get('/tickets')
def get_tickets(db: Session = Depends(get_db)):
    ticket_service = TicketService()
    tickets = ticket_service.list_all(db)
    return tickets

@app.get('/tickets/{ticket_id}')
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket_service = TicketService()
    ticket = ticket_service.get_by_id(db, ticket_id)    
    
    if ticket:
        return ticket
    else:
        raise HTTPException(404, detail='Ticket não encontrado.')


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

@app.put('/update_ticket/{ticket_id}')
def update_ticket(ticket_id: int, update: TicketUpdate, db: Session = Depends(get_db)):

    ticket_service = TicketService()

    try: 
        updated_ticket = ticket_service.update_ticket(
            session=db,
            ticket_id=ticket_id,
            update=update
        )
        
        return updated_ticket

    except ValidationError:
        raise HTTPException(400, detail='Update inválido. Verifique se todos os campos foram preenchidos adequadamente.')

@app.delete('/delete_ticket/{ticket_id}')
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):

    ticket_service = TicketService()

    try:
        ticket_service.delete_ticket(session = db,
                                     ticket_id = ticket_id)

    except TicketNotFound:
        raise HTTPException(400, detail='Ticket não encontrado!')


    return {'message': f'Ticket {ticket_id} deletado com sucesso.'}