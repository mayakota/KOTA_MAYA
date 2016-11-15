sentence = input("Please enter a sentence: ")

def replace(string):
    if string.count(" ") == 0:
        return string
    else:
        string = string[0 : string.index(" ")] + "_" + string[string.index(" ")+1 : len(string)]
        print(string)

print(sentence)
