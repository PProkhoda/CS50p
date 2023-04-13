def main():
    input_time = input("What time is it? ")
    time = convert(input_time)
    # print(time)
    if input_time.endswith("a.m."):
        if 7 <= time <= 8:
            print("breakfast time")
    elif input_time.endswith("p.m."):
        if 0 <= time <= 1:
            print("lunch time")
        else:
            print("dinner time")
    else:
        if 7 <= time <= 8:
            print("breakfast time")
        elif 12 <= time <= 13:
            print("lunch time")
        else:
            print("dinner time")
     
        
def convert(time):
    time = time.replace("a.m.", "").replace("p.m.", "").strip()
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    new_time = hours + minutes/60
    return new_time


if __name__ == "__main__":
    main()