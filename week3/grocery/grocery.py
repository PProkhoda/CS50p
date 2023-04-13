unsorted_dict = {}

while True:
    try:
        item = input().upper()
        if item in unsorted_dict:
            unsorted_dict[item] += 1
        else:
            unsorted_dict[item] = 1
    except EOFError:
        sorted_dict = dict(sorted(unsorted_dict.items()))
        for d in sorted_dict:
            print(f"{sorted_dict[d]} {d}")
        break
    
    
