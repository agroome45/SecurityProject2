import sys
import os
import re
import operator
from audioop import reverse

LETTERS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

LetterFrequencyOrder = ['E','T','A','O','I','N','S','R','H','D','L','U','C','M','F','Y','W','G','P','B','V','K','X','Q','J','Z']

doubleWords = ['OF','TO','IN','IT','IS','BE','AS','AT','SO','WE','HE','BY','OR','ON','DO','IF','ME','MY','UP','AN','GO','NO','US','AM']

triple = ['THE','AND','FOR','ARE','BUT','NOT','YOU','ALL','ANY','CAN','HAD','HER','WAS','ONE','OUR','OUT','DAY','GET','HAS','HIM','HIS','HOW','MAN','NEW','NOW','OLD',
          'SEE','TWO','WAY','WHO','BOY','DID','ITS','LET','PUT','SAY','SHE','TOO','USE']


class letterData:
    def __init__(self, letterUpper,letterLower, frequency,encryptedLetter,possible, set):
        self.letterUpper = letterUpper
        self.letterLower = letterLower
        self.frequency = frequency
        self.encryptedLetter = encryptedLetter
        self.possible = possible
        self.set = set

def tockenizeText(txt):
    tockens = re.split(' +', txt)
    return tockens

def tockenizeWord(txt):
    tockens = re.split('', txt)
    return tockens

def main(argv):
    
    print("Opening file " ,argv)
    
    fileName = ""
    
    fileName = argv[0]
    
    file = open(fileName, "r")
    
    text = file.read()
    
    splitText = tockenizeText(text)
    
    #print(splitText)
    
    letters = setLetterData()
    
    getFrequencyCount(splitText, letters)
    
    #printFrequency(letters)
    
    orderedLetters = orderByFrequency(letters)
    setEncryptedLetter(orderedLetters)
    printFrequency(orderedLetters)
    getKey(orderedLetters)
    
   
    
    #print(text)
    
def breakEncryption(orderedLetters, splitText):
    print()
    return
        
    
def getNumSet(orderedLetters):
    count = 0
    for i in range(len(orderedLetters)):
        if(orderedLetters[i].set == True):
            count = count + 1
    return count

def getSet(orderedLetters):
    set = []
    for i in range(len(orderedLetters)):
        if(orderedLetters[i].set == True):
            set.append(orderedLetters[i])  
    return set
           
def getKey(orderedLetters):
    key = []
    for i in range(len(LETTERS)):
        for j in range(len(orderedLetters)):
            if(LETTERS[i] == orderedLetters[j].encryptedLetter):
                key.append(orderedLetters[j].letterUpper)
                break 
    myKey = ""
    for k in range(len(key)):
        myKey = myKey + key[k]
    print(myKey)
    return myKey
        
def getFrequencyCount(splitText, letters):
    for i in range(len(splitText)):
        holderWord = splitText[i]
        splitString = tockenizeWord(holderWord)
        for j in range(len(splitString)):
            char = splitString[j]
            for l in range(len(letters)):
                letter = letters[l]
                if(letter.letterUpper == char or letter.letterLower == char):
                    letter.frequency = letter.frequency + 1
                    break 

def setEncryptedLetter(orderedLetters):
   for i in range(len(orderedLetters)):
        if(i == 0):
           orderedLetters[i].encryptedLetter = 'E'
        elif(i == 1):
            orderedLetters[i].encryptedLetter = 'T' 
        else:
            orderedLetters[i].encryptedLetter = '?'
    
def orderByFrequency(letters):
    sortedLetters = sorted(letters, key=operator.attrgetter("frequency")) 
    sortedLetters.reverse()   
    return sortedLetters 
                
 
def printFrequency(letters):
    for i in range(len(letters)):
        print(letters[i].letterUpper, " : ", letters[i].frequency, " ",letters[i].encryptedLetter )

def setLetterData():
    letters = []
    letters.append(letterData('A','a', 0, None,[], False))
    letters.append(letterData('B','b', 0, None,[], False))
    letters.append(letterData('C','c', 0, None,[], False))
    letters.append(letterData('D','d', 0, None,[], False))
    letters.append(letterData('E','e', 0, None,[], False))
    letters.append(letterData('F','f', 0, None,[], False))
    letters.append(letterData('G','g', 0, None,[], False))
    letters.append(letterData('H','h', 0, None,[], False))
    letters.append(letterData('I','i', 0, None,[], False))
    letters.append(letterData('J','j', 0, None,[], False))
    letters.append(letterData('K','k', 0, None,[], False))
    letters.append(letterData('L','l', 0, None,[], False))
    letters.append(letterData('M','m', 0, None,[], False))
    letters.append(letterData('N','n', 0, None,[], False))
    letters.append(letterData('O','o', 0, None,[], False))
    letters.append(letterData('P','p', 0, None,[], False))
    letters.append(letterData('Q','q', 0, None,[], False))
    letters.append(letterData('R','r', 0, None,[], False))
    letters.append(letterData('S','s', 0, None,[], False))
    letters.append(letterData('T','t', 0, None,[], False))
    letters.append(letterData('U','u', 0, None,[], False))
    letters.append(letterData('V','v', 0, None,[], False))
    letters.append(letterData('W','w', 0, None,[], False))
    letters.append(letterData('X','x', 0, None,[], False))
    letters.append(letterData('Y','y', 0, None,[], False))
    letters.append(letterData('Z','z', 0, None,[], False))
    return letters

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
    main(sys.argv[1:])