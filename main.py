import sqlite3

from controller.aggregate import AggregateController
from utils.exceptions.termination import TerminationException

def main():
    db_connection = sqlite3.connect('example.db')
    AggregateController.init(db_connection)
    try:
        while True:
            AggregateController.redirect(input("Enter command:\n"))
    except TerminationException:
        pass
    finally:
        print("System terminated")
        
if __name__ == "__main__":
    main()