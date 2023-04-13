tweet = input("Input: ")
print("Output: ", end = "")

for t in tweet:
    if t.lower() == "a" or t.lower() == "e" or t.lower() == "i" or t.lower() == "o" or t.lower() == "u":
        t = ""
    print(t, end = "")
print("")