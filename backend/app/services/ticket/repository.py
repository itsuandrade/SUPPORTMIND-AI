from sqlalchemy.orm import Session
from datetime import datetime, UTC

from backend.app.services.ticket.model import Ticket
from backend.app.services.ticket.schema import TicketUpdate

class TicketRepository():

    def __init__(self, db: Session):
        self.db = db

    def create(self, new_ticket) -> Ticket:

        ticket = Ticket(
            title = new_ticket.title,
            description = new_ticket.description,
            category = 'general',
            status = 'open',
            priority = 'low',
            created_at = datetime.now(UTC)
            )

        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)

        return ticket
    
    def update(self, ticket_id: int, update) -> Ticket:

        ticket = self.db.query(Ticket).filter(Ticket.id == ticket_id).first()

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
    
    def delete(self, ticket_id: int) -> bool:

        ticket = self.db.query(Ticket).filter(Ticket.id == ticket_id).first()

        self.db.delete(ticket)
        self.db.commit()

        return True

    def list_all(self):
        tickets = self.db.query(Ticket).all()
        return tickets

    def get_by_id(self, ticket_id: int):
        ticket = self.db.query(Ticket).filter(Ticket.id == ticket_id).first()
        return ticket

