from pydantic import BaseModel

class Address(BaseModel):    
    street: str
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    name: str
    age: int 
    address:Address

address_dict1 = {"street": "123 Main St", "city": "Anytown", "state": "CA", "zip_code": "12345"}
address1 = Address(**address_dict1)

# patient_info1 = {"name": "John Doe", "age": 30, "address": address_dict1}
patient_info1 = {"name": "John Doe", "age": 30, "address": address1}
patient1 = Patient(**patient_info1)

print(patient1)
print(patient1.address)
print(patient1.address.street)

temp = patient1.model_dump()
print(temp)
print(type(temp))

temp = patient1.model_dump(include={'name', 'age'})
print(temp)
print(type(temp))

temp = patient1.model_dump(exclude={'address':{'street'}})
print(temp)
print(type(temp))

temp = patient1.model_dump_json()
print(temp)
print(type(temp))
