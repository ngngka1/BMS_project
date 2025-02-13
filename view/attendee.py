from view.base import BaseView
class AttendeeView(BaseView):
    def __init__(self):
        super().__init__()
        self.set_table_name("Attendee")
        self.set_commands_description({
            "Attendee help": "Show this help message",
            "Attendee register <email_address> <password> <first_name> <last_name> <type> <phone_no> <address> <organization>": "Register an Attendee",
            "Attendee login <email_address> <password>": "login with email and password",
            "Attendee info": "Show info of logged in user",
            "Attendee update <email_address> <password> <first_name> <last_name> <type> <phone_no> <address> <organization>": "Update the information of the attendee (login required)",
        })
        self.set_admin_commands_description({
            "Attendee attend <account_id> <bin>": "tick attendance of the attendee on the banquet with bin",
            "Attendee getByEmail <email_address>": "get an attendee's information by their email address",
            "Attendee updateByEmail <email_address> <first_name> <last_name> <type> <phone_no> <address> <organization>": "update an attendee's information by their email address",
        })
        self.add_argument_prompt({
            "first_name": "Only english name is accepted",
            "last_name": "Only english name is accepted",
            "phone_no": "8-character long number",
            "type": "staff, student, alumni, guest",
            "organization": "polyu, speed, hkcc, others"
        })
    