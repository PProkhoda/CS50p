def main():
    fract = inp()
    if fract > 98:
        print("F")
    elif fract < 2:
        print("E")
    else:
        print(f"{fract}%")

def inp():
    while True:
        
        fraction = input("Fraction: ")
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            z = round((x / y) * 100)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if z <= 100:
                return z
    

main()
