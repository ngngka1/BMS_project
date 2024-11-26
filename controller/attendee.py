import sqlite3
from model.attendee import AttendeeModel
from view.attendee import AttendeeView
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
        elif command == 'update':
            AttendeeController.update(args)
        
    def __init__(self):
        '''
            Note: should call AttendeeController.init() instead, the controller instance is not used
        '''
        AttendeeController.init()

    @staticmethod
    def update(*args):
        AttendeeController.__view.results = AttendeeController.__model.update(*args)
        AttendeeController.__view.display()
        
    @staticmethod
    def register(*args):
        AttendeeController.__view.results = AttendeeController.__model.insert(*args)
        
        AttendeeController.__view.display()
        

        