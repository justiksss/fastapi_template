from src.common.exceptions.base import BaseExceptionModel


class BaseAuthException(BaseExceptionModel):
    """Base exception for authentication/authorization which describes required for handling fields."""


class NotValidToken(BaseAuthException):
    """JWT Token is not valid during or after decoding"""
    pass


class AccessTokenExpired(BaseAuthException):
    """JWT Token expired"""
    pass

