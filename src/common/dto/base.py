from pydantic import BaseModel, ConfigDict


class BasePydanticModel(BaseModel):
    """Base class for pydantic validation, model e.t.c"""
    model_config = ConfigDict(extra="forbid", from_attributes=True)

