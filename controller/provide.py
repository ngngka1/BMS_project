import sqlite3
from model.provide import ProvideModel
from utils.miscellaneous.smart_input import smart_input
from controller.base import BaseController

class ProvideController(BaseController):
    model_class = ProvideModel
        
    @staticmethod
    def create(*args):
        bin_id = args[0]
        meal_nos = args[1]
        print("bin_id:", bin_id)
        print("meal_nos:", meal_nos)
        if (len(meal_nos) < 4):
            print("input at least four different meals!")
            return
        for meal_no in meal_nos:
            ProvideController.model.insert(**{
                "bin": bin_id,
                "meal_no": meal_no
            })