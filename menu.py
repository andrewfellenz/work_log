import os
import time


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

    
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
            clear_screen()
            try:
                choice = int(input(menu_body))
                # These lines are place holders to make the code more testable
                if choice == 0 or choice > len(self):
                    raise ValueError
                else:
                    return self[choice].lower()
            except ValueError:
                print('Please choose from the menu items.')
                time.sleep(1)

    
if __name__ == '__main__':
    e = Menu('farts', 'chestnuts', 'apples', 'oranges', 'happiness')
    e.show()
