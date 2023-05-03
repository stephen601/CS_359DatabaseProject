from flask import Flask, make_response, jsonify, request, render_template, redirect, url_for
import json
import sqlite3
import os

app = Flask(__name__)

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
    database = request.form['database']
    conn = db_connection(database)
    try:
        # Perform any necessary operations on the database
        # ...
        conn.close()
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
            return redirect(url_for('query', new_database=new_database))
        else:
            return jsonify({"status": "error"})
    else:
        return jsonify({"status": "error", "message": "Database file not found."})

@app.route("/query")
def query():
    new_database = request.args.get('new_database')
    return render_template("query.html", new_database=new_database)

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
