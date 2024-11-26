from settings import check_admin_mode

def admin_required(func):
    def wrapper(*args, **kwargs):
        if not check_admin_mode():
            raise Exception("No permission for this action!")
        func(*args, **kwargs)
    return wrapper