from view.base import BaseView
class ReportView(BaseView):
    def __init__(self):
        super().__init__()
        self.set_table_name("Report")
        self.set_admin_commands_description({
            "Report help": "Show this help message",
            "Report list": "list all the available reports",
        })
    