from csv import DictReader, DictWriter
import sys

if len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
        new_students = []
        students = []
        with open(sys.argv[1]) as file:
            reader = DictReader(file)
            for row in reader:
                students.append({"name": row["name"], "house": row["house"]})
            for student in students:
                last, first = student["name"].strip().split(",")
                new_students.append({"first": first.strip(), "last": last.strip(), "house": student["house"]})
                    
    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")

    filename, extentions = sys.argv[2].strip().split(".")
    if extentions != "csv":
        print("Could not read invalid_file.csv")
    else:
        with open(sys.argv[2], "w") as output_file:
            writer = DictWriter(output_file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            writer.writerows(new_students)
