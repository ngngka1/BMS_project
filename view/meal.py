from view.base import BaseView
class MealView(BaseView):
    def __init__(self):
        super().__init__()
        self.set_table_name("Meal")
        self.set_commands_description({
            "Meal help": "Show this help message",
            "Meal list": "list avaiable meals",
        })
        self.set_admin_commands_description({
            "Meal create <type> <dish_name> <price> <special_cuisine>": "create a Meal record",
            "Meal update <type> <dish_name> <price> <special_cuisine>": "update a Meal record"
        })
        self.add_argument_prompt({
            "type": "can only be fish, chicken, beef or vegetarian"
        })