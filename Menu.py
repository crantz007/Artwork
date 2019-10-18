class Menu:

    def __init__(self):
        self.text_descript = {}
        self.functions = {}

    def add_option(self, key, descript, func):
        self.text_descript[key] = descript
        self.functions[key] = func

    def is_valid(self, choice):

        return choice in self.text_descript

    def get_action(self, choice):
        return self.functions.get(choice)

    def __str__(self):
        texts = [f'{key}: {self.text_descript[key]}' for key in self.text_descript.keys()]
        return '\n'.join(texts)
