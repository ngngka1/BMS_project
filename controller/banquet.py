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
            
    @staticmethod
    @authenticated_required
    def list_all():
        BanquetController.view.display(BanquetController.model.list_all())
        
    @staticmethod
    @authenticated_required
    def register(*args):
        kwargs = BanquetController.smart_input(*args, **{
            "bin": to_int,
            "drink_choice": to_string_allow_null,
            "meal_choice": to_string_allow_null,
            "remarks": to_string_allow_null,
        })
        kwargs["email_address"] = get_session_data("email_address")
        if BanquetController.check_available(**kwargs):
            AttendController.create(**kwargs)
        
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
        
    @staticmethod
    @authenticated_required
    def check_available(**kwargs):
        row = dict(BanquetController.model.get_one(kwargs["bin"]))
        if not row or row["quota"] == 0:
            raise ForbiddenException("The banquet is already full")
        row["quota"] -= 1
        if row["quota"] <= 0:
            row["quota"] = 0
            row["available"] = False
        BanquetController.model.update(**row)
        return True
    
    @staticmethod
    @admin_required
    def update(*args):
        kwargs = BanquetController.smart_input(*args, **{
            "bin": to_int,
            "name": to_string,
            "date_and_time": to_date_string,
            "address": to_string,
            "location": to_string,
            "meal_nos": to_list_from_string,
            "staff_no": to_int,
            "quota": to_int,
            "available": to_boolean,
        })
        BanquetController.model.update(**kwargs)

