import time
import sys
from colorama import init, Fore, Style
import datetime

# Initialize colorama
init(autoreset=True)

def type_message(message, color=Fore.WHITE):
    for char in message:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(0.05)  # Adjust the sleep duration for typing speed
    print(Style.RESET_ALL)

def bangladesh_wishes():
    type_message("Happy Victory Day, Bangladesh!", Fore.GREEN)
    type_message("Wishing you a day filled with pride, joy, and celebration.", Fore.CYAN)
    type_message("On this special day, let's reflect on the historic victory that led to the independence of Bangladesh.", Fore.RED)
    type_message("May the spirit of unity and freedom continue to inspire generations to come.", Fore.MAGENTA)
    type_message("Happy 16th December!", Fore.RED)

def programming_message():
    code = """\
current_date = datetime.date.today()
if (current_date.month, current_date.day) == (12, 16):
    programming_message()
else:
    bangladesh_wishes()
"""
    type_message("\n" + code, Fore.YELLOW)

# Call the function to display the programming message
programming_message()

# Call the function to display the wishes
bangladesh_wishes()

# Print code2 at the end of the program with green color
code2 = """\
|((((((((((()))))))))))|
|((((((((/~~~~\))))))))|
|(((((((        )))))))|
|(((((((        )))))))|
|((((((((\____/))))))))|
|((((((((((()))))))))))|
 ~~~~~~~~~~~~~~~~~~~~~~
  B A N G L A D E S H
"""
type_message("\n" + code2, Fore.GREEN)

# Wait for user input before closing
input("Press Enter to exit...")
