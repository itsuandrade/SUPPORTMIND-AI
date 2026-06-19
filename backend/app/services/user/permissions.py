from backend.app.services.user.exceptions import UnauthorizedUserAccess

class UserPermissionService:

    @staticmethod
    def validate_admin(user):

        if user.role == 'admin':
            return
        
        else:
            raise UnauthorizedUserAccess()