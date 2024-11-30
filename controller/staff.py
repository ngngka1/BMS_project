import sqlite3
from model.staff import StaffModel
from view.staff import StaffView
from controller.base import BaseController
from controller.maintain import MaintainController
from utils.miscellaneous.type_cast import *
from utils.auth.decorators import admin_required

class StaffController(BaseController):
    model_class = StaffModel
    view_class = StaffView
        
    @staticmethod
    def handle_input(*args):
        if not args: return
        command = args[0].lower()
        new_args = args[1:]
        if command == "help":
            StaffController.view.help()
        elif command == "list":
            StaffController.list_all()
        elif command == "create":
            StaffController.create(*new_args)
        elif command == "attend":
            StaffController.attend(*new_args)
            
    @staticmethod
    @admin_required
    def list_all():
        StaffController.view.display(StaffController.model.list_all())
            
    @staticmethod
    @admin_required
    def create(*args):
        kwargs = StaffController.smart_input(*args, **{
            "first_name": to_string,
            "last_name": to_string,
            "department": to_string,
        })
        StaffController.model.insert(**kwargs)
        
    @staticmethod
    @admin_required
    def attend(*args):
        kwargs = StaffController.smart_input(*args, **{
            "staff_no": to_int,
            "bin": to_int,
        })
        kwargs["present"] = True
        MaintainController.model.update(**kwargs)
        print("staff attendence updated successfully")
