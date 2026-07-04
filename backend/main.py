from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(
    title="Nexora Electronics AI Customer Support",
    description="Multi-Agent AI Customer Support System",
    version="1.0.0"
)

app.include_router(router)