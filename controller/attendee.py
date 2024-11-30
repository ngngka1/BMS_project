import sqlite3
from controller.base import BaseController
from model.attendee import AttendeeModel
from view.attendee import AttendeeView
from utils.miscellaneous.type_cast import *
from settings import get_session_data, start_session, stop_session
from utils.auth.decorators import admin_required, authenticated_required
from controller.attend import AttendController

class AttendeeController(BaseController):
    model_class = AttendeeModel
    view_class = AttendeeView
    
    @staticmethod
    def handle_input(*args):
        if not args: return
        command = args[0].lower()
        new_args = args[1:]
        if command == "help":
            AttendeeController.view.help()
        elif command == 'register':
            AttendeeController.register(*new_args)
        elif command == 'login':
            AttendeeController.login(*new_args)
        elif command == "info":
            AttendeeController.get_information()
        elif command == "logout":
            AttendeeController.logout()
        elif command == 'update':
            AttendeeController.update(*new_args)
        elif command == 'getbyemail':
            AttendeeController.get_information_by_email(*new_args)
        elif command == 'updatebyemail':
            AttendeeController.update_information_by_email(*new_args)
        elif command == "attend":
            AttendeeController.update_attendence(*new_args)
        
    @staticmethod
    @admin_required
    def update_attendence(*args):
        kwargs = AttendeeController.smart_input(*args, **{
            "bin": to_int,
            "account_id": to_int,
        })
        kwargs["present"] = True
        AttendController.update(**kwargs)
        print("attendence updated successfully")
        
    @staticmethod
    def login(*args):
        kwargs = AttendeeController.smart_input(*args, **{
            "email_address": to_string,
            "password": to_string
        })
        AttendeeController.model.login(**kwargs)
        
    # @staticmethod
    # def

    @staticmethod
    @authenticated_required
    def logout():
        stop_session()
        print("logged out sucessfully")

    @staticmethod
    @authenticated_required
    def update(*args):
        kwargs = AttendeeController.smart_input(*args, **{
            "email_address": allow_null_wrapper(to_string),
            "password": allow_null_wrapper(to_string),
            "first_name": allow_null_wrapper(to_string),
            "last_name": allow_null_wrapper(to_string),
            "type": allow_null_wrapper(to_string),
            "phone_no": allow_null_wrapper(to_string),
            "address": allow_null_wrapper(to_string),
            "organization": allow_null_wrapper(to_string),
        })
        kwargs["old_email_address"] = get_session_data("email_address")
        kwargs["password"] = kwargs["password"] if kwargs["password"] else get_session_data("password")
        AttendeeController.model.update(**kwargs)
        start_session(**{
            "email_address": kwargs["email_address"] if kwargs["email_address"] else get_session_data("email_address"),
            "password": kwargs["password"]
        })
        
    @staticmethod
    def register(*args):
        kwargs = AttendeeController.smart_input(*args, **{
            "email_address": to_string,
            "password": to_string,
            "first_name": to_string,
            "last_name": to_string,
            "type": to_string,
            "phone_no": to_string,
            "address": to_string,
            "organization": to_string,
        })
        AttendeeController.model.insert(**kwargs)
        
    @staticmethod
    @authenticated_required
    def get_information():
        AttendeeController.view.display(AttendeeController.model.get_information_by_email(get_session_data("email_address")))
        
    @staticmethod
    @admin_required
    def get_information_by_email(*args):
        AttendeeController.view.display(AttendeeController.model.get_information_by_email(args[0]))
        
    @staticmethod
    @admin_required
    def update_information_by_email(*args):
        kwargs = AttendeeController.smart_input(*args, **{
            "email_address": to_string,
            "first_name": allow_null_wrapper(to_string),
            "last_name": allow_null_wrapper(to_string),
            "type": allow_null_wrapper(to_string),
            "phone_no": allow_null_wrapper(to_string),
            "address": allow_null_wrapper(to_string),
            "organization": allow_null_wrapper(to_string),
        })
        AttendeeController.model.update_information_by_email(**kwargs)