from sqlalchemy.orm import Session
from backend.app.services.ticket.repository import TicketRepository
from backend.app.services.ticket.permissions import TicketPermissionService
from backend.app.services.ticket.exceptions import TicketNotFound

class TicketService():

    def __init__(self, db: Session):
        self.repository = TicketRepository(db)
        self.permission = TicketPermissionService()

    def _get_ticket_or_raise(self, ticket_id):

        ticket = self.repository._get_by_id(ticket_id)
        
        if not ticket:
            raise TicketNotFound()
        
        return ticket

    def create_ticket(self, new_ticket, user):

        ticket = self.repository.create(new_ticket, user)
        
        # category = ai_service.classify(ticket)

        # ticket = repository.update_category(
        #     ticket.id,
        #     category
        # )

        return ticket
    
    def get_by_id(self, ticket_id, user):
        ticket = self._get_ticket_or_raise(ticket_id)
        self.permission.validate_owner_or_admin(ticket, user)
        return ticket
    
    def list_all(self, user):
        self.permission.validate_admin(user)
        tickets = self.repository.list_all()
        return tickets
 
    def get_user_tickets(self, user):
        tickets = self.repository.get_by_user(user)
        return tickets

    def update_ticket(self, ticket_id, update, user):
        self.permission.validate_admin(user)
        ticket = self._get_ticket_or_raise(ticket_id)
        updated_ticket = self.repository.update(ticket, update)    
        return updated_ticket
        
    def delete_ticket(self, ticket_id, user):
        self.permission.validate_admin(user)
        ticket = self._get_ticket_or_raise(ticket_id)
        deleted = self.repository.delete(ticket)
        return deleted
