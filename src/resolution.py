from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

def get_solution_from_db(category):
    try:
        connection = psycopg2.connect(
            dbname="customer_support",
            user="postgres",
            password="your_password",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()

        cursor.execute("SELECT solution FROM knowledge_base WHERE category=%s", (category,))
        result = cursor.fetchone()
        return result[0] if result else "Solution not found"
    except Exception as e:
        return str(e)
    finally:
        cursor.close()
        connection.close()

@app.route('/resolve', methods=['POST'])
def resolve():
    data = request.get_json()
    category = data.get('category')
    solution = get_solution_from_db(category)
    return jsonify({'category': category, 'solution': solution})

if __name__ == '__main__':
    app.run(port=5432)
