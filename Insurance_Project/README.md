
# Insurance Prediction Project

This project is a FastAPI and Streamlit-based web application for predicting insurance charges based on user input. It uses a machine learning model trained on historical insurance data.

## Features
- Predict insurance charges using ML model
- User-friendly web interface (Streamlit)
- REST API endpoints (FastAPI)
- Docker support for easy deployment

## Project Structure
- `main.py`: FastAPI backend
- `frontend.py`: Streamlit frontend
- `model/predict.py`: ML model logic
- `data/insurance.csv`: Dataset
- `schema/`: Pydantic models for request/response
- `config/`: Configuration files
- `notebooks/`: Jupyter notebooks for model development
- `requirements.txt`: Python dependencies

## Getting Started
### 1. Clone the repository
```bash
git clone https://github.com/Shikher-jain/FastApi.git
cd FastApi/Insurance_Project
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run FastAPI backend
```bash
uvicorn main:app --reload
```

### 4. Run Streamlit frontend
```bash
streamlit run frontend.py
```

### 5. Docker (optional)
Build and run the app using Docker:
```bash
docker build -t insurance-prediction .
docker run -p 8000:8000 insurance-prediction
```

## API Endpoints
- `/predict`: Get insurance charge prediction
- `/docs`: Swagger UI for API documentation

## Deployment
You can deploy this app on Streamlit Community Cloud or any cloud platform supporting FastAPI and Streamlit.

## License
MIT
