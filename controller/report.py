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
        elif command == 'attendence':
            ReportController.attendence()
        elif command == 'staffattendence':
            ReportController.staff_attendence()
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
                print(f"\tattendence percentage: {results[0]['percentage']}")
            else:
                print(f"\tMost of the attendees are: {results[0]['type']}")
                print(f"\tLeast of the attendees are: {results[-1]['type']}")
                print()
                min_attendence = max_attendence = results[0]
                for x in results:
                    min_attendence = x if min_attendence["attendence_percentage"] > x["attendence_percentage"] else min_attendence
                    max_attendence = x if max_attendence["attendence_percentage"] < x["attendence_percentage"] else max_attendence
                print(f"\ttype of attendees that has the highest attendence: {max_attendence['type']}: {max_attendence['attendence_percentage']}%")
                print(f"\ttype of attendees that has the lowest attendence: {min_attendence['type']}: {min_attendence['attendence_percentage']}%")
        
    @staticmethod
    def attendence():
        results = ReportController.model.attendence()
        ReportController.view.display(results)
        if len(results) >= 1:
            print("attendence report:")
            print(f"\tBanquet with the high attendence percentage:")
            print(f"\t\t{results[0]['banquet_name']}: {results[0]['attendence_percentage']}")
            if len(results) > 1:
                print(f"\tBanquet with the least attendence percentage:")
                print(f"\t\t{results[-1]['banquet_name']}: {results[-1]['attendence_percentage']}")
    
    @staticmethod
    def popular_meals():
        results = ReportController.model.popular_meals()
        ReportController.view.display(results)
        print("Top meals in all banquets:")
        for i, row in enumerate(results):
            print(f"\t{i+1}. {row['dish_name']}")
        
    @staticmethod
    def staff_attendence():
        results = ReportController.model.staff_attendence()
        ReportController.view.display(results)
        if len(results) >= 1:
            print("Staff attendence report:")
            print(f"\tstaff with the highest attendence is:")
            print(f"\t\t{results[0]['first_name']}: {results[0]['attendence_percentage']}")
            if len(results) > 1:
                print(f"\tstaff with the lowest attendence:")
                print(f"\t\t{results[-1]['first_name']}: {results[-1]['attendence_percentage']}")