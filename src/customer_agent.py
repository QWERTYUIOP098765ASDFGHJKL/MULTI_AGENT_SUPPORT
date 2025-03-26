from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/submit_query', methods=['POST'])
def submit_query():
    data = request.get_json()
    query_text = data.get('query')

    # Send query to classification agent
    response = requests.post('http://localhost:5001/classify', json={'query': query_text})
    return response.json()

if __name__ == '__main__':
    app.run(port=5000)
