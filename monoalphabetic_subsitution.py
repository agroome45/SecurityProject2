import sys

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    
    fileR = open("myMessage.txt", "r")
    myMessage = fileR.read()
    myKey = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    checkValidKey(myKey)
    translated = encryptMessage(myKey, myMessage)
    file = open("textFile.txt", "w")
    file.write(translated)
    print(translated)
    
    deTranslated = decryptMessage(myKey, translated)
    print(deTranslated)
    
def checkValidKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        sys.exit('This is not a valid monoalphabetic substitution cipher key!')
    

def encryptMessage(key, message):
    translated = ''
    charsA = LETTERS
    charsB = key
    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # symbol is not in LETTERS, just add it
            translated += symbol
    return translated

def decryptMessage(key, message):
    translated = ''
    charsA = LETTERS
    charsB = key
    for symbol in message:
        if symbol.upper() in charsB:
            symIndex = charsB.find(symbol.upper())
            if symbol.isupper():
                translated += charsA[symIndex].upper()
            else:
                translated += charsA[symIndex].lower()
        else:
            # symbol is not in LETTERS, just add it
            translated += symbol
    return translated

if __name__ == "__main__":
    main()
