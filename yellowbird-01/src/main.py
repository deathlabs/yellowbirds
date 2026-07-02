import sqlite3
import subprocess
import pickle

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()

def ping_host(hostname):
    result = subprocess.run("ping -c 1 " + hostname, shell=True, capture_output=True)
    return result.stdout

def load_data(data_bytes):
    return pickle.loads(data_bytes)
