import sqlite3
from model.provide import ProvideModel
from controller.base import BaseController

class ProvideController(BaseController):
    model_class = ProvideModel
        
    @staticmethod
    def create(*args):
        bin_id = args[0]
        meal_nos = args[1]
        if (len(meal_nos) < 4):
            raise sqlite3.IntegrityError("input at least four different meals!")
        for meal_no in meal_nos:
            ProvideController.model.insert(**{
                "bin": bin_id,
                "meal_no": meal_no
            })