from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.services.ticket.schema import *
from backend.app.services.ticket.service import TicketService

ticket_router = APIRouter(
    prefix='/tickets',
    tags=['Tickets']
)

def get_ticket_service(db: Session = Depends(get_db)) -> TicketService:
    return TicketService(db)

@ticket_router.get('/', response_model=list[TicketResponse])
def get_tickets(ticket_service = Depends(get_ticket_service)) -> list[TicketResponse]:
    tickets = ticket_service.list_all()
    return tickets

@ticket_router.post('/', response_model=TicketResponse)
def create_ticket(new_ticket: TicketCreate, ticket_service = Depends(get_ticket_service)) -> TicketResponse:
    ticket = ticket_service.create_ticket(new_ticket)
    return ticket

@ticket_router.get('/{ticket_id}', response_model=TicketResponse)
def get_ticket(ticket_id: int, ticket_service = Depends(get_ticket_service)) -> TicketResponse:

    ticket = ticket_service.get_by_id(ticket_id)    
    
    if ticket:
        return ticket
    else:
        raise HTTPException(404, detail='Ticket não encontrado.')
    

@ticket_router.put('/{ticket_id}', response_model=TicketResponse)
def update_ticket(ticket_id: int, update: TicketUpdate, ticket_service = Depends(get_ticket_service), db: Session = Depends(get_db)) -> TicketResponse:
    updated_ticket = ticket_service.update_ticket(ticket_id, update)
    return updated_ticket

@ticket_router.delete('/{ticket_id}')
def delete_ticket(ticket_id: int, ticket_service = Depends(get_ticket_service), db: Session = Depends(get_db)):
    ticket_service.delete_ticket(ticket_id)
    return {'message': f'Ticket {ticket_id} deletado com sucesso.'}