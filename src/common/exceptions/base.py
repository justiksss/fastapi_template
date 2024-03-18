class BaseExceptionModel(Exception):
    """Base exception model for else"""

    def __init__(self, details: list[str], title: str) -> None:
        self.details = details
        self.title = title
