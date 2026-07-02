import sqlite3
import subprocess
import pickle

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchone()

def ping_host(hostname):
    # Use subprocess without shell=True to prevent command injection
    try:
        result = subprocess.run(["ping", "-c", "1", hostname], capture_output=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.output

def load_data(data_bytes):
    # Raise an exception if input appears to be untrusted
    if is_data_trusted(data_bytes):
        return pickle.loads(data_bytes)
    else:
        raise ValueError("Untrusted data")

def is_data_trusted(data_bytes):
    # Implement a function to check if data_bytes comes from a trusted source
    # Return True if trusted, False otherwise
    pass
