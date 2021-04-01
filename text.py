def revword (word):
    word2 = word[::-1]
    return word2

def countword ():
    fhand = open('text.txt')
    text = fhand.read()
    text1 = text.lower()
    words = text1.split()
    checkWord = words[0]
    if revword(checkWord)==checkWord:
        counter = 0
    else:
        counter = 1
    for word in words:
        if revword(word)==checkWord:
            counter+=1
    return counter