from view.base import BaseView
class AttendeeView(BaseView):
    __COMMANDS_DESC = {
        "Attendee help": "Show this help message",
        "Attendee login <email_address> <password>": "login with email and password",
        "Attendee register <email_address> <password> <first_name> <last_name> <type> <phone_no> <address> <organization>": "Register an Attendee",
        "Attendee update <email_address> <password> <first_name> <last_name> <type> <phone_no> <address> <organization>": "Update the information of the attendee"
    }
    __ADMIN_COMMANDS_DESC = {
        "Attendee getByEmail <email_address>": "get an attendee's information by their email address"
    }
    __TABLE_NAME = "Attendee"
    