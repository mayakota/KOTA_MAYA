word1 = input("Please enter the first word: ")
word2 = input("Please enter the second word: ")
word3 = input("Please enter the third word: ")

def makeCenter(word):
    if (len(word) >= 20):
        return word
    else:
        print(word)
        return makeCenter(" ", word, " ")
    
        
    
