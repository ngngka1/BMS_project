from view.base import BaseView
class ReportView(BaseView):
    def __init__(self):
        super().__init__()
        self.set_table_name("Report")
        self.set_admin_commands_description({
            "Report help": "Show this help message",
            "Report attendance": "show the attendance behavior of attendees for banquets",
            "Report staffAttendance": "show the attendance behavior of staff for banquets",
            "Report popularMeals": "show the attendance behavior of staff for banquets",
            "Report attendeeTypes": "show the percentage of different types of attendance",
        })
    