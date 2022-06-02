"""

                            Cross-platform programming
             Laboratory work 2 "Simple CLI calculator with MVC model"
                             Anton Kosenko IT-ZP01


"""

class Model:

    def __init__(self):
        pass
        self.previous_value = ''
        self.value = ''
        self.operator = ''

    def calculate(self):
        operation = input()

        number_1 = int(input('Enter your first number: '))
        number_2 = int(input('Enter your second number: '))

        # Addition
        if operation == '+':
            print('{} + {} = '.format(number_1, number_2))
            print(number_1 + number_2)
        # Subtraction
        elif operation == '-':
            print('{} - {} = '.format(number_1, number_2))
            print(number_1 - number_2)

        # Multiplication
        elif operation == '*':
            print('{} * {} = '.format(number_1, number_2))
            print(number_1 * number_2)

        # Division
        elif operation == '/':
            print('{} / {} = '.format(number_1, number_2))
            print(number_1 / number_2)

        else:
            print('You have not typed a valid operator, please run the program again.')

    def _evaluate(self):
        return eval(self.previous_value+self.operator+self.value)

    def again(self):
        calc_again = input()
        if calc_again.upper() == 'Y':
            self.calculate()
        else:
            print('See you later.')
