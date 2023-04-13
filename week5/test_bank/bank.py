def main():
    say = input("Greeting: ")
    print(f"${value(say)}")


def value(greeting):
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        sum = 0
        return sum
    elif greeting.startswith("h"):
        sum = 20
        return sum
    else:
        sum = 100
        return sum


if __name__ == "__main__":
    main()