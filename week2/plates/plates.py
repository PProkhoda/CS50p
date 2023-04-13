def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s.isalnum():
        return False
    elif len(s) < 2 or len(s) > 6:
        return False
    elif s[0].isdigit() or s[1].isdigit():
        return False
    else:
        for i in range(len(s)):
            if i > 2 and s[i].isalpha() and s[i - 1].isdigit():
                return False
            elif i > 1 and s[i] == "0" and s[i - 1].isalpha():
                return False
        return True


main()