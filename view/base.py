from settings import check_admin_mode
from tabulate import tabulate

class BaseView:
    @property
    def __ADMIN_MODE(self):
        return check_admin_mode()
    
    def set_commands_description(self, dic: dict):
        for key, val in dic.items():
            self.commands_desc[key] = val
    
    def set_admin_commands_description(self, dic: dict):
        for key, val in dic.items():
            self.admin_commands_desc[key] = val
            
    def set_table_name(self, x: str):
        self.table_name = x
    
    def add_argument_prompt(self, dic: dict):
        for key, val in dic.items():
            if key in self.arguments_prompt:
                print(f"Warning: prompt for argument <{key}> overwritten to: {val}")
            self.arguments_prompt[key] = val
            
    def get_argument_prompt(self, argument_name):
        return self.arguments_prompt.get(argument_name)
        
    def get_table_name(self):
        return self.table_name
    
    def help(self):
        print(f"Commands for manipulating {self.get_table_name()} table:")
        for i, key in enumerate(self.commands_desc.keys()):
            print(f"{i+1}. {key}: {self.commands_desc[key]}")
        if self.__ADMIN_MODE:
            for i, key in enumerate(self.admin_commands_desc.keys()):
                if (i == 0):
                    print("\nadmin commands:")
                print(f"{i+1}. {key}: {self.admin_commands_desc[key]}")
            
        
    def __init__(self):
        self.results = {}
        self.commands_desc = {}
        self.admin_commands_desc = {}
        self.arguments_prompt = {}
        
    def display(self, rows=None):
        if rows:
            self.results = rows
        if not self.results:
            print("No matching results!")
        else:
            formatted_results = []
            for row in self.results:
                formatted_row = {}
                for key, value in dict(row).items():
                    if key not in ["available", "present"]: # ye im brute forcing at this point
                        formatted_row[key] = value
                    else:
                        formatted_row[key] = "Yes" if value else "No"
                formatted_results.append(formatted_row)
            print(tabulate([row for row in formatted_results], headers="keys", tablefmt="grid"))