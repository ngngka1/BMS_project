
SESSION_DATA = {
    'admin_mode': False,
    "email_address": None,
    "password": None,
}

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
