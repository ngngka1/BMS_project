from settings import check_admin_mode
class BaseView:
    __ADMIN_MODE = check_admin_mode()
    __COMMANDS_DESC = {}
    __ADMIN_COMMANDS_DESC = {}
    __TABLE_NAME = "undefined"
    __ARGUMENTS_PROMPT = {}
    
    @classmethod
    def set_commands_description(cls, dic: dict):
        for key, val in dic.items():
            if key in cls.__COMMANDS_DESC:
                print(f"Warning: prompt for command <{key}> overwritten to: {val}")
            cls.__COMMANDS_DESC[key] = val
    
    @classmethod
    def set_admin_commands_description(cls, dic: dict):
        for key, val in dic.items():
            if key in cls.__ADMIN_COMMANDS_DESC:
                print(f"Warning: prompt for admin command <{key}> overwritten to: {val}")
            cls.__ADMIN_COMMANDS_DESC[key] = val
            
    @classmethod
    def set_table_name(cls, x: str):
        cls.__TABLE_NAME = x
    
    @staticmethod
    def add_argument_prompt(dic: dict):
        for key, val in dic.items():
            if key in BaseView.__ARGUMENTS_PROMPT:
                print(f"Warning: prompt for argument <{key}> overwritten to: {val}")
            BaseView.__ARGUMENTS_PROMPT[key] = val
            
    @staticmethod
    def get_argument_prompt(argument_name):
        return BaseView.__ARGUMENTS_PROMPT.get(argument_name)
        
    @classmethod
    def get_table_name(cls):
        return cls.__TABLE_NAME
    
    @classmethod
    def help(cls):
        print(f"Commands for manipulating {cls.get_table_name()} table:")
        for i, key in enumerate(cls.__COMMANDS_DESC.keys()):
            print(f"{i+1}. {key}: {cls.__COMMANDS_DESC[key]}")
        if cls.__ADMIN_MODE:
            for i, key in enumerate(cls.__ADMIN_COMMANDS_DESC.keys()):
                print(f"{i+1}. {key}: {cls.__ADMIN_COMMANDS_DESC[key]}")
            
        
    def __init__(self):
        self.results = []
        
    def help(self):
        print("help for the view")
        
    def display(self):
        for row in self.results:
            print(row)