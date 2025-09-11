from pydantic import BaseModel, Field
from typing import Optional, List

from .enums import UnitEnum

# UNITS

class UnitValueBase(BaseModel):
    unit: UnitEnum
    method: Optional[str] = Field(None)

class FloatUnitValue(UnitValueBase):
    value: float

class StrUnitValue(UnitValueBase):
    value: str