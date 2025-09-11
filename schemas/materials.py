from pydantic import BaseModel, Field
from typing import Optional, List
import uuid

from base_schemas import FloatUnitRangeValue, StrUnitValue
from enums import HStatementEnum, EUHStatementEnum, StateOfMatterEnum

class UseCase(BaseModel):
    description: str

class MaterialBase(BaseModel):
    # basic info
    name: str
    short_description: str
    other_names: Optional[List[str]] = Field([])

    cas: Optional[str] = Field(None, description="CAS number")
    
    # safety
    h_statements: Optional[List[HStatementEnum]] = Field([])
    euh_statements: Optional[List[EUHStatementEnum]] = Field([])

    # economic
    use_cases: Optional[List[UseCase]] = Field([])
    price_per_kg: Optional[float] = Field(None, description="Estimated price per kilogram")

    # storing / processing
    storage: Optional[str] = Field(None)

    # chemical / physical properties
    state_of_matter: Optional[StateOfMatterEnum] = Field(None)
    viscosity: Optional[FloatUnitRangeValue] = Field(None)
    density: Optional[FloatUnitRangeValue] = Field(None)
    non_solid_content: Optional[FloatUnitRangeValue] = Field(None)
    nco_content: Optional[FloatUnitRangeValue] = Field(None)
    amine_content: Optional[FloatUnitRangeValue] = Field(None)
    ph_value: Optional[FloatUnitRangeValue] = Field(None)
    mean_particle_size: Optional[FloatUnitRangeValue] = Field(None)
    particle_size_distribution: Optional[List[FloatUnitRangeValue]] = Field([]) # here we use the "extra" field to define the sieve size
    solubility: Optional[List[str]] = Field([]) # here we use the cas or id fields of substances

class Substance(MaterialBase):
    pass
    
class Component(BaseModel):
    substance: Substance
    share_percent: Optional[float] = Field(None)

class Product(MaterialBase):
    components: Optional[List[Component]] = Field([])

ethanol = Substance(
    name="Ethanol",
    short_description="Primary alcohol; 2 Carbon atoms; used in alcoholic beverages",
    other_names=["Ethyl alcohol", "EtOH"],
    cas="64-17-5",
    h_statements=["H225", "H319"],
    density=FloatUnitRangeValue(unit="GRAMM_PER_MILLILITRE", value=0.78)
)

print(ethanol.name)
print(ethanol.short_description)
print(f"{ethanol.density.value} {ethanol.density.unit.display}")

for i in ethanol.h_statements:
    print(i.display)