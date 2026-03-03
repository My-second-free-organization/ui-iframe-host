from fastapi import FastAPI
from .routes import router

app = FastAPI(title="FlowForge Email Connector", version="2.4.0")
app.include_router(router, prefix="/api/v1/email")

@app.get("/health")
def health(): return {"status": "healthy"}
