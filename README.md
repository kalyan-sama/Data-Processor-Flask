# Simplified Data Retrieval and Processing System

This Flask application simulates a simplified version of a data retrieval and processing system.

## Features

1. API endpoint for data retrieval (`/fetch-data`)
2. Data processing (converting text to uppercase)
3. In-memory data storage
4. API endpoint for retrieving processed data (`/get-processed-data`)

## Setup and Installation

1. **Clone the repository:** 
```git clone https://github.com/kalyan-sama/Data-Processor-Flask.git```

2. **Create a virtual environment:**
```python -m venv venv```

3. **Activate the virtual environment:**
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

4. **Install the required dependencies:**
```pip install -r requirements.txt```

## Running the Application

1. Ensure you're in the project directory and your virtual environment is activated.

2. Run the Flask application:
```python app.py```

3. The application will start running on `http://127.0.0.1:5000/`.

## Using the API

1. To fetch and process data:
Send a GET request to `http://127.0.0.1:5000/fetch-data`
example: `curl http://127.0.0.1:5000/fetch-data`

2. To retrieve the processed data:
Send a GET request to `http://127.0.0.1:5000/get-processed-data`
Example: `curl http://127.0.0.1:5000/get-processsed-data`
