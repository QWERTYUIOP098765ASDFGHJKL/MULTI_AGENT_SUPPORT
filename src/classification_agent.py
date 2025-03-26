from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple classification logic
def classify_query(query):
    if "bill" in query.lower():
        return "Billing", "Log in to your account and navigate to the Billing section."
    elif "appointment" in query.lower():
        return "Appointments", "You can schedule an appointment in the Appointments tab."
    else:
        return "General", "Please contact support for further assistance."

@app.route('/classify', methods=['POST'])
def classify():
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({"error": "Invalid input"}), 400

    category, solution = classify_query(data['query'])
    return jsonify({"category": category, "solution": solution})

if __name__ == '__main__':
    print("Classification Agent running on http://localhost:5001")
    app.run(port=5001)
