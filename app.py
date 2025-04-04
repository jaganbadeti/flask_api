from flask import Flask, jsonify, send_file
import mysql.connector
import pandas as pd

app = Flask(__name__)

# Connect to MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",     # Change if needed
        user="root",     # Replace with your MySQL username
        password="Chagallu@534342",  # Replace with your MySQL password
        database="landing"
    )

@app.route('/employees', methods=['GET'])
def get_employees():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Employee")
    employees = cursor.fetchall()
    conn.close()
    return jsonify(employees)

@app.route('/download', methods=['GET'])
def download_employees():
    conn = get_db_connection()
    query = "SELECT * FROM Employee"
    df = pd.read_sql(query, conn)
    conn.close()
    csv_path = 'employees.csv'
    df.to_csv(csv_path, index=False)
    return send_file(csv_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
