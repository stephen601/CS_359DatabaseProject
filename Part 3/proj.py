import sqlite3
from sqlite3 import Error
import sys

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


def main():
    database = r"ABC.sqlite"

    conn = create_connection(database)
    if conn is not None:

        queryNumber = sys.argv[1]

        queryNumber = int(queryNumber)
        
        if queryNumber==1:
            parameter = sys.argv[2]    
            print("temp")
        elif queryNumber==2:
            parameter = sys.argv[2]     
            print("temp")
        elif queryNumber==3:
            print("temp")
        elif queryNumber==4:
            parameter = sys.argv[2]     
            print("temp")
        elif queryNumber==5:
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
        elif queryNumber==6:
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
            except Error as e:
                print(e)
        elif queryNumber==7:
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
        elif queryNumber==8:
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

        close_connection(conn)

    else:
        print("Something went wrong with the database connection.")


if __name__ == '__main__':
    main()
