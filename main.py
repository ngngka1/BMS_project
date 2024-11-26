import sqlite3
from settings import start_db_connection
from controller.aggregate import AggregateController
from utils.exceptions.TerminationException import TerminationException

def main():
    db_connection = sqlite3.connect('bms.db')
    start_db_connection(db_connection)
    AggregateController.init(db_connection)
    try:
        while True:
            AggregateController.redirect(input("\nEnter command:\n"))
    except TerminationException:
        pass
    except Exception as e:
        print("fatal exception: ", e, "\n, terminating system")
    finally:
        db_connection.close()
        print("System terminated")
        
if __name__ == "__main__":
    main()