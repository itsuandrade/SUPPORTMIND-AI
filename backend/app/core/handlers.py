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

from backend.app.services.user.exceptions import UserNotFound, UnauthorizedUserAccess, WrongCredentials

async def user_not_found_handler(request: Request, exc: UserNotFound):
    return JSONResponse(
        status_code=404,
        content={"detail": "User not found."}
    )

async def wrong_credentials_handler(request: Request, exc: WrongCredentials):
    return JSONResponse(
        status_code=401,
        content={"detail": "Username or password are wrong. Try loggin in again."}
    )

async def unauth_user_acess(request: Request, exc: UnauthorizedUserAccess):
    return JSONResponse(
        status_code=403,
        content={"detail": "Forbidden."}
    )