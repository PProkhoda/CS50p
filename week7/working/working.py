import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    try:
        #                        1   2    3         4           5  6    7        8
        matches = re.search(r"^(\d+)(:)?(\d+)? +(am|pm) +to +(\d+)(:)?(\d+)? +(am|pm)", s, re.IGNORECASE)
        if matches.group(2):
            if 0 <= int(matches.group(3)) < 60:
                if matches.group(4).lower() == "am":
                    if matches.group(1) == "12":
                        a = f"00:{matches.group(3)} to "
                    else:
                        a = f"{int(matches.group(1)):02}:{matches.group(3)} to "
                elif matches.group(4).lower() == "pm":
                    a = f"{int(matches.group(1))+12}:{matches.group(3)} to "
            else:
                raise ValueError 
        else:
            if matches.group(4).lower() == "am":
                if matches.group(1) == "12":
                    a = f"00:00 to "
                else:
                    a = f"{int(matches.group(1)):02}:00 to "
            elif matches.group(4).lower() == "pm":
                if matches.group(1) == "12":
                    a = f"12:00 to "
                else:
                    a = f"{int(matches.group(1))+12}:00 to "
                
        if matches.group(6):
            if 0 <= int(matches.group(7)) < 60:
                if matches.group(8).lower() == "am":
                    if matches.group(5) == "12":
                        b = f"00:{matches.group(7)}"
                    else:
                        b = f"{int(matches.group(5)):02}:{matches.group(7)}"
                elif matches.group(8).lower() == "pm":
                    if matches.group(5) == "12":
                        b = f"12:{matches.group(7)}"
                    else:
                        b = f"{int(matches.group(5))+12}:{matches.group(7)}"
            else:
                raise ValueError 
        else:
            if matches.group(8).lower() == "am":
                if matches.group(5) == "12":
                    b = f"00:00 to "
                else:
                    b = f"{int(matches.group(5)):02}:00"
            elif matches.group(8).lower() == "pm":
                if matches.group(5) == "12":
                    b = f"12:00"
                else:
                    b = f"{int(matches.group(5))+12}:00"
        return (a + b)
    except:
        raise ValueError
    

if __name__ == "__main__":
    main()