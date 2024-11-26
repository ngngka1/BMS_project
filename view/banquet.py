from view.base import BaseView
class BanquetView(BaseView):
    __COMMANDS_DESC = {
        "Banquet help": "Show this help message",
        "Banquet list": "list the available banquets (login required)"
    }
    __ADMIN_COMMANDS_DESC = {
        "Banquet create <name> <date_and_time> <address> <location> <contact_staff_first_name> <contact_staff_last_name> <available> <quota>": "create a banquet record",
        "Banquet update <name> <date_and_time> <address> <location> <contact_staff_first_name> <contact_staff_last_name> <available> <quota>": "update a banquet record"
    }
    __TABLE_NAME = "Banquet"