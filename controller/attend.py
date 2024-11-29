from controller.base import BaseController
from model.attend import AttendModel
from utils.miscellaneous.type_cast import *
from utils.auth.decorators import authenticated_required
class AttendController(BaseController):
    model_class = AttendModel
    @staticmethod
    @authenticated_required
    def create(**kwargs):
        AttendController.model.insert(**kwargs)
        