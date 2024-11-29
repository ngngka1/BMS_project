import sqlite3
from controller.base import BaseController
from model.meal import MealModel
from view.meal import MealView
from utils.miscellaneous.smart_input import smart_input
from utils.miscellaneous.type_cast import *
class MealController(BaseController):
    model_class = MealModel
    view_class = MealView
        
    @staticmethod
    def handle_input(*args):
        if not args: return
        command = args[0].lower()
        new_args = args[1:]
        if command == "help":
            MealController.view.help()
        elif command == "list":
            MealController.view.display(MealController.model.list_all())
        elif command == "create":
            MealController.create(*new_args)
        elif command == "update":
            MealController.update(*new_args)
       
    @staticmethod     
    def create(*args):
        kwargs = smart_input(*args, **{
            "type": to_string,
            "dish_name": to_string,
            "price": to_int,
            "special_cuisine": to_string,
        })
        MealController.model.insert(**args)
        
    @staticmethod     
    def create(*args):
        kwargs = smart_input(*args, **{
            "type": to_string,
            "dish_name": to_string,
            "price": to_int,
            "special_cuisine": to_string,
        })
        MealController.model.insert(**kwargs)
