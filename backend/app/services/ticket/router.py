from fastapi import APIRouter, HTTPException, Depends
from backend.app.core.database import get_db
from sqlalchemy.orm import Session

from backend.app.services.ticket.schema import TicketCreate, TicketUpdate, TicketResponse
from backend.app.services.ticket.service import TicketService
from backend.app.services.ticket.exceptions import TicketNotFound

ticket_router = APIRouter(
    prefix='/tickets',
    tags=['Tickets']
)

def get_ticket_service() -> TicketService:
    return TicketService()

@ticket_router.get('/', response_model=list[TicketResponse])
def get_tickets(ticket_service = Depends(get_ticket_service), db: Session = Depends(get_db)) -> list[TicketResponse]:
    tickets = ticket_service.list_all(db)
    return tickets


@ticket_router.post('/', response_model=TicketResponse)
def create_ticket(ticket: TicketCreate, ticket_service = Depends(get_ticket_service), db: Session = Depends(get_db)) -> TicketResponse:

    new_ticket = ticket_service.create_ticket(
                    session=db,
                    title=ticket.title,
                    description=ticket.description
                    )

    return new_ticket

@ticket_router.get('/{ticket_id}', response_model=TicketResponse)
def get_ticket(ticket_id: int, ticket_service = Depends(get_ticket_service), db: Session = Depends(get_db)) -> TicketResponse:

    ticket = ticket_service.get_by_id(db, ticket_id)    
    
    if ticket:
        return ticket
    else:
        raise HTTPException(404, detail='Ticket não encontrado.')
    

@ticket_router.put('/{ticket_id}', response_model=TicketResponse)
def update_ticket(ticket_id: int, update: TicketUpdate, ticket_service = Depends(get_ticket_service), db: Session = Depends(get_db)) -> TicketResponse:

    updated_ticket = ticket_service.update_ticket(
        session=db,
        ticket_id=ticket_id,
        update=update
    )
    
    return updated_ticket

@ticket_router.delete('/{ticket_id}')
def delete_ticket(ticket_id: int, ticket_service = Depends(get_ticket_service), db: Session = Depends(get_db)):

    try:
        ticket_service.delete_ticket(session = db,
                                     ticket_id = ticket_id)

    except TicketNotFound:
        raise HTTPException(400, detail='Ticket não encontrado!')


    return {'message': f'Ticket {ticket_id} deletado com sucesso.'}