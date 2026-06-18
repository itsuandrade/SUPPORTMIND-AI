from fastapi import Request
from fastapi.responses import JSONResponse

## TICKETS:

from backend.app.services.ticket.exceptions import TicketNotFound, UnauthorizedTicketAccess

async def ticket_not_found_handler(request: Request, exc: TicketNotFound):
    return JSONResponse(
        status_code=404,
        content={"detail": "Ticket not found."}
    )

async def unauthorized_ticket_handler(request: Request, exc: UnauthorizedTicketAccess):
    return JSONResponse(
        status_code=403,
        content={"detail": "Forbidden."}
    )

## USERS: