from pydantic import BaseModel, Field
from typing import Optional, List

from enums import UnitEnum

# UNITS

class UnitValueBase(BaseModel):
    unit: UnitEnum
    method: Optional[str] = Field(None)
    index: Optional[int] = Field(None) # used for ordering values in a list. 

class FloatUnitRangeValue(UnitValueBase):
    value: float
    lower_limit: Optional[float] = Field(None)
    upper_limit: Optional[float] = Field(None)

class StrUnitValue(UnitValueBase):
    value: str

