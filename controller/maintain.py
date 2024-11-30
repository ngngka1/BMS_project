import sqlite3
from model.maintain import MaintainModel
from controller.base import BaseController
from utils.miscellaneous.type_cast import *
from utils.auth.decorators import admin_required 
class MaintainController(BaseController):
    model_class = MaintainModel
        
    @staticmethod
    @admin_required
    def create(*args):
        kwargs = {
            "present": args[0],
            "staff_no": int(args[1]),
            "bin": int(args[2]),
        }
        MaintainController.model.insert(**kwargs)
        
    @staticmethod
    @admin_required
    def update(**kwargs):
        MaintainController.model.update(**kwargs)
        
