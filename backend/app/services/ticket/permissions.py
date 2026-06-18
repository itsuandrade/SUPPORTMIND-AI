from backend.app.services.ticket.exceptions import UnauthorizedTicketAccess

class TicketPermissionService:

    @staticmethod
    def validate_admin(user):

        if user.role == 'admin':
            return
        
        else:
            raise UnauthorizedTicketAccess()

    @staticmethod
    def validate_owner_or_admin(ticket, user):

        if user.role == 'admin':
            return
        
        if ticket.user_id != user.id:
            raise UnauthorizedTicketAccess()