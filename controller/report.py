from controller.base import BaseController
from model.report import ReportModel
from view.report import ReportView
class ReportController(BaseController):
    model_class = ReportModel
    view_class = ReportView
    @staticmethod
    def handle_input(*args):
        if not args: return
        command = args[0].lower()
        # new_args = args[1:]
        if command == "help":
            ReportController.view.help()
        elif command == "attendeetypes":
            ReportController.attendee_types()
        elif command == 'attendence':
            ReportController.attendence()
        elif command == 'popularmeals':
            ReportController.popular_meals()
            
    @staticmethod
    def attendee_types():
        ReportController.view.display(ReportController.model.attendee_types())
    
    @staticmethod
    def attendence():
        ReportController.view.display(ReportController.model.attendence())
    
    @staticmethod
    def popular_meals():
        ReportController.view.display(ReportController.model.popular_meals())
        
    @staticmethod
    def staff_attendence():
        ReportController.view.display(ReportController.model.staff_attendence())