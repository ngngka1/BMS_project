import sqlite3
from model.staff import StaffModel
from view.staff import StaffView
class StaffController:
    __view = None
    __model = None
    def init(db_connection: sqlite3.Connection):
        __model = StaffModel(db_connection)
        __view = StaffView()
        
    @staticmethod
    def handle_input(*args):
        command = args[0]
        args = args[1:]
