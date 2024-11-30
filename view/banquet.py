from view.base import BaseView
class BanquetView(BaseView):
    def __init__(self):
        super().__init__()
        self.set_table_name("Banquet")
        self.set_commands_description({
            "Banquet help": "Show this help message",
            "Banquet list": "(login required) list all the available banquets",
            "Banquet list <criteria>": "(login required) list all the available banquets with specified criterion",
            "Banquet register <bin> <drink_choice> <meal_choice> <remarks>": " (login required) register an available banquet"
        })
        self.set_admin_commands_description({
            "Banquet create <name> <date_and_time> <address> <location> <meal_nos> <staff_no> <quota> <available>": "create a banquet record",
            "Banquet update <bin> <name> <date_and_time> <address> <location> <meal_nos> <staff_no> <quota> <available>": "update a banquet record",
            "Banquet listAttendees <bin>": "list all the attendees for a banquet with the bin"
        })
        self.add_argument_prompt({
            "date_and_time": 'date and time in the format of "YYYY-MM-DD HH:MM:SS" (e.g. "2024-02-12 19:30:00")',
            "meal_nos": 'meal numbers in a list (e.g.: "[1, 4, 7, 2]" if the targeted meals is 1, 2, 4 and 7)',
            "bin": "The banquet identification number",
            "drink_choice": "remarks about drink choices/preference",
            "meal_choice": "remarks about meal choices/preference",
            "remarks": "other remarks",
            "criteria": "one or more of the 3 defined criteria (e.g. enter '[nameContains=din, dateBefore=2024-12-2 19:30:30, available]' to use all criteria, or press enter to skip)"
        })