from fastapi import FastAPI

from backend.app.services.ticket.router import ticket_router
from backend.app.services.user.router import user_router
from backend.app.core import handlers

app = FastAPI()

### Routes
app.include_router(ticket_router)
app.include_router(user_router)

### Exception handlers:
app.add_exception_handler(handlers.TicketNotFound, handlers.ticket_not_found_handler)
app.add_exception_handler(handlers.UnauthorizedTicketAccess, handlers.unauthorized_ticket_handler)

app.add_exception_handler(handlers.UserNotFound, handlers.user_not_found_handler)
app.add_exception_handler(handlers.WrongCredentials, handlers.wrong_credentials_handler)
app.add_exception_handler(handlers.UnauthorizedUserAccess, handlers.unauth_user_acess)

### Health check
@app.get('/')
def health_check():
    return {
        'project': "SupportMind AI",
        'status': "ok"
    }