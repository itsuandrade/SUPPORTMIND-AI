from sqlalchemy.orm import Session
from model import Ticket
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
            status='open',
            priority='low',
            created_at=datetime.now(UTC)
            )

        db.add(ticket)
        db.commit()
        db.refresh(ticket)

        return ticket
    
