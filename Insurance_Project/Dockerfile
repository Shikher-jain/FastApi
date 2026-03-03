# Use an official Python runtime as a parent image
FROM python:3.11.4-slim

# Set the working directory in the container
WORKDIR /main

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port that the application will run on
EXPOSE 8000

# Define the command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]