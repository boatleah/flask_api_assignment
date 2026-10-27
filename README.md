# Flask Api Assignment

## Setup:
mkdir flask_api_assignment </br>
cd flask_api_assignment </br>
python -m venv venv </br>
venv\Scripts\activate </br>
pip install --upgrade pip </br>
pip install Flask pytest

## Run test:
pytest test_app.py
## Outcome:
6 passed in 0.57s

## Run server:
Python app.py

## Outcome:
Running on http://127.0.0.1:5000/hello?name=Leah

## Result when clicked on http://127.0.0.1:5000/hello?name=Leah
{
  "message": "Hello, Leah!",
  "status": "success"
}



