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
        parameter = sys.argv[2]
        queryNumber = int(queryNumber)
        
        if queryNumber==1:
            print("temp")
        elif queryNumber==2:
            print("temp")
        elif queryNumber==3:
            print("temp")
        elif queryNumber==4:
            print("temp")
        elif queryNumber==5:
            print("temp")
        elif queryNumber==6:
            print("temp")
        elif queryNumber==7:
            print("temp")
        elif queryNumber==8:
            print("temp")

        close_connection(conn)

    else:
        print("Something went wrong with the database connection.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

