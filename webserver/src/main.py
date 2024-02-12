import os
import sys
from flask import Flask
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)


@app.route("/")
def hello():
    conn = None
    data = None
    try:
        conn = mysql.connector.connect(host=os.environ["MYSQL_HOST"],
                                       port=os.environ["MYSQL_PORT"],
                                       database=os.environ["MYSQL_DATABASE"],
                                       user=os.environ["MYSQL_USER"],
                                       password=os.environ["MYSQL_PASSWORD"])
        if conn.is_connected():
            print('Connected to MySQL database')

            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT name FROM Users LIMIT 1")
            data = cursor.fetchone()

    except Error as e:
        print('Failed to connect to MySQL database', e, file=sys.stderr)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()

    return f'hello world, {data["name"]}' if data else "Data not found"


if __name__ == "__main__":
    app.run(debug=True)
