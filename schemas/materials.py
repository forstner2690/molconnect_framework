from pydantic import BaseModel, Field
from typing import Optional, List

from .base_schemas import FloatUnitValue, StrUnitValue

class UseCase(BaseModel):
    description: str

class MaterialBase(BaseModel):
    # basic info
    name: str
    short_description: str
    cas: Optional[str] = Field(None, description="CAS number")
    
    # safety
    h_statements = Optional[List[HStatementEnum]] = Field([])
    euh_statements = Optional[List[EUHStatementEnum]] = Field([])

    # economic
    use_cases: Optional[List[UseCase]] = Field([])
    price_per_kg: Optional[float] = Field(None, description="Estimated price per kilogram")

    # chemical / physical properties
    state_of_matter: Optional[StateOfMatterEnum] = Field(None)
    viscosity: Optional[FloatUnitValue] = Field(None)
    density: Optional[FloatUnitValue] = Field(None)
    non_solid_content: Optional[FloatUnitValue] = Field(None)
    nco_content: Optional[FloatUnitValue] = Field(None)
    amine_content: Optional[FloatUnitValue] = Field(None)

class Substance(MaterialBase):
    pass
    
class Component(BaseModel):
    substance: Substance
    share_percent: Optional[float] = Field(None)

class Composition(MaterialBase):
    components: Optional[List[Component]] = Field([])
