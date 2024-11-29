import sqlite3
from model.staff import StaffModel
from view.staff import StaffView
from controller.base import BaseController
class StaffController(BaseController):
    model_class = StaffModel
    view_class = StaffView
        
    @staticmethod
    def handle_input(*args):
        if not args: return
        command = args[0].lower()
        args = args[1:]
        if command == "help":
            StaffController.view.help()
