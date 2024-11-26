class BaseView:
    def __init__(self):
        self.results = []
        
    def display(self):
        for row in self.results:
            print(row)