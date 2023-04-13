say = input("Greeting: ")
say = say.strip().lower()

if say.startswith("hello"):
    print("$0")
elif say.startswith("h"):
    print("$20")
else:
    print("$100")