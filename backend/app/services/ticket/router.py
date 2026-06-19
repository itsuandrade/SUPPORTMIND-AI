from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.core.dependencies import get_current_user
from backend.app.services.ticket.schema import *
from backend.app.services.ticket.service import TicketService
from backend.app.services.ticket.exceptions import *
from backend.app.services.user.model import User

#DEFINES ROUTER:

ticket_router = APIRouter(
    prefix='/tickets',
    tags=['Tickets']
)

#SERVICES:

def get_ticket_service(db: Session = Depends(get_db)) -> TicketService:
    return TicketService(db)

#ROUTES:

@ticket_router.post('/', response_model=TicketResponse)
def create_ticket(new_ticket: TicketCreate,
                  user: User = Depends(get_current_user),
                  ticket_service = Depends(get_ticket_service)) -> TicketResponse:
    
    ticket = ticket_service.create_ticket(new_ticket, user)
    return ticket

@ticket_router.get('/', response_model=list[TicketResponse])
def get_tickets(user: User = Depends(get_current_user),
                ticket_service = Depends(get_ticket_service)) -> list[TicketResponse]:
    
    tickets = ticket_service.list_all(user)
    return tickets

@ticket_router.get('/me', response_model=list[TicketResponse])
def get_user_tickets(user: User = Depends(get_current_user),
                     ticket_service: TicketService = Depends(get_ticket_service)) -> list[TicketResponse]:
    
    tickets = ticket_service.get_user_tickets(user)
    return tickets

@ticket_router.get('/{ticket_id}', response_model=TicketResponse)
def get_ticket(ticket_id: int,
               user: User = Depends(get_current_user),
               ticket_service = Depends(get_ticket_service)) -> TicketResponse:
    
    ticket = ticket_service.get_by_id(ticket_id, user)      
    return ticket

@ticket_router.put('/{ticket_id}', response_model=TicketResponse)
def update_ticket(ticket_id: int, update: TicketUpdate,
                  user: User = Depends(get_current_user),
                  ticket_service = Depends(get_ticket_service)) -> TicketResponse:
    
    updated_ticket = ticket_service.update_ticket(ticket_id, update, user)
    return updated_ticket

@ticket_router.delete('/{ticket_id}')
def delete_ticket(ticket_id: int, 
                  user: User = Depends(get_current_user),
                  ticket_service = Depends(get_ticket_service)):
    
    ticket_service.delete_ticket(ticket_id, user)
    return {'message': f'Ticket deleted succesfully.'}
