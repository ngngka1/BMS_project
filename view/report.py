from view.base import BaseView
class ReportView(BaseView):
    def __init__(self):
        super().__init__()
        self.set_table_name("Report")
        self.set_commands_description({
            # "Attendee update <email_address> <first_name> <last_name> <type> <phone_no> <address> <organization>": "Update the information of the attendee (login required)",
        })
        self.set_admin_commands_description({
            # "AttendeepdateByEmail <email_address> <first_name> <last_name> <type> <phone_no> <address> <organization>": "update an attendee's information by their email address"
        })
    