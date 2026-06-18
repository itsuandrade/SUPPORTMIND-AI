from sqlalchemy.orm import Session
from datetime import datetime, UTC

from backend.app.services.ticket.model import Ticket
from backend.app.services.ticket.exceptions import *

class TicketRepository():

    def __init__(self, db: Session):
        self.db = db

    def create(self, new_ticket, user_id) -> Ticket:

        ticket = Ticket(
            title = new_ticket.title,
            description = new_ticket.description,
            category = 'general',
            status = 'open',
            priority = 'low',
            created_at = datetime.now(UTC),
            user_id = user_id
            )

        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)

        return ticket
    
    def _get_by_id(self, ticket_id: int) -> Ticket:
        ticket = self.db.query(Ticket).filter(Ticket.id == ticket_id).first()
        return ticket
    
    def list_all(self) -> list[Ticket]:
        tickets = self.db.query(Ticket).all()
        return tickets

    def get_by_user(self, user):
        tickets = user.tickets
        return tickets
    
    def update(self, ticket, update) -> Ticket:

        if update.status:
            ticket.status = update.status
        
        if update.priority:
            ticket.priority = update.priority

        if update.category:
            ticket.category = update.category
        
        ticket.updated_at = datetime.now(UTC)

        self.db.commit()
        self.db.refresh(ticket)

        return ticket

    def delete(self, ticket) -> bool:
        self.db.delete(ticket)
        self.db.commit()
        return True