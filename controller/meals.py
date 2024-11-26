import sqlite3
from model.meals import MealsModel
from view.meals import MealsView
class MealsController:
    __view = None
    __model = None
    def init(db_connection: sqlite3.Connection):
        __model = MealsModel(db_connection)
        __view = MealsView()
        
    @staticmethod
    def handle_input(*args):
        command = args[0]
        args = args[1:]
