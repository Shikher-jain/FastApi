from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator
from typing import Optional, List, Dict, Annotated


        
class Patient(BaseModel):
    name: str
    age: int 
    email: EmailStr
    website: Optional[AnyUrl] = None
    weight: float
    height: float
    married: bool
    allergies: Optional[List[str]]  = None
    contact_details: Dict[str, str]


    # @field_validator("age",mode="before")
    @field_validator("age",mode="after") # BY default, the validation is done in "after" mode, which means that the validation function will be called after the field value has been parsed and validated by Pydantic. If you want to perform validation before parsing and validation, you can use "before" mode.
    @classmethod
    def age_validor(cls, value):   #cls: class itself, value: the value of the field being validated
        if value < 0:
            raise ValueError("Age must be a positive number")
        return value
    
    @field_validator("name")
    @classmethod
    def name_validor(cls, value):   #cls: class itself, value: the value of the field being validated
        return value.upper()
    
    @field_validator("email")
    @classmethod
    def email_validor(cls, value):   #cls: class itself, value: the value of the field being validated
        valid_domains = ["@example.com", "@company.com"]
    
        if not any(value.endswith(domain) for domain in valid_domains):
            raise ValueError("Email must end with @example.com or @company.com")
        return value


def insert_data(patient: Patient):
        print(f"Inserting data for {patient.name} with age {patient.age}, weight {patient.weight}, height {patient.height}, married {patient.married}, allergies {patient.allergies}, contact details {patient.contact_details}")
def update_data(patient: Patient):
        print(f"Inserting data for {patient.name} with age {patient.age}, weight {patient.weight}, height {patient.height}, married {patient.married}, allergies {patient.allergies}, contact details {patient.contact_details}")

patient_info1 = {"name": "John Doe", "age": '30',"email": "john.doe@example.com", "website": "https://www.johndoe.com", "weight": 70.5, "height": 175.0, "married": False, "allergies": ["peanuts",'dust','pollen'], "contact_details": {"email": "john.doe@example.com", "phone": "123-456-7890"}}
patient1 = Patient(**patient_info1)
update_data(patient1)

patient_info2 = {"name": "John Doe", "age": 30,"email": "john.doe@example.com",  "weight": 70.5, "height": 175.0, "married": False, "allergies": ["peanuts",'dust','pollen'], "contact_details": {"email": "john.doe@example.com", "phone": "123-456-7890"}}
patient2 = Patient(**patient_info2)
update_data(patient2)
