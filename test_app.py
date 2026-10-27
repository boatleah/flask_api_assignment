from app import app

client = app.test_client()

def test_hello_default():
    r = client.get("/hello")
    assert r.status_code == 200
    assert r.get_json()["message"] == "Hello, world!"

def test_hello_with_name():
    r = client.get("/hello?name=Leah")
    assert r.status_code == 200
    assert r.get_json()["message"] == "Hello, Leah!"

def test_sum_valid():
    r = client.post("/sum", json={"numbers": [1, 2, 3]})
    assert r.status_code == 200
    assert r.get_json()["sum"] == 6

def test_sum_missing_field():
    r = client.post("/sum", json={"nums": [1, 2]})
    assert r.status_code == 400

def test_sum_no_json():
    r = client.post("/sum", data="not json")
    assert r.status_code == 400

def test_sum_bad_values():
    r = client.post("/sum", json={"numbers": [1, "a"]})
    assert r.status_code == 400