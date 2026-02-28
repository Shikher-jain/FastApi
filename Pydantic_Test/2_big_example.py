from pydantic import BaseModel, Field, EmailStr, AnyUrl
from typing import Optional, List, Dict, Annotated


class Patient(BaseModel):

    name: Annotated[
        str,
        Field(
            ...,
            description="The name of the patient",
            max_length=50,
            json_schema_extra={"example": "John Doe"},
        ),
    ]

    age: Annotated[
        int,
        Field(
            ...,
            ge=0,
            description="The age of the patient",
            json_schema_extra={"example": 30},
        ),
    ]

    email: Annotated[
        EmailStr,
        Field(
            ...,
            description="The email address of the patient",
            json_schema_extra={"example": "example1@gmail.com"},
        ),
    ]

    website: Annotated[
        Optional[AnyUrl],
        Field(
            default=None,
            description="The website of the patient",
            json_schema_extra={"example": "https://www.example.com"},
        ),
    ]

    weight: Annotated[
        float,
        Field(
            ...,
            gt=0,
            description="The weight of the patient in kg",
            json_schema_extra={"example": 70.5},
        ),
    ]

    height: Annotated[
        float,
        Field(
            ...,
            gt=0,
            description="The height of the patient in cm",
            json_schema_extra={"example": 175.0},
        ),
    ]

    married: Annotated[
        bool,
        Field(
            ...,
            description="Whether the patient is married",
            json_schema_extra={"example": False},
        ),
    ]

    allergies: Annotated[
        Optional[List[str]],
        Field(
            default=None,
            description="List of allergies",
            json_schema_extra={"example": ["peanuts", "dust"]},
        ),
    ]

    contact_details: Annotated[
        Dict[str, str],
        Field(
            ...,
            description="Contact details of the patient",
            json_schema_extra={
                "example": {
                    "email": "john.doe@example.com",
                    "phone": "1234567890"
                }
            },
        ),
    ]
        
# class Patient(BaseModel):
#     name: str = Field(..., description="The name of the patient", example="John Doe",max_length=50)
#     age: int = Field(..., description="The age of the patient", example=30, ge=0)
#     email: EmailStr = Field(..., description="The email address of the patient", example="example1@gmail.com")
#     website: Optional[AnyUrl] = Field(default=None, description="The website of the patient", example="https://www.example.com")
#     weight: float = Field(..., description="The weight of the patient in kg", example=70.5, gt=0)
#     height: float = Field(..., description="The height of the patient in cm", example=175.0, gt=0)
#     married: bool = Field(..., description="Whether the patient is married", example=False)
#     allergies: Optional[List[str]] = Field(default=None, description="List of allergies")
#     contact_details: Dict[str, str] = Field(..., description="Contact details of the patient")

def insert_data(patient: Patient):
        print(f"Inserting data for {patient.name} with age {patient.age}, weight {patient.weight}, height {patient.height}, married {patient.married}, allergies {patient.allergies}, contact details {patient.contact_details}")
def update_data(patient: Patient):
        print(f"Inserting data for {patient.name} with age {patient.age}, weight {patient.weight}, height {patient.height}, married {patient.married}, allergies {patient.allergies}, contact details {patient.contact_details}")

patient_info1 = {"name": "John Doe", "age": 30,"email": "john.doe@example.com", "website": "https://www.johndoe.com", "weight": 70.5, "height": 175.0, "married": False, "allergies": ["peanuts",'dust','pollen'], "contact_details": {"email": "john.doe@example.com", "phone": "123-456-7890"}}
patient1 = Patient(**patient_info1)
update_data(patient1)

patient_info2 = {"name": "John Doe", "age": 30,"email": "john.doe@example.com",  "weight": 70.5, "height": 175.0, "married": False, "allergies": ["peanuts",'dust','pollen'], "contact_details": {"email": "john.doe@example.com", "phone": "123-456-7890"}}
patient2 = Patient(**patient_info2)
update_data(patient2)
