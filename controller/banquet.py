import sqlite3
from view.banquet import BanquetView
from model.banquet import BanquetModel
from utils.miscellaneous.smart_input import smart_input

class BanquetController:
    __view: BanquetView = None
    __model: BanquetModel = None
    @staticmethod
    def init(db_connection: sqlite3.Connection):
        BanquetController.__model = BanquetModel(db_connection)
        BanquetController.__view = BanquetView()
        
    @staticmethod
    def handle_input(*args):
        command = args[0]
        args = args[1:]
        if command == "help":
            BanquetController.__view.help()
        if command == 'list':
            BanquetController.list_all()
        elif command == "create":
            BanquetController.create(*args)
        elif command == "update":
            BanquetController.update(*args)
            
    def list_all():
        BanquetController.__view.results = BanquetController.__model.list_all()
        BanquetController.__view.display()
        
    def create(*args):
        kwargs = smart_input(*args, {
            "name": None,
            "date_and_time": None,
            "address": None,
            "location": None,
            "staff_no": None,
            "quota": None,
            "available": None,
        })
        BanquetController.__model.insert(**kwargs)
    
    def update(*args):
        kwargs = smart_input(*args, {
            "email_address": None,
            "password": None
        })
        BanquetController.__model.update(**kwargs)

