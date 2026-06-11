from fastapi import FastAPI
from backend.app.services.ticket.router import ticket_router
from backend.app.services.user.router import user_router

app = FastAPI()

### Routes
app.include_router(ticket_router)
app.include_router(user_router)

### Health check
@app.get('/')
def health_check():
    return {
        'project': "SupportMind AI",
        'status': "ok"
    }