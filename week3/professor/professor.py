import random


def main():
    l = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(l)
        y = generate_integer(l)
        false = 0
        while True:
            if false == 3:
                print(f"{x} + {y} = {x + y}")
                false = 0
                break
            try:
                z = int(input(f"{x} + {y} = "))
            except ValueError:
                false += 1
                print("EEE")
            else:
                if x + y == z:
                    score += 1
                    break
                else:
                    false += 1
                    print("EEE")
    print(f"Score: {score}")
            
                


def get_level():
    while True:
        try:
            lev = int(input("Level: "))
            if 0 < lev < 4:
                return lev
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        start = 0
        stop = 10
    else:
        start = 10 ** (level-1)
        stop = 10 ** level
    rand_int = random.randrange(start,stop,1)
    return rand_int


if __name__ == "__main__":
    main()