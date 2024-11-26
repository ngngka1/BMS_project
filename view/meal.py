from view.base import BaseView
class MealView(BaseView):
    __COMMANDS_DESC = {
        "Meal help": "Show this help message",
    }
    __ADMIN_COMMANDS_DESC = {
        "Meal create <type> <dish_name> <price> <special_cuisine>": "create a Meal record",
        "Meal update <type> <dish_name> <price> <special_cuisine>": "update a Meal record"
    }
    __TABLE_NAME = "Meal"