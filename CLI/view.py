"""

                            Cross-platform programming
             Laboratory work 2 "Simple CLI calculator with MVC model"
                             Anton Kosenko IT-ZP01


"""

from model import Model

class View():

    def __init__(self, controller):
        super().__init__()
        self.model = Model()
        self.controller = controller

    def welcome(self):
        print('''
                    Welcome to simple Calculator
                    Please type in the math operation you would like to complete:
                    + for addition
                    - for substraction
                    * for multiplication
                    / for division
                    ''')

    def again(self):
        print('''
        Do you want to calculate again?
        Please type Y or N''')
        self.model.again()

    def main(self):
        self.welcome()
        self.model.calculate()
        self.again()

