import sys
from pyfiglet import Figlet

figlet = Figlet()

try:
    if len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if figlet.getFonts().count(sys.argv[2]) == 1:
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid Usage")
    elif len(sys.argv) > 1:
        sys.exit("Invalid Usage")
except IndexError:
    sys.exit("Missing arguments")

text = input("Input: ")
print("Output: " + figlet.renderText(text))
