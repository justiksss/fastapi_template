import uvicorn

from logger_config import configure_logger
from src.app import create_app

app = create_app()

configure_logger(log_level="DEBUG")

if __name__ == '__main__':
    uvicorn.run(
        app="entrypoints.asgi:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
