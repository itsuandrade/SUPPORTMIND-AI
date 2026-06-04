from backend.app.services.ticket.repository import TicketRepository
from backend.app.services.ticket.exceptions import *

repository = TicketRepository()

class TicketService():

    def create_ticket(self, session, title, description):

        ticket = repository.create(db=session,
                                   title=title,
                                   description=description)
        
        # category = ai_service.classify(ticket)

        # ticket = repository.update_category(
        #     ticket.id,
        #     category
        # )

        return ticket
    
    def update_ticket(self, session, ticket_id, update):

        updated_ticket = repository.update(db=session,
                                           ticket_id=ticket_id,
                                           update=update)
        
        return updated_ticket
    
    def delete_ticket(self, session, ticket_id):

        deleted = repository.delete(db=session,
                                        ticket_id=ticket_id)
                
        if not deleted:
            raise TicketNotFound()
    
        return deleted
    
    def list_all(self, session):

        tickets = repository.list_all(session)

        return tickets
    
    def get_by_id(self, session, ticket_id):

        ticket = repository.get_by_id(db=session,
                                      ticket_id=ticket_id)
        
        return ticket