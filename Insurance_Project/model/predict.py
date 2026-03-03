import joblib
import pandas as pd

# Load the pre-trained model
model = joblib.load('model/model.pkl')

MODEL__VERSION = "1.0.0"

class_labels = model.classes_.tolist()

def predict_output(user_input: dict):
    input_df = pd.DataFrame([user_input])
    predict_class = model.predict(input_df)[0]

    proabilities = model.predict_proba(input_df)[0]
    confidence = max(proabilities)

    class_prob = dict(zip(class_labels, map(lambda p : round(p,4),proabilities)))

    return {
        "predicted_category": predict_class,
        "confidence": round(confidence,4),
        "class_probabilities": class_prob
    }