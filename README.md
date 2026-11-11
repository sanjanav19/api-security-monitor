# API Security Monitor

An API security monitoring project built using Python and FastAPI.

## Current Features

- FastAPI backend
- API health-check endpoint
- Products endpoint
- Login placeholder endpoint
- HTTP middleware for request monitoring
- Request logging: method, path, IP, status code and response time
- Endpoint to retrieve request logs

## Technology Stack

- Python 3.13
- FastAPI
- Uvicorn

## Run Locally

1. Clone this repository.
2. Navigate to the backend folder.
3. Create and activate a virtual environment.
4. Install dependencies:

   python -m pip install -r requirements.txt

5. Start the server:

   uvicorn main:app --reload

6. Open http://127.0.0.1:8000/docs

## Current Limitations

- Request logs are stored in memory.
- Login is currently a placeholder.
- Automated threat detection and database integration are planned future features.
