from flask import Flask, make_response, jsonify, request, render_template
import json
import sqlite3

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('ABC.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/getTable', methods=["POST"])
def get_table_data():
        conn = db_connection()
        cursor = conn.cursor()

        table_name = request.form["table"]

        # query database schema to get column names for selected table
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [row[1] for row in cursor.fetchall()]

        # dynamically construct SQL statement with selected columns and table name
        column_names = ", ".join(columns)
        sql = f"SELECT {column_names} FROM {table_name}"
        cursor.execute(sql)

        # process cursor data into custom objects or dictionaries
        data = []
        for row in cursor.fetchall():
            data.append(dict(zip(columns, row)))

        return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
