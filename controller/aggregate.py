from controller.base import BaseController
from controller.attendee import AttendeeController
from controller.attend import AttendController
from controller.banquet import BanquetController
from controller.meal import MealController
from controller.staff import StaffController
from controller.provide import ProvideController
from controller.maintain import MaintainController
from controller.report import ReportController
from utils.exceptions.TerminationException import TerminationException
import shlex
from settings import check_debug_mode, check_admin_mode
from view.aggregate import AggregateView

class AggregateController:
    view: AggregateView = None
    @staticmethod
    def rollback():
        BaseController.rollback()
        
    def commit():
        BaseController.commit()
    
    @staticmethod
    def init(db_connection):
        # BaseController(db_connection)
        AttendeeController.init(db_connection)
        AttendController.init(db_connection)
        BanquetController.init(db_connection)
        MealController.init(db_connection)
        StaffController.init(db_connection)
        ProvideController.init(db_connection)
        MaintainController.init(db_connection)
        ReportController.init(db_connection)
        AggregateController.view = AggregateView()
        AggregateController.view.help()
    
    def __init__(self, db_connection):
        AggregateController.init(db_connection)
        
    @staticmethod
    def redirect(input: str):
        print(input if check_debug_mode() else "")
        args = shlex.split(input)
        if not args: return
        table = args[0].lower() # might as well just make the commands case-insensitive
        new_args = args[1:] if len(args) > 1 else []
        if table == "quit":
            raise TerminationException()
        elif table == "help":
            AggregateController.view.help()
        elif table == "attendee":
            AttendeeController.handle_input(*new_args)
        elif table == "banquet":
            BanquetController.handle_input(*new_args)
        elif table == "meal":
            MealController.handle_input(*new_args)
        else:
            if not check_admin_mode():
                return
            if table == "staff":
                StaffController.handle_input(*new_args)
            elif table == "report":
                ReportController.handle_input(*new_args)
            
