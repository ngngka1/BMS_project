from settings import check_admin_mode
from exceptions.ForbiddenException import ForbiddenException

def admin_required(func):
    def wrapper(*args, **kwargs):
        if not check_admin_mode():
            raise ForbiddenException("No permission for this action!")
        func(*args, **kwargs)
    return wrapper

def authenticate(func):
    def wrapper(*args, **kwargs):
        
        # if not SESSION_DATA.get("email_address") or not SESSION_DATA.get("password"):
        #     raise ForbiddenException("Please login first!")
        func(*args, **kwargs)
    return wrapper