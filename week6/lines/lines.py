import sys

if len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    name, extention = sys.argv[1].strip().split(".")
    if extention != "py":
        sys.exit("Not a Python file")
    else:
        try:
            with open(sys.argv[1]) as file:
                n = 0
                for row in file:
                    if row.lstrip().startswith("#"):
                        continue
                    elif len(row.strip()) == 0:
                        continue
                    else:
                        n += 1
        except FileNotFoundError:
            sys.exit("File does not exist")
                
print(n) 