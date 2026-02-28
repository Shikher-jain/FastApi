from pydantic import BaseModel


class Patient(BaseModel):
    name: str
    age: int


def insert_data(patient: Patient):
        print(f"Inserting data for {patient.name} with age {patient.age}")
def update_data(patient: Patient):
        print(f"Updating data for {patient.name} with age {patient.age}")

patient_info1 = {"name": "John Doe", "age": 30}
patient_info2 = {"name": "John Smith", "age": '35'}
patient_info3 = {"name": "John Smith", "age": 'ten'}

patient1 = Patient(**patient_info1)
insert_data(patient1)

patient2 = Patient(**patient_info2)
update_data(patient2)

# patient3 = Patient(**patient_info3)
# update_data(patient3)