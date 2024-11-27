from utils.exceptions.ForbiddenException import ForbiddenException
import sqlite3
SESSION_DATA = {
    'admin_mode': False,
    "db_connection": None,
    "email_address": None,
    "password": None,
}

def start_db_connection(db_connection: sqlite3.Connection):
    SESSION_DATA["db_connection"] = db_connection
    
def get_db_connection() -> sqlite3.Connection:
    return SESSION_DATA.get("db_connection")

def start_session(**kwargs):
    SESSION_DATA["email_address"] = kwargs.get("email_address")
    SESSION_DATA["password"] = kwargs.get("password")
    
def get_session_data(key=None):
    if key: return SESSION_DATA.get(key)
    return {
        "email_address": SESSION_DATA.get("email_address"),
        "password": SESSION_DATA.get("password"),
    }

def check_admin_mode():
    return SESSION_DATA.get("admin_mode")

def enable_admin_mode():
    SESSION_DATA['admin_mode'] = True


def validate_session():
    if (check_admin_mode()):
        return
    if get_session_data("email_address") is None or get_session_data("password") is None:
        raise ForbiddenException("Please login first!")
    cursor = get_db_connection().cursor()
    try:
        with open("./model/sql_scripts/auth/query_user_by_credentials.sql", "r") as f:
            sql_command = f.read()
    except:
        raise OSError("Failed to read sql script")
    cursor.execute(sql_command.format(**get_session_data()))
    result = cursor.fetchone()
    if result is None:
        return ["Invalid session"]