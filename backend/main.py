from fastapi import FastAPI
from backend.app.services.ticket.router import ticket_router

app = FastAPI()

### Routes
app.include_router(ticket_router)

### Health check
@app.get('/health')
def health_check():
    return {
        'project': "SupportMind AI",
        'status': "ok"
    }