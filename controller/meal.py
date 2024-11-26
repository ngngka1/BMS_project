import sqlite3
from model.meal import MealModel
from view.meal import MealView
class MealController:
    __view = None
    __model = None
    def init(db_connection: sqlite3.Connection):
        __model = MealModel(db_connection)
        __view = MealView()
        
    @staticmethod
    def handle_input(*args):
        command = args[0]
        args = args[1:]
