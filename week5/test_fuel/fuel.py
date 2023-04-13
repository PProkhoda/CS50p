def main():
    # fuel = convert()
    while True:
        f = input("Fraction: ")
        try:
            fuel = convert(f)           
        except ValueError:
            pass
        except  ZeroDivisionError:
            pass
        else:
            break
    print(gauge(fuel))


def convert(fraction):
    x, y = fraction.strip().split("/")

    if int(y) == 0:
        raise ZeroDivisionError
    elif int(x) == False or int(y) == False:
        raise ValueError
    elif int(x) > int(y):
        raise ValueError
    else:
        z = int(int(x)/int(y) * 100)
        # print(f"z-{z}")
        return z


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()