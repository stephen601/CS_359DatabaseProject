from flask import Flask, make_response, jsonify, request, render_template, redirect, url_for, session
import json
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "secret_key"

def db_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
    except sqlite3.error as e:
        print(e)
    return conn

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/logout', methods=['POST'])
def logout():
    database = session.get('database')
    conn = db_connection(database)
    try:
        # Perform any necessary operations on the database
        # ...
        conn.close()
        session.pop('database', None)
        message = "Database connection closed successfully."
        return render_template("index.html", message=message)
    except:
        # Handle any errors that may occur
        # ...
        return render_template("error.html")

@app.route('/api/database', methods=["POST"])
def get_database():
    new_database = request.form["database"]
    if os.path.isfile(new_database):
        conn = db_connection(new_database)
        if conn:
            session['database'] = new_database
            return redirect(url_for('query'))
        else:
            return jsonify({"status": "error"})
    else:
        return jsonify({"status": "error", "message": "Database file not found."})

@app.route("/query")
def query():
    database = session.get('database')
    return render_template("query.html", database=database)

@app.route('/api/display', methods=["GET"])
def get_table_data():
    database = session.get('database')
    conn = db_connection(database)
    cursor = conn.cursor()

    # query database schema to get column names for selected table
    cursor.execute(f"PRAGMA table_info(DigitalDisplay)")
    columns = [row[1] for row in cursor.fetchall()]

    # dynamically construct SQL statement with 
    sql = f"SELECT * FROM DigitalDisplay"
    cursor.execute(sql)

    # process cursor data into custom objects or dictionaries
    data = []
    for row in cursor.fetchall():
        data.append(dict(zip(columns, row)))

    return jsonify(data)

@app.route('/display_all')
def display_all():
    # Display all the digital displays
    return render_template("display_all.html")

@app.route('/search')
def search():
    # Search digital displays given a scheduler system
    return render_template("search.html")

@app.route('/insert')
def insert():
    # Insert a new digital display
    return render_template("insert.html")

@app.route('/delete')
def delete():
    # Delete a digital display
    return render_template("delete.html")

@app.route('/update')
def update():
    # Update a digital display
    return render_template("update.html")

@app.route('/process_option', methods=['POST'])
def process_option():
    option = request.form['option']
    if option == 'display_all':
        return redirect(url_for('display_all'))
    elif option == 'search':
        return redirect(url_for('search'))
    elif option == 'insert':
        return redirect(url_for('insert'))
    elif option == 'delete':
        return redirect(url_for('delete'))
    elif option == 'update':
        return redirect(url_for('update'))

if __name__ == '__main__':
    app.run(debug=True)
