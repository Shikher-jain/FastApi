from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    AnyUrl,
    field_validator,
    model_validator,
    computed_field
)
from typing import Optional, List, Dict


# -------------------------
# Nested Model
# -------------------------
class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str


# -------------------------
# Main Model
# -------------------------
class Patient(BaseModel):
    # Fields with validation rules
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., ge=0)
    email: EmailStr
    website: Optional[AnyUrl] = None
    weight: float = Field(..., gt=0)
    height: float = Field(..., gt=0)
    married: bool
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]
    address: Address   # Nested model


    # -------------------------
    # Field Validator
    # -------------------------
    @field_validator("name")
    @classmethod
    def name_must_be_upper(cls, value):
        return value.upper()


    # -------------------------
    # Model Validator
    # -------------------------
    @model_validator(mode="after")
    def check_emergency_contact(self):
        if self.age > 60 and "emergency_contact" not in self.contact_details:
            raise ValueError(
                "Patients above 60 must include an emergency contact"
            )
        return self


    # -------------------------
    # Computed Field
    # -------------------------
    @computed_field
    @property
    def bmi(self) -> float:
        height_in_meters = self.height / 100
        return round(self.weight / (height_in_meters ** 2), 2)


# -------------------------
# Raw Data (Input Data)
# -------------------------
patient_data = {
    "name": "John Doe",
    "age": "65",   # string → automatically converted to int
    "email": "john.doe@example.com",
    "website": "https://www.johndoe.com",
    "weight": 80,
    "height": 175,
    "married": True,
    "allergies": ["dust", "pollen"],
    "contact_details": {
        "email": "john.doe@example.com",
        "phone": "1234567890",
        "emergency_contact": "Jane Doe"
    },
    "address": {
        "street": "123 Main St",
        "city": "Los Angeles",
        "state": "CA",
        "zip_code": "90001"
    }
}


# -------------------------
# Create Model Instance
# -------------------------
patient = Patient(**patient_data)


# -------------------------
# Access Data
# -------------------------
print("Name:", patient.name)
print("City:", patient.address.city)
print("BMI:", patient.bmi)


# -------------------------
# Serialization
# -------------------------

# Full dump
print("\nFull model_dump():")
print(patient.model_dump())

# Include specific fields
print("\nInclude only name and age:")
print(patient.model_dump(include={"name", "age"}))

# Exclude nested field
print("\nExclude address.street:")
print(patient.model_dump(exclude={"address": {"street"}}))

# JSON output
print("\nJSON Output:")
print(patient.model_dump_json())