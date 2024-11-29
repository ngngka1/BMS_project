from controller.base import BaseController
from model.attend import AttendModel
from utils.miscellaneous.smart_input import smart_input
from utils.miscellaneous.type_cast import *
from utils.auth.decorators import authenticated_required
from settings import get_session_data
class AttendController(BaseController):
    model_class = AttendModel
    @staticmethod
    @authenticated_required
    def register(*args):
        kwargs = smart_input(*args, **{
            "bin": to_int,
            "drink_choice": to_string_allow_null,
            "meal_choice": to_string_allow_null,
            "remarks": to_string_allow_null,
        })
        kwargs["email_address"] = get_session_data("email_address")
        