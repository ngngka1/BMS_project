
from controller.attendee import AttendeeController
from controller.banquet import BanquetController
from controller.meals import MealsController
from controller.staff import StaffController

class AggregateController:
    @staticmethod
    def init(db_connection):
        AttendeeController.init(db_connection)
        BanquetController.init(db_connection)
        MealsController.init(db_connection)
        StaffController.init(db_connection)
    
    def __init__(self, db_connection):
        AggregateController.init(db_connection)
        
    @staticmethod
    def redirect(input: str):
        args = input.split(' ')
        table = args[0]
        args = args[1:]
        if table == "attendee":
            AttendeeController.handle_input(args)
        elif table == "banquet":
            BanquetController.handle_input(args)
        elif table == "staff":
            StaffController.handle_input(args)
        elif table == "meals":
            MealsController.handle_input(args)