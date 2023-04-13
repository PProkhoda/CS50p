def main():
    tweet = input("Input: ")
    print(shorten(tweet))


def shorten(word):
    new_word = ""
    for t in word:
        if t.lower() == "a" or t.lower() == "e" or t.lower() == "i" or t.lower() == "o" or t.lower() == "u":
            t = ""
        new_word += str(t)
    return new_word
    


if __name__ == "__main__":
    main()