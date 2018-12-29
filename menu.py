class Menu(dict):
    def __init__(self, *args):
        for count, item in enumerate(args, 1):
            self.update({count: item})
    
    
    def show(self):
        border = '-'*15 + '\n'
        menu_body = border + 'Enter a number to select a menu item\n'
        for key, value in self.items():
            menu_body += (f'{key}. {value}\n')
        menu_body += border

        while True:
            try:
                choice = int(input(menu_body))
                # These lines are place holders to make the code more testable
                if choice == 0 or choice > len(self):
                    pass
                else:
                    return choice
            except ValueError:
                print('Please choose from the menu items')

    
if __name__ == '__main__':
    e = Menu('farts', 'chestnuts', 'apples', 'oranges', 'happiness')
    print(e.show())
