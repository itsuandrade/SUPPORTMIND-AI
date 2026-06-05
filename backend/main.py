from fastapi import FastAPI

from backend.app.core.database import engine, Base

from backend.app.services.ticket.router import ticket_router

app = FastAPI()
Base.metadata.create_all(bind=engine) 

### Routes
app.include_router(ticket_router)

### Health check
@app.get('/health')
def health_check():
    return {
        'project': "SupportMind AI",
        'status': "ok"
    }