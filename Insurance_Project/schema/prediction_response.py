from pydantic import BaseModel, Field
from typing import Dict 

class PredictionResponse(BaseModel):    
    predicted_category: str = Field(..., description="Predicted insurance premium category", example="medium")
    confidence: float = Field(..., description="Confidence score of the prediction", example=0.85)
    class_probabilities: Dict[str, float] = Field(..., description="Probabilities for each insurance premium category", example={"low": 0.1, "medium": 0.85, "high": 0.05})
