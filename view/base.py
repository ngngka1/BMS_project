from settings import check_admin_mode
class BaseView:
    __ADMIN_MODE = check_admin_mode()
    __COMMANDS_DESC = {
        "undefined": "To be defined"
    }
    __ADMIN_COMMANDS_DESC = {}
    __TABLE_NAME = "undefined"
    
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