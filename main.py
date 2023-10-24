import uvicorn
from fastapi import FastAPI

from app import routers


def init_app() -> FastAPI:
    app = FastAPI(debug=True)
    app.include_router(routers.router)
    return app


if __name__ == "__main__":
    uvicorn.run(init_app, port=8000)
