import unittest
import os
import mysql.connector
import sys

from main import hello

class TestUserName(unittest.TestCase):
    def test_false_hello(self):
        result = hello()
        assert result != "hello world, dorian"

    def test_hello(self):
        result = hello()
        assert result == "hello world, Dorian"

    def test_database_status(self):
        conn = mysql.connector.connect(host=os.environ["MYSQL_HOST"],
                                       port=os.environ["MYSQL_PORT"],
                                       database=os.environ["MYSQL_DATABASE"],
                                       user=os.environ["MYSQL_USER"],
                                       password=os.environ["MYSQL_PASSWORD"])

        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT name FROM Users LIMIT 1")
            data = cursor.fetchone()

            assert data is not None

        finally:
            if conn is not None and conn.is_connected():
                conn.close()

if __name__ == '__main__':
    unittest.main()

