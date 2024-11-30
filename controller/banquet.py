import sqlite3
from view.banquet import BanquetView
from model.banquet import BanquetModel
from controller.provide import ProvideController
from controller.base import BaseController
from controller.maintain import MaintainController
from controller.attend import AttendController
from utils.miscellaneous.type_cast import *
from utils.auth.decorators import admin_required, authenticated_required
from settings import get_session_data
from utils.exceptions.ForbiddenException import ForbiddenException

class BanquetController(BaseController):
    model_class = BanquetModel
    view_class = BanquetView
    @staticmethod
    def handle_input(*args):
        if not args: return
        command = args[0].lower()
        new_args = args[1:]
        if command == "help":
            BanquetController.view.help()
        elif command == 'list':
            BanquetController.list_all()
        elif command == "register":
            BanquetController.register(*new_args)
        elif command == "create":
            BanquetController.create(*new_args)
        elif command == "update":
            BanquetController.update(*new_args)
        elif command == "attendedby":
            BanquetController.update_attendence(*new_args)
        elif command == "listattendees":
            BanquetController.get_attendees(*new_args)
            
    @staticmethod
    @admin_required
    def get_attendees(*args):
        kwargs = BanquetController.smart_input(*args, **{
            "bin": to_int,
        })
        BanquetController.view.display(BanquetController.model.get_attendees(kwargs["bin"]))
            
    @staticmethod
    @admin_required
    def update_attendence(*args):
        kwargs = BanquetController.smart_input(*args, **{
            "account_id": to_int,
            "bin": to_int,
        })
        AttendController.update(**kwargs)
        print("attendence updated successfully")
        
    @staticmethod
    @authenticated_required
    def list_all():
        BanquetController.view.display(BanquetController.model.list_all())
        
    @staticmethod
    @authenticated_required
    def register(*args):
        kwargs = BanquetController.smart_input(*args, **{
            "bin": to_int,
            "drink_choice": allow_null_wrapper(to_string),
            "meal_choice": allow_null_wrapper(to_string),
            "remarks": allow_null_wrapper(to_string),
        })
        kwargs["account_id"] = get_session_data("account_id")
        
        if BanquetController.check_available(**kwargs):
            AttendController.create(**kwargs)
            print(f"you have registered banquet {kwargs['bin']} successfully")
        
    @staticmethod
    @admin_required
    def create(*args):
        kwargs: dict = BanquetController.smart_input(*args, **{
            "name": to_string,
            "date_and_time": to_date_string,
            "address": to_string,
            "location": to_string,
            "meal_nos": to_list_from_string,
            "staff_no": to_int,
            "quota": to_int,
            "available": to_boolean,
        })
        meal_nos = kwargs.pop("meal_nos")
        staff_no = kwargs.pop("staff_no")
        bin_id = BanquetController.model.insert(return_pk=True, **kwargs)
        ProvideController.create(bin_id, meal_nos)
        MaintainController.create(None, staff_no, bin_id)
        print(f"Banquet created successfully:")
        BanquetController.view.display([BanquetController.model.get_one(bin_id)])
        
        
    @staticmethod
    @authenticated_required
    def check_available(**kwargs):
        row = BanquetController.model.get_one(kwargs["bin"])
        if not row:
            raise ForbiddenException("The banquet with the specified bin does not exist")
        row = dict(row)
        if row["quota"] == 0:
            if row["available"]:
                row["available"] = True
                BanquetController.model.update(**row)
            raise ForbiddenException("The banquet is already full")
        row["quota"] = row["quota"] - 1
        print("row['quota']:", row["quota"])
        print("type of row['quota']:", type(row["quota"]))
        if row["quota"] == 0:
            row["available"] = False
        BanquetController.model.update(**row)
        return True
    
    @staticmethod
    @admin_required
    def update(*args):
        kwargs = BanquetController.smart_input(*args, **{
            "bin": to_int,
            "name": allow_null_wrapper(to_string),
            "date_and_time": allow_null_wrapper(to_date_string),
            "address": allow_null_wrapper(to_string),
            "location": allow_null_wrapper(to_string),
            "meal_nos": allow_null_wrapper(to_list_from_string),
            "staff_no": allow_null_wrapper(to_int),
            "quota": allow_null_wrapper(to_int),
            "available": allow_null_wrapper(to_boolean),
        })
        BanquetController.model.update(**kwargs)
        print("banquet updated successfully:")
        BanquetController.view.display(BanquetController.model.get_one(kwargs["bin"]))

