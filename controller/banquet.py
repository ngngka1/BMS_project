import sqlite3
from view.banquet import BanquetView
from model.banquet import BanquetModel

class BanquetController:
    __view = None
    __model = None
    def init(db_connection: sqlite3.Connection):
        __model = BanquetModel(db_connection)
        __view = BanquetView()
        
    @staticmethod
    def handle_input(*args):
        command = args[0]
        args = args[1:]
        
    def create(*args):
        pass
    
    def update(*args):
        pass

