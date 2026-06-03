from repository import TicketRepository

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