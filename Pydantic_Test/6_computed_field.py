from pydantic import BaseModel, Field, EmailStr, AnyUrl, computed_field
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

    @computed_field
    @property
    def bmi(self) -> float:
        height_in_meters = self.height / 100
        return round(self.weight / (height_in_meters ** 2),2)



def insert_data(patient: Patient):
        
        print(f"Inserting data for {patient.name} with age {patient.age}, weight {patient.weight}, height {patient.height}, married {patient.married}, allergies {patient.allergies}, contact details {patient.contact_details}, BMI {patient.bmi}")
def update_data(patient: Patient):
        print(f"Updating data for {patient.name} with age {patient.age}, weight {patient.weight}, height {patient.height}, married {patient.married}, allergies {patient.allergies}, contact details {patient.contact_details}, BMI {patient.bmi}")

patient_info1 = {"name": "John Doe", "age": '90',"email": "john.doe@example.com", "website": "https://www.johndoe.com", "weight": 70.5, "height": 175.0, "married": False, "allergies": ["peanuts",'dust','pollen'], "contact_details": {"email": "john.doe@example.com", "phone": "123-456-7890", "emergency_contact": "Jane Doe"}}
patient1 = Patient(**patient_info1)
insert_data(patient1)

patient_info2 = {"name": "John Doe", "age": 30,"email": "john.doe@example.com",  "weight": 70.5, "height": 175.0, "married": False, "allergies": ["peanuts",'dust','pollen'], "contact_details": {"email": "john.doe@example.com", "phone": "123-456-7890"}}
patient2 = Patient(**patient_info2)
update_data(patient2)
