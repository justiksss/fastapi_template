from src.common.exceptions.base import BaseExceptionModel


class BaseDatabaseException(BaseExceptionModel):
    """Base exception for handler during database commands/queries"""


class IntegrityError(BaseDatabaseException):
    """Duplicate unique constraint, not foreign key e.t.c"""


class NotFound(BaseDatabaseException):
    """Not found row/rows in database table"""


