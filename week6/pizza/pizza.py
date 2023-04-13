from tabulate import tabulate 
from csv import DictReader
import sys

if len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    name, extention = sys.argv[1].strip().split(".")
    if extention != "csv":
        sys.exit("Not a CSV file")
    else:
        try:
            table = []
            with open(sys.argv[1]) as file:
                reader = DictReader(file)
                print(tabulate(reader, headers="keys", tablefmt="grid"))
                    
        except FileNotFoundError:
            sys.exit("File does not exist")
