from fastapi import FastAPI

from logger_config import configure_logger

configure_logger(log_level="DEBUG")


def create_app() -> FastAPI:
    """FastAPI factory

    :return
        Return a configured app instance with routers
    """
    app = FastAPI()

    for setting in [init_routers, init_middleware]:
        setting(app=app)

    return app


def init_routers(app: FastAPI) -> None:
    """Include all routers here"""
    pass


def init_middleware(app: FastAPI) -> None:
    """Init middleware here"""
    pass


