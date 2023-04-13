list_month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def check_month(x):
    if x > 12:
        return False
    elif x < 1:
        return False
    else:
        return True


def check_day(x):
    if x > 31:
        return False
    elif x < 1:
        return False
    else:
        return True


while True:
    n = input("Date: ").strip()
    try:
        month, day, year = n.split("/")
        day = int(day)
        month = int(month)
        year = int(year)
        if check_month(month) and check_day(day):
            break
    except ValueError:
        pass
    
    
    try:
        month, day, year = n.split(" ")
        year = int(year.strip())
        for i in list_month:
            if month == i:
                month = int(list_month.index(i)) + 1
        if "," in day:
            day = int(day.replace(",", ""))
            if check_day(day):
                break
                
    except ValueError:
        pass


print(f"{year}-{month:02}-{day:02}")
