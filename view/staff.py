from view.base import BaseView
class StaffView(BaseView):
    __COMMANDS_DESC = {
        "Staff help": "Show this help message",
    }
    __ADMIN_COMMANDS_DESC = {
        "Staff create <first_name> <last_name> <department>": "create a Staff record",
        "Staff update <first_name> <last_name> <department>": "update a Staff record"
    }
    __TABLE_NAME = "Staff"