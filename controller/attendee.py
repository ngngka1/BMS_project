import sqlite3
from model.attendee import AttendeeModel
from view.attendee import AttendeeView
from utils.exceptions.InadequateArgumentsException import InadequateArgumentsException
class AttendeeController:
    __view: AttendeeView = None
    __model: AttendeeModel = None
    @staticmethod
    def init(db_connection: sqlite3.Connection):
        AttendeeController.__model = AttendeeModel(db_connection)
        AttendeeController.__view = AttendeeView()
        
    @staticmethod
    def handle_input(*args):
        command = args[0]
        args = args[1:]
        if command == 'register':
            AttendeeController.register(args)
        elif command == 'login':
            AttendeeController.login(args)
        elif command == 'update':
            AttendeeController.update(args)
        
    def __init__(self):
        AttendeeController.init()

    @staticmethod
    def login(*args):
        kwargs = {
            "email_address": None,
            "password": None
        }
        for i, key in enumerate(kwargs.keys()):
            if (i == len(args)):
                raise InadequateArgumentsException(f"Missing Argument: {key}")
            kwargs[key] = args[i]
        AttendeeController.__view.results = AttendeeController.__model.login(kwargs)
        AttendeeController.__view.display()

    @staticmethod
    def update(*args):
        kwargs = {
            "email_address": None,
            "password": None,
            "first_name": None,
            "last_name": None,
            "type": None,
            "phone_no": None,
            "address": None,
            "organization": None,
        }
        for i, key in enumerate(kwargs.keys()):
            if (i == len(args)):
                raise InadequateArgumentsException(f"Missing Argument: {key}")
            kwargs[key] = args[i]
        AttendeeController.__view.results = AttendeeController.__model.update(*args)
        AttendeeController.__view.display()
        
    @staticmethod
    def register(*args):
        kwargs = {
            "email_address": None,
            "password": None,
            "first_name": None,
            "last_name": None,
            "type": None,
            "phone_no": None,
            "address": None,
            "organization": None,
        }
        for i, key in enumerate(kwargs.keys()):
            if (i == len(args)):
                raise InadequateArgumentsException(f"Missing Argument: {key}")
            kwargs[key] = args[i]
        AttendeeController.__view.results = AttendeeController.__model.insert(**kwargs)
        AttendeeController.__view.display()