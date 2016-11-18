word = input("Please enter a word: ")
stop = len(word)


def tree(word, start, stop):
    if start <= stop:
        print(0, start)
        start = 1 + start
        return tree(tree(word, start, stop))

print(tree(word, start, stop))
