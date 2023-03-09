import random


class Main:
    title = 'Title'
    text = 'Text'

    def __init__(self):
        self.base = {}

    def dispatch(self):
        self.enter_list()
        self.print_console()

    def enter_list(self):
        # input()
        self.base['title 1'] = 'text 1'
        self.base['title 2'] = 'text 2'
        self.base['title 3'] = 'text 3'
        self.base['title 4'] = 'text 4'
        self.base['title 5'] = 'text 5'
        self.base['title 6'] = 'text 6'
        self.base['title 7'] = 'text 7'
        self.base['title 8'] = 'text 8'
        self.base['title 9'] = 'text 9'
        self.base['title 10'] = 'text 10'
        self.base['title 11'] = 'text 11'

    def print_console(self):

        display = random.choice(list(self.base.keys()))
        print(display, self.base[display])
