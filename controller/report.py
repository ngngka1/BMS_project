from controller.base import BaseController
from model.report import ReportModel
class ReportController(BaseController):
    model_class = ReportModel
    @staticmethod
    def handle_input(*args):
        if not args: return
        command = args[0].lower()
        new_args = args[1:]
        if command == "help":
            ReportController.view.help()
        elif command == "attendeetypes":
            ReportController.attendee_types()
        elif command == 'attendence':
            ReportController.attendence()
        elif command == 'popularmeals':
            ReportController.login(*new_args)
            
    @staticmethod
    def attendee_types():
        pass
    
    @staticmethod
    def attendence():
        pass
    
    @staticmethod
    def popular_meals():
        pass