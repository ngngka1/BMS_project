import sqlite3
from controller.base import BaseController
from model.attendee import AttendeeModel
from view.attendee import AttendeeView
from utils.miscellaneous.smart_input import smart_input
from settings import get_session_data
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
        elif command == 'update':
            AttendeeController.update(*new_args)
        elif command == 'getbyemail':
            AttendeeController.get_information_by_email(*new_args)
        
    @staticmethod
    def login(*args):
        kwargs = smart_input(*args, **{
            "email_address": None,
            "password": None
        })
        
        AttendeeController.view.results = AttendeeController.model.login(**kwargs)
        AttendeeController.view.display()

    @staticmethod
    def update(*args):
        kwargs = smart_input(*args, **{
            "first_name": None,
            "last_name": None,
            "type": None,
            "phone_no": None,
            "address": None,
            "organization": None,
        })
        kwargs["email_address"] = get_session_data("email_address")
        kwargs["password"] = get_session_data("password")
        AttendeeController.view.results = AttendeeController.model.update(**kwargs)
        AttendeeController.view.display()
        
    @staticmethod
    def register(*args):
        kwargs = smart_input(*args, **{
            "email_address": None,
            "password": None,
            "first_name": None,
            "last_name": None,
            "type": None,
            "phone_no": None,
            "address": None,
            "organization": None,
        })
        AttendeeController.view.results = AttendeeController.model.insert(**kwargs)
        AttendeeController.view.display()
        
    @staticmethod
    def get_information_by_email(*args):
        AttendeeController.view.results = AttendeeController.model.get_information_by_email(args[0])
        AttendeeController.view.display()
        
    @staticmethod
    def update_information_by_email(*args):
        kwargs = smart_input(*args, **{
            "email_address": None,
            "first_name": None,
            "last_name": None,
            "type": None,
            "phone_no": None,
            "address": None,
            "organization": None,
        })
        AttendeeController.view.results = AttendeeController.model.update_information_by_email(**kwargs)
        AttendeeController.view.display()
