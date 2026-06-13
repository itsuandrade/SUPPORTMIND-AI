from sqlalchemy.orm import Session

from backend.app.services.ticket.repository import TicketRepository
from backend.app.services.ticket.exceptions import TicketNotFound


class TicketService():

    def __init__(self, db: Session):
        self.repository = TicketRepository(db)

    def create_ticket(self, new_ticket):

        ticket = self.repository.create(new_ticket)
        
        # category = ai_service.classify(ticket)

        # ticket = repository.update_category(
        #     ticket.id,
        #     category
        # )

        return ticket
    
    def update_ticket(self,ticket_id, update):
        updated_ticket = self.repository.update(ticket_id, update)
        return updated_ticket
    
    def delete_ticket(self, ticket_id):

        deleted = self.repository.delete(ticket_id)
                
        if not deleted:
            raise TicketNotFound()
    
        return deleted
    
    def list_all(self):
        tickets = self.repository.list_all()
        return tickets
    
    def get_by_id(self, ticket_id):
        ticket = self.repository.get_by_id(ticket_id)
        return ticket