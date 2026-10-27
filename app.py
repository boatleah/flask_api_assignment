from flask import Flask, request, jsonify

app = Flask(__name__)

# GET endpoint: takes information out of the API.
@app.get("/hello")
def hello():
    name = request.args.get("name")
    if name:
        message = f"Hello, {name}!"
    else:
        message = "Hello, world!"
    return jsonify({"message": message, "status": "success"})

# POST endpoint: puts data into the API.
@app.post("/sum")
def sum_numbers():
    data = request.get_json(silent=True)  # None if body isn't valid JSON

    # Error handling
    if not isinstance(data, dict) or "numbers" not in data:
        return jsonify({"error": "JSON body with 'numbers' list required"}), 400

    numbers = data["numbers"]
  
    if not isinstance(numbers, list) or not all(
        isinstance(n, (int, float)) and not isinstance(n, bool) for n in numbers
    ):
        return jsonify({"error": "'numbers' must be a list of numbers"}), 400

    return jsonify({"sum": sum(numbers), "status": "success"})

if __name__ == "__main__":
    # Runs locally on port 5000
    app.run(debug=True, port=5000)