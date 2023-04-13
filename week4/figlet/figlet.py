from pyfiglet import Figlet
import sys
from random import choice


figlet = Figlet()
l = figlet.getFonts()


if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in l:
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(input('Input: ')))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    figlet.setFont(font=choice(l))
    print(figlet.renderText(input('Input: ')))
else:
    sys.exit("Invalid usage")
    