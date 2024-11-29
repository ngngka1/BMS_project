import sqlite3
from settings import start_db_connection
from controller.aggregate import AggregateController
from utils.exceptions.TerminationException import TerminationException
from utils.exceptions.ForbiddenException import ForbiddenException
import re
import argparse
from settings import enable_admin_mode

def main(db_path='bms.db'):
    db_connection = sqlite3.connect(db_path)
    db_connection.create_function('regexp', 2, lambda x, y: 1 if re.search(x,y) else 0)
    db_connection.row_factory = sqlite3.Row
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
    parser = argparse.ArgumentParser()
    parser.add_argument('--db', type=str, help='relative path to the database')
    parser.add_argument('--admin', action='store_true', help='indicate if it is admin mode is enabled')
    parser.add_argument('--auto-remove', action='store_true', help='indicate whether the database at specified path at -db will be removed when program terminates')
    parsed_args = parser.parse_args()
    if parsed_args.admin:
        enable_admin_mode()
    if parsed_args.db:
        main(parsed_args.db)
    else:
        main()
    if parsed_args.db and parsed_args.auto_remove:
        import os
        os.remove(parsed_args.db)