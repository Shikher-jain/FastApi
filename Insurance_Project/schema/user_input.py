from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated

from config.city_tier  import tier_1_cities, tier_2_cities

class InsuranceData(BaseModel):
    age: Annotated[int, Field(..., gt=0,lt=120, description="Age of the insured person")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the insured person in kg")]
    height: Annotated[float, Field(..., gt=0, lt=2.5, description="Height of the insured person in m")]
    income_lpa: Annotated[float, Field(..., gt=0, description="Income of the insured person in lakhs per annum")]
    smoker: Annotated[bool, Field(..., description="Whether the insured person is a smoker or not")]
    city: Annotated[str, Field(..., description="City of residence of the insured person")]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job','business_owner', 'unemployed', 'private_job'], Field(..., description="Occupation of the insured person")]  

    @field_validator('city')
    def validate_city(cls, value):
        return value.strip().title()

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"

    @computed_field
    @property
    def age_group(self) -> str:
        age = self.age
        if age < 25:
            return "young"
        elif age < 45:
            return "adult"
        elif age < 60:
            return "middle_aged"
        return "senior"

    @computed_field
    @property
    def city_tier(self) -> int:
        city = self.city.strip().lower()
        if city in tier_1_cities:
            return 1
        elif city in tier_2_cities:
            return 2
        else:
            return 3

