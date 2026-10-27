## Setup
```
mkdir flask_api_assignment
cd flask_api_assignment
python -m venv venv
venv\Scripts\activate
pip install --upgrade pip
pip install Flask pytest
```

## Run tests
**Run:**
```
pytest test_app.py
```
**Outcome:**
```
6 passed in 0.57s
```

## Run server
**Run:**
```
python app.py
```
**Outcome:**
```
Running on http://127.0.0.1:5000
```

## Tested endpoints

### GET /hello?name=Leah
**Run:**
```
Invoke-RestMethod -Uri "http://127.0.0.1:5000/hello?name=Leah"
```
**Outcome:**
```
message      status
-------      ------
Hello, Leah! success
```
Opening the URL in a browser shows:
```
{
  "message": "Hello, Leah!",
  "status": "success"
}
```

### POST /sum with valid input
**Run:**
```
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:5000/sum -ContentType "application/json" -Body '{"numbers":[1,2,3]}'
```
**Outcome:**
```
status  sum
------  ---
success   6
```

### POST /sum with bad input (returns HTTP 400)
**Run:**
```
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:5000/sum -ContentType "application/json" -Body '{"nums":[1,2]}'
```
**Outcome:**
```
{"error": "JSON body with 'numbers' list required"}
```
