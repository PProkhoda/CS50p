def main():
    x = input()
    convert(x)

def convert(smile):
    smile = smile.replace(":(", "🙁").replace(":)", "🙂")
    print(smile)

# x = input()
# convert(x)                                      
        
main()
