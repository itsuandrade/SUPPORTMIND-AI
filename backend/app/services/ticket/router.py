from fastapi import APIRouter, HTTPException, Depends
from pydantic import ValidationError
from backend.app.core.database import get_db
from sqlalchemy.orm import Session

from backend.app.services.ticket.schema import TicketCreate, TicketUpdate
from backend.app.services.ticket.service import TicketService
from backend.app.services.ticket.exceptions import TicketNotFound

ticket_router = APIRouter(
    prefix='/tickets',
    tags=['Tickets']
)

@ticket_router.get('/')
def get_tickets(db: Session = Depends(get_db)):
    ticket_service = TicketService()
    tickets = ticket_service.list_all(db)
    return tickets


@ticket_router.post('/create')
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
    

@ticket_router.get('/{ticket_id}')
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket_service = TicketService()
    ticket = ticket_service.get_by_id(db, ticket_id)    
    
    if ticket:
        return ticket
    else:
        raise HTTPException(404, detail='Ticket não encontrado.')
    

@ticket_router.put('/{ticket_id}')
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
    

@ticket_router.delete('/{ticket_id}')
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):

    ticket_service = TicketService()

    try:
        ticket_service.delete_ticket(session = db,
                                     ticket_id = ticket_id)

    except TicketNotFound:
        raise HTTPException(400, detail='Ticket não encontrado!')


    return {'message': f'Ticket {ticket_id} deletado com sucesso.'}