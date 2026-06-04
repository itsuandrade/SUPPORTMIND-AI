from sqlalchemy.orm import Session
from fastapi import HTTPException

from backend.app.services.ticket.model import Ticket
from backend.app.services.ticket.schema import TicketUpdate
from datetime import datetime, UTC

class TicketRepository():

    def create(self,
               db: Session,
               title: str,
               description: str,
               ) -> Ticket:

        ticket = Ticket(
            title = title,
            description = description,
            category='general',
            status='open',
            priority='low',
            created_at=datetime.now(UTC)
            )

        db.add(ticket)
        db.commit()
        db.refresh(ticket)

        return ticket
    
    def update(self,
               db: Session,
               ticket_id: int,
               update: TicketUpdate) -> Ticket:

        ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

        if update.status:
            ticket.status = update.status
        
        if update.priority:
            ticket.priority = update.priority

        if update.category:
            ticket.category = update.category
        
        ticket.updated_at = datetime.now(UTC)

        db.commit()
        db.refresh(ticket)

        return ticket
    
    def delete(self, db: Session, ticket_id: int) -> bool:

        ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

        db.delete(ticket)
        db.commit()

        return True

    def list_all(self, db: Session):
        tickets = db.query(Ticket).all()
        return tickets

    def get_by_id(self, db: Session, ticket_id: int):
        ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
        return ticket

