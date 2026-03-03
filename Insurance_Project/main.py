from fastapi import FastAPI
from fastapi.responses import JSONResponse

from schema.user_input import InsuranceData
from model.predict import predict_output, model, MODEL__VERSION
from schema.prediction_response import PredictionResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Insurance Premium Prediction API!"}


@app.get("/health")
def health_check():
    return {"status": "ok", "version": MODEL__VERSION, "model_info" : model is not None} 

@app.post("/predict", response_model=PredictionResponse)
def predict_insurance_premium(data: InsuranceData):
    try:
        input_data = {
            'bmi': data.bmi,
            'age_group': data.age_group,
            'lifestyle_risk': data.lifestyle_risk,
            'city_tier': data.city_tier,
            'income_lpa': data.income_lpa,
            'occupation': data.occupation
        }

        prediction = predict_output(input_data)
        return JSONResponse(status_code=200, content={'response':prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)}) 