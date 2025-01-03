# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application files
COPY . .

# Expose ports
EXPOSE 8000
EXPOSE 8501

# Run API and Streamlit App
CMD ["sh", "-c", "uvicorn scripts.race_api:app --host 0.0.0.0 --port 8000 & streamlit run frontend/dashboard.py --server.port 8501"]
