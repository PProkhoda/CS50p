from datetime import date
import datetime
import sys
import inflect


def main():
    p = inflect.engine()
    i = input("Date of Birth: ")
    if check(i) == False:
        sys.exit("Invalid date")
    delta = transform(i)
    print(p.number_to_words(delta).replace(" and", "").capitalize(), "minutes")


def check(string):
    try:
        year, month, day = string.strip().split("-")     
        if year.isdigit() and len(year) == 4:
            if month.isdigit() and 0 < int(month) < 13:
                if day.isdigit() and 0 < int(day) < 32:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    except:
        return False


def transform(born_date):
    today = datetime.date.today()
    born_date = datetime.datetime.strptime(born_date, '%Y-%m-%d').date()
    delta = today - born_date
    return int(delta.total_seconds() / 60)


if __name__ == "__main__":
    main()