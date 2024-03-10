import logging
import logging.config


def configure_logger(log_level: str) -> None:
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "vl": {
                "format": "%(levelname)-8s | %(asctime)s | %(name)s: %(message)s",
            }
        },
        "handlers": {
            "stdout": {
                "class": "logging.StreamHandler",
                "level": log_level,
                "formatter": "vl",
                "stream": "ext://sys.stdout",
            },
            "stderr": {
                "class": "logging.StreamHandler",
                "level": "ERROR",
                "formatter": "vl",
                "stream": "ext://sys.stderr",
            },
        },
        "loggers": {
            "root": {"level": log_level, "handlers": ["stdout"]},
            "uvicorn.error": {
                "level": log_level,
                "handlers": ["stderr"],
                "propagate": True,
            },
        },
    }

    logging.config.dictConfig(config=config)
