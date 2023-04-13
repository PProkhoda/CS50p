import inflect

p = inflect.engine()
name_list = []

while True:
    try:
        name = input("Name: ")
        name_list.append(name)
    except EOFError:
        print()
        break

# print use inflect lib
print(f"Adieu, adieu, to {p.join(name_list)}")

# print use "if_else"
# if len(name_list) == 1:
#     print(f"Adieu, adieu, to {name_list[0]}")
# elif len(name_list) == 2:
#     print(f"Adieu, adieu, to {name_list[0]} and {name_list[1]}")
# elif len(name_list) > 2:
#     print("Adieu, adieu, to ", sep = "", end = "")
#     for i in range(len(name_list) - 1):
#         print(f"{name_list[i]}, ", sep = "", end = "")
#     print(f"and {name_list[-1]}")
    


