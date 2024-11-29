import sqlite3
from utils.exceptions.InadequateArgumentsException import InadequateArgumentsException
class BaseController:
    
    @classmethod
    def rollback(cls):
        for model in cls.__subclasses__():
            vars(model).get("model").db_connection.rollback()
            
    @classmethod
    def commit(cls):
        for model in cls.__subclasses__():
            vars(model).get("model").db_connection.commit()
            
    # @classmethod
    # def schedule_commit(cls)
    
    @classmethod
    def init(cls, db_connection: sqlite3.Connection):
        cls.model = vars(cls).get("model_class")(db_connection)
        view_class = vars(cls).get("view_class")
        cls.view = view_class() if view_class else None
        
    def __init__(self, db_connection: sqlite3.Connection):
        self.__class__.init(db_connection)
        
    @classmethod
    def smart_input(cls, *args, **kwargs) -> dict[str, any]:
        # key = name of the argument
        # value = if not None, refers to the typecast function of that type, None otherwise
        for i, key in enumerate(kwargs.keys()):
            cast_func = kwargs[key]
            if (i >= len(args)):
                key_name = key.replace('_', ' ')
                
                print(f"{key_name}: ")
                arg_prompt = cls.view.get_argument_prompt(key)
                if arg_prompt:
                    print(f"({arg_prompt})")
                arg = input()
                if not arg:
                    try:
                        cast_func(arg)
                    except ValueError:
                        raise InadequateArgumentsException(f"{key_name} can not be null!")
                if cast_func:
                    arg = cast_func(arg)
                kwargs[key] = arg
            else:
                arg = args[i]
                if cast_func:
                    arg = cast_func(arg)
                kwargs[key] = arg
        return kwargs