from datetime import datetime
import re

def to_string(x):
    return str(x)

def to_string_allow_null(x):
    x = str(x)
    return x if x else "NA"

def to_date_string(x):
    datetime.strptime(x, '%Y/%m/%d')
    return x

def to_int(x):
    return int(x)

def to_list_from_string(x):
    if (not re.match(r"^[\[]{1}(.+)([,]{1}.+)*[\]]{1}$", x)):
        raise ValueError("Not a string in list format (e.g. should be [1,2,3,4] etc.)")
    return (x[1:-1]).replace(' ', '').split(',') # example: [1, 2, 5, 6]
    

def to_boolean(x):
    x = x.lower()
    if x == "true" or x == "0":
        return True
    if x == "false" or x == "1":
        return False
    raise ValueError("Not castable to boolean")
