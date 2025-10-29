'''Main program'''
import time
from functions import clean_terminal

def main_menu():
    print("Welcome to the show!")
    time.sleep(3)
    clean_terminal()
    print("===Dice Throwdown===")
    menu_choice = input(
            "1.\n Start game\n"
            "2. Add player\n" 
            "3. Show player(s)\n" 
            "4. Add balance\n"
            "5. Show balance\n" 
            "6. Exit program\n")
    match menu_choice:
        case '1':
            pass
        case '2':
            pass
        case '3':
            pass
        case '4':
            pass
        case '5':
            pass
        case '6':
            pass
        
def main():
    '''Run program'''
    main_menu()

if __name__ == "__main__":
    main()              