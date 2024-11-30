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
        elif command == 'attendance':
            ReportController.attendance()
        elif command == 'staffattendance':
            ReportController.staff_attendance()
        elif command == 'popularmeals':
            ReportController.popular_meals()
        elif command == "attendeetypes":
            ReportController.attendee_types()
            
    @staticmethod
    def attendee_types():
        results = ReportController.model.attendee_types()
        ReportController.view.display(results)
        if len(results) >= 1:
            print("Attendee types report:")
            if len(results) == 1:
                print(f"\tAll attendees are: {results[0]['type']}")
                print(f"\tattendance percentage: {results[0]['percentage']}")
            else:
                print(f"\tMost of the attendees are: {results[0]['type']}")
                print(f"\tLeast of the attendees are: {results[-1]['type']}")
                print()
                min_attendance = max_attendance = results[0]
                for x in results:
                    min_attendance = x if min_attendance["attendance_percentage"] > x["attendance_percentage"] else min_attendance
                    max_attendance = x if max_attendance["attendance_percentage"] < x["attendance_percentage"] else max_attendance
                print(f"\ttype of attendees that has the highest attendance: {max_attendance['type']}: {max_attendance['attendance_percentage']}%")
                print(f"\ttype of attendees that has the lowest attendance: {min_attendance['type']}: {min_attendance['attendance_percentage']}%")
        
    @staticmethod
    def attendance():
        results = ReportController.model.attendance()
        ReportController.view.display(results)
        if len(results) >= 1:
            print("attendance report:")
            print(f"\tBanquet with the high attendance percentage:")
            print(f"\t\t{results[0]['banquet_name']}: {results[0]['attendance_percentage']}%")
            if len(results) > 1:
                print(f"\tBanquet with the least attendance percentage:")
                print(f"\t\t{results[-1]['banquet_name']}: {results[-1]['attendance_percentage']}%")
    
    @staticmethod
    def popular_meals():
        results = ReportController.model.popular_meals()
        ReportController.view.display(results)
        print("Top meals in all banquets:")
        for i, row in enumerate(results):
            print(f"\t{i+1}. {row['dish_name']}")
        
    @staticmethod
    def staff_attendance():
        results = ReportController.model.staff_attendance()
        ReportController.view.display(results)
        if len(results) >= 1:
            print("Staff attendance report:")
            print(f"\tstaff with the highest attendance is:")
            print(f"\t\t{results[0]['first_name']}: {results[0]['attendance_percentage']}%")
            if len(results) > 1:
                print(f"\tstaff with the lowest attendance:")
                print(f"\t\t{results[-1]['first_name']}: {results[-1]['attendance_percentage']}%")