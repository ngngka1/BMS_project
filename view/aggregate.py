from view.base import BaseView
class AggregateView(BaseView):
    __COMMANDS_DESC = {
        "help": "Show this help message",
        "Attendee help": "Show help messages for Attendee table",
        "Banquet help": "Show help messages for Banquet table",
        "Meal help": "Show help messages for Meal table",
        "Staff help": "Show help messages for Staff table",
    }
    
    __TABLE_NAME = "all"