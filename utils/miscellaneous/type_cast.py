from datetime import datetime
import re

def allow_null_wrapper(func):
    def wrapper(x: str):
        if not x:
            return None
        return func(x)
    return wrapper

def to_string(x):
    return str(x)

def to_date_string(x):
    temp = x.split()
    if len(temp) != 2 and not re.match('^[0-9]{4}[-][0-9]{2}[-][0-9]{2} [0-9]{2}[:][0-9]{2}[:][0-9]{2}$', x):
        raise ValueError("Invalid date format")
    
    return x

def to_int(x):
    return int(x)

def to_list_from_string(x):
    if (not re.match(r"^[\[]{1}((.+)+([,]{1}.+)*)*[\]]{1}$", x)):
        raise ValueError("Not a string in list format (e.g. should be [1,2,3,4] etc.)")
    return list(x.strip() for x in (x[1:-1]).split(','))
    

def to_boolean(x):
    x = x.lower()
    if x == "true" or x == "0":
        return True
    if x == "false" or x == "1":
        return False
    raise ValueError("Not castable to boolean")
