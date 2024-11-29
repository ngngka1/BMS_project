import sqlite3
class BaseController:
    
    @classmethod
    def init(cls, db_connection: sqlite3.Connection):
        cls.model = vars(cls).get("model_class")(db_connection)
        view_class = vars(cls).get("view_class")
        cls.view = view_class() if view_class else None
        
    def __init__(self, db_connection: sqlite3.Connection):
        self.__class__.init(db_connection)