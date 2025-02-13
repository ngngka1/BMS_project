from view.base import BaseView
class StaffView(BaseView):
    def __init__(self):
        super().__init__()
        self.set_table_name("Staff")
        self.set_commands_description({
            "Staff help": "Show this help message",
        })
        self.set_admin_commands_description({
            "Staff list": "list all the staff",
            "Staff attend <staff_no> <bin>": "tick attendance of the staff on the banquet with bin",
            "Staff create <first_name> <last_name> <department>": "create a Staff record",
            "Staff update <staff_no> <first_name> <last_name> <department>": "update a Staff record"
        })
        self.add_argument_prompt({
            "staff_no": "Input the staff no. of the contact staff",
            "department": "catering, events services, kitchen staff, bar services, facilities management, audio and visual, decor and design, guest services, security"
        })