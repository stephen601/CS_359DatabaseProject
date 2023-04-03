import sqlite3
from sqlite3 import Error
import sys
import numpy as np


def close_connection(conn):
    conn.close()


def create_connection(db_file):
    conn = None
    try:
        conn=sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        print("[INFO] Connection established: " + sqlite3.version)

    except Error as e:
        print(e)

    return conn


def query1(conn):
    try:
        parameter = str(sys.argv[2])

        streetDetected = False

        cur = conn.cursor()
        cur.execute("SELECT * FROM Site")
        rows = cur.fetchall()

        for row in rows:
            row_address = row[2].split()
            thisAddress = row_address[1] + ' ' + row_address[2] + ' ' + row_address[3]

            if parameter == thisAddress:
                print('Site Code:', row[0])
                print('Site Type:', row[1])
                print('Site Address:', row[2])
                print('Site Phone:', row[3])

                streetDetected = True

        if streetDetected is False:
            print("No matching street values found.")

    except IndexError as e:
        print("You need to supply a parameter.")




def query2(conn):
    try:
        parameter = str(sys.argv[2])

        cur = conn.cursor()
        cur2 = conn.cursor()

        cur.execute(f"SELECT * FROM DigitalDisplay WHERE schedulerSystem like '{parameter}'")

        rows = cur.fetchall()

        for row in rows:
            cur2.execute(
                f"SELECT name FROM TechnicalSupport WHERE empId IN(SELECT empId FROM Specializes WHERE modelNo like '{row[2]}')"
            )
            namerow = cur2.fetchall()
            name = namerow[0][0]

            print("Serial Number:", row[0])
            print("Scheduler System:", row[1])
            print("Model Number:", row[2])
            print("Employee name:", name)

    except IndexError as e:
        print("You need to supply a parameter.")




def query3(conn):
    cur = conn.cursor()

    allRows = cur.execute(f"SELECT name FROM Salesman").fetchall()
    allNames = sorted([x[0] for x in allRows])
    uniqueNames = np.unique(allNames)

    for thename in uniqueNames:
        if allNames.count(thename) <= 1:
            print(f"{thename}: {allNames.count(thename)}")
        else:
            relevantRows = cur.execute(f"SELECT * FROM Salesman WHERE name LIKE '{thename}'")
            print(f"{thename}: {allNames.count(thename)} {[i for i in relevantRows]}")


def query4(conn):
    try:
        parameter = str(sys.argv[2])

        cur = conn.cursor()

        allRows = cur.execute(f"SELECT name FROM Client WHERE phone LIKE '{parameter}'").fetchall()

        print(f"Clients with phone number {parameter}: ")
        for row in allRows:
            print(row[0])

    except IndexError as e:
        print("You need to supply a parameter.")
def query5(conn):
     try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT Administrator.empId, Administrator.name, SUM(AdmWorkHours.hours) AS total_working_hours
            FROM Administrator
            JOIN AdmWorkHours ON Administrator.empId = AdmWorkHours.empId
            GROUP BY Administrator.empId
            ORDER BY total_working_hours ASC
            """)
        rows = cursor.fetchall()
        for row in rows:
            print(row[0], row[1], row[2])
     except Error as e:
        print(e)    
def query6(conn):
    try:
        cursor = conn.cursor()
        model_no = sys.argv[2]
        cursor.execute("""
            SELECT TechnicalSupport.name
            FROM TechnicalSupport
            JOIN Specializes ON TechnicalSupport.empId = Specializes.empId
            WHERE Specializes.modelNo = ?
            """, (model_no,))
        rows = cursor.fetchall()
        for row in rows:
            print(row[0])
    except IndexError as e:
       print("You need to supply a parameter.")
def query7(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT Salesman.name, AVG(Purchases.commissionRate) AS avg_commission_rate
            FROM Salesman
            JOIN Purchases ON Salesman.empId = Purchases.empId
            GROUP BY Salesman.empId
            ORDER BY avg_commission_rate DESC
            """)
        rows = cursor.fetchall()
        max_len_name = max(len(row[0]) for row in rows)
        max_len_rate = max(len(str(row[1])) for row in rows)
        print(f"{'Name'.ljust(max_len_name)} {'Average Commission Rate'}")
        print("------------------".ljust(max_len_name + max_len_rate + 1, "-"))
        for row in rows:
            print(f"{row[0].ljust(max_len_name)} {row[1]:.2f}")
    except Error as e:
       print(e)
def query8(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 'Administrator' AS Role, COUNT(*) AS cnt FROM Administrator
            UNION
            SELECT 'Salesmen' AS Role, COUNT(*) AS cnt FROM Salesman
            UNION
            SELECT 'Technicians' AS Role, COUNT(*) AS cnt FROM TechnicalSupport
            """)
        rows = cursor.fetchall()
        max_len = max(len(row[0]) for row in rows)
        print(f"{'Role'.ljust(max_len)} {'cnt'}")
        print("------------------")
        for row in rows:
            print(f"{row[0].ljust(max_len)} {row[1]}")
    except Error as e:
       print(e)


def main():

    database = r"ABC.sqlite"

    conn = create_connection(database)
    if conn is not None:

        queryNumber = int(sys.argv[1])

        if queryNumber == 1:
            query1(conn)
        elif queryNumber == 2:
            query2(conn)
        elif queryNumber == 3:
            query3(conn)
        elif queryNumber == 4:
            query4(conn)
        elif queryNumber == 5:
            query5(conn)
        elif queryNumber==6:
            query6(conn)
        elif queryNumber==7:
            query7(conn)
        elif queryNumber==8:
            query8(conn)
        close_connection(conn)

    else:
        print("Something went wrong with the database connection.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

