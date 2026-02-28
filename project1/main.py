from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field,computed_field
from typing import Annotated,Literal,Optional
import json

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description="The unique identifier for the patient", example="P001")]
    name: Annotated[str, Field(..., description="The name of the patient", example="John Doe")]
    city: Annotated[str, Field(..., description="The city of the patient", example="New York")]
    age: Annotated[int, Field(..., ge=0,lt=100, description="The age of the patient", example=30)]
    gender: Annotated[Literal['male','female','other'], Field(..., description="The gender of the patient", example="male")]
    height: Annotated[float, Field(..., ge=0, description="The height of the patient in meters", example=1.75)]
    weight: Annotated[float, Field(..., ge=0, description="The weight of the patient in kilograms", example=70.0)]

class PatientUpdate(BaseModel):
    # id:     Annotated[Optional[str], Field(..., description="The unique identifier for the patient", example="P001")]
    name:   Annotated[Optional[str], Field(default = None, description="The name of the patient", example="John Doe")]
    city:   Annotated[Optional[str], Field(default = None, description="The city of the patient", example="New York")]
    age:    Annotated[Optional[int], Field(default = None, ge=0,lt=100, description="The age of the patient", example=30)]
    gender: Annotated[Optional[Literal['male','female','other']], Field(default = None, description="The gender of the patient", example="male")]
    height: Annotated[Optional[float], Field(default = None, ge=0, description="The height of the patient in meters", example=1.75)]
    weight: Annotated[Optional[float], Field(default = None, ge=0, description="The weight of the patient in kilograms", example=70.0)]

def load_data():
    try:
        with open("patient_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):     
    with open("patient_data.json", "w") as file:
        json.dump(data, file, indent=4)
    return {"message": "Patient added successfully"}

@app.get("/")
def root():
    return {"message": "Patient Management System"}

@app.get("/about")
def about():
    return {"message": "This is the about page"}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
# def view_patient(patient_id: str):
def view_patient(patient_id: str=Path(..., description="The ID of the patient to view", examples="P001")):
    data = load_data() 
    if patient_id not in data:
        # return {"error": "Patient not found"}
        raise HTTPException(status_code=404, detail="patient not found ")
    return {"patient_id": patient_id, "data": data[patient_id]}  

@app.get("/sort")
# def sort_patients(sort_by: str order):
def sort_patients(sort_by: str = Query(..., description="The field to sort by", examples="height"),order:str=Query("asc", description="The sort order (asc or desc)", examples="asc")):
 
    valid_fields = ["height", "weight","age"]
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field. Must be one of {valid_fields}")
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid sort order. Must be 'asc' or 'desc'")
    

    data = load_data()

    # sorted_data = dict(sorted(data.items(), key=lambda item: item[1][sort_by], reverse=(True if order == "desc" else False ))) 
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse = (order == "desc"))
    return sorted_data

@app.post("/add")
def add_patient(patient: Patient)  :
    data = load_data()
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient with this ID already exists")
    data[patient.id] = patient.model_dump(exclude=["id"])
    save_data(data)
    return JSONResponse(content={"message": "Patient added successfully"}, status_code=201)


@app.put("/edit/{patient_id}")
def edit_patient(patient_id: str, patient_update: PatientUpdate)  :
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient with this ID does not exist")
    
    # existing_patient_info = data[patient_id] 
    # updated_patient_info = patient_update.model_dump(exclude_unset=True)
    # for key, value in updated_patient_info.items():
    #     existing_patient_info[key] = value

    # data[patient_id] = existing_patient_info
    # existing_patient_info['id'] = patient_id
    # patient_pydantic_obj=Patient(**existing_patient_info)
    # existing_patient_info = patient_pydantic_obj.model_dump(exclude ='id')
    # save_data(data)
    # return JSONResponse(content={"message": "Patient updated successfully"}, status_code=201)

    data[patient_id] = {**data[patient_id], **patient_update.model_dump(exclude_unset=True)}
    '''
        is equivalent to:
           Get existing patient data.
           Get only the fields the user wants to update.
           Merge them (new fields overwrite old ones).
           Save the merged result back.
    '''
    save_data(data)
    return JSONResponse(content={"message": "Patient updated successfully"}, status_code=201)

# @app.patch("/edit/{patient_id}", status_code=200)
# def edit_patient(patient_id: str, patient_update: PatientUpdate):

#     data = load_data()

#     if patient_id not in data:
#         raise HTTPException(status_code=404,detail="Patient with this ID does not exist")

#     # Get existing patient data
#     existing_patient = data[patient_id]

#     # Only update provided fields
#     update_data = patient_update.model_dump(exclude_unset=True)

#     # Merge old + new data
#     updated_data = {**existing_patient, **update_data, "id": patient_id}

#     # Revalidate with full Patient model
#     validated_patient = Patient(**updated_data)

#     # Save without ID in JSON (since ID is key)
#     data[patient_id] = validated_patient.model_dump(exclude=["id"])

#     save_data(data)

#     return {
#         "message": "Patient updated successfully",
#         "updated_patient": validated_patient
#     }

@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient with this ID does not exist")
    del data[patient_id]
    save_data(data)
    return JSONResponse(content={"message": "Patient deleted successfully"}, status_code=200)