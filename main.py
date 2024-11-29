import sqlite3
from settings import start_db_connection
from controller.aggregate import AggregateController
from utils.exceptions.TerminationException import TerminationException
from utils.exceptions.ForbiddenException import ForbiddenException
import re

def main():
    db_connection = sqlite3.connect('bms.db')
    db_connection.create_function('regexp', 2, lambda x, y: 1 if re.search(x,y) else 0)
    start_db_connection(db_connection)
    try:
        AggregateController.init(db_connection)
        while True:
            try:
                AggregateController.redirect(input("\nEnter command:\n"))
            except sqlite3.IntegrityError as e:
                print("Integrity error:", e.args[0])
            except ForbiddenException as e:
                print(e.args[0])
    except TerminationException:
        pass
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(type(e))
        print(repr(e))
        print("fatal exception: ", e.args[0], "\n, terminating system")
    finally:
        db_connection.close()
        print("System terminated")
        
if __name__ == "__main__":
    main()