def word_count(string):
    lower = string.lower()
    words = lower.split()
    dict = {}
    for word in words:
        count = words.count(word)
        dict[word] = count
    return dict

string = input("Enter a random sentance... or whatever. ")
print("Word count: {}".format(word_count(string)))
