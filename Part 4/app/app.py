from flask import Flask, make_response, jsonify, request, render_template, redirect, url_for, session
import json
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "secret_key"
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def db_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
    except sqlite3.error as e:
        print(e)
    return conn


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['database'] = request.form['database']
        conn = db_connection(session['database'])
        try:
            # Perform any necessary operations on the database
            # ...
            conn.close()
            session['message'] = "Database connection established successfully."
            return redirect(url_for('index',os=os))
        except:
            # Handle any errors that may occur
            # ...
            return render_template("error.html")
    else:
        message = session.pop('message', None)
        return render_template("index.html", message=message, os=os)


@app.route('/logout', methods=['POST'])
def logout():
    session['database'] = request.form['database']
    conn = db_connection(session['database'])
    try:
        # Perform any necessary operations on the database
        # ...
        conn.close()
        session.pop('database', None)
        session['message'] = "Database connection closed successfully."
        return redirect(url_for('index'))
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

@app.route('/details')
def details():
    model_no = request.args.get('modelNo')
    conn = db_connection(session.get('database'))
    cursor = conn.cursor()

    # Execute the SQL query with the given modelNo value
    cursor.execute("""
        SELECT DigitalDisplay.*, Model.width, Model.height, Model.weight, Model.depth, Model.screenSize
        FROM DigitalDisplay
        JOIN Model ON DigitalDisplay.modelNo = Model.modelNo
        WHERE DigitalDisplay.modelNo = ?
    """, (model_no,))
    data = cursor.fetchone()

    # Close the database connection
    conn.close()

    # Render the detail template with the data
    return render_template('detail.html', data=data)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        scheduler_system = request.form.get('schedulerSystem')
        print(scheduler_system)
        conn = db_connection(session.get('database'))
        cursor = conn.cursor()

        # Execute the SQL query to search for entries with the selected scheduler system
        cursor.execute("""
            SELECT * FROM DigitalDisplay
            WHERE schedulerSystem = ?
        """, (scheduler_system,))
        data = cursor.fetchall()

        # Close the database connection
        conn.close()

        # Render the search results template with the data
        return render_template('search.html', data=data)

    else:
        # Render the search template with the scheduler system dropdown menu
        cursor = db_connection(session.get('database')).cursor()
        cursor.execute("SELECT DISTINCT schedulerSystem FROM DigitalDisplay")
        systems = [row[0] for row in cursor.fetchall()]
        return render_template("search.html", systems=systems)


@app.route('/api/display', methods=['POST'])
def get_display_data():
    scheduler_system = request.form.get('schedulerSystem')
    database = session.get('database')
    conn = db_connection(database)
    cursor = conn.cursor()

    # query database to get data for selected scheduler system
    sql = f"SELECT * FROM DigitalDisplay WHERE schedulerSystem = '{scheduler_system}'"
    cursor.execute(sql)

    # process cursor data into custom objects or dictionaries
    data = []
    for row in cursor.fetchall():
        data.append(dict(zip(['modelNo', 'serialNo', 'schedulerSystem'], row)))

    return jsonify(data)



@app.route('/insert')
def insert():
    # Insert a new digital display
    return render_template("insert.html")

@app.route('/api/insertNewDisplay', methods=['POST'])
def insertNewDisplay():

    model_number = request.form['modelNumber']
    scheduler_system = request.form['schedulerSystem']
    serial_number = request.form['serialNumber']
    
    print(model_number)
    print(serial_number)
    print(scheduler_system)

    database = session.get('database')
    conn = db_connection(database)
    cursor = conn.cursor()

    sql = f"INSERT INTO DigitalDisplay (serialNo, schedulerSystem, modelNo) VALUES ({serial_number}, '{scheduler_system}', {model_number});"
    sql2 = f"INSERT INTO Model (modelNo, width, height, weight, depth, screenSize) VALUES ({model_number}, 10, 8, 20, 2, 12);"
    
    cursor.execute(sql)
    cursor.execute(sql2)
    conn.commit()

    return render_template("display_all.html")

@app.route('/api/digital_delete', methods=['POST'])
def digital_delete():

    model_number = request.form['modelNumber']

    database = session.get('database')
    conn = db_connection(database)
    cursor = conn.cursor()

    sql = f"DELETE FROM DigitalDisplay WHERE modelNo={model_number};"
    
    print(sql)
    cursor.execute(sql)
    conn.commit()

    return render_template("display_all.html")

@app.route('/api/digital_update', methods=['POST'])
def digital_update():

    model_number = request.form['modelNumber']
    width = request.form['width']
    height = request.form['height']
    weight = request.form['weight']
    depth = request.form['depth']
    screenSize = request.form['screenSize']

    database = session.get('database')
    conn = db_connection(database)
    cursor = conn.cursor()

    sql = f"UPDATE Model SET width={width}, height={height}, weight={weight}, depth={depth}, screenSize={screenSize} WHERE modelNo={model_number};"
    
    print(sql)
    cursor.execute(sql)
    conn.commit()

    return render_template("display_all.html")

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