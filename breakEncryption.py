import sys
import os
import re
import operator
import statistics
from statistics import mode
from audioop import reverse
from copy import deepcopy

LETTERS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

LetterFrequencyOrder = ['E','T','A','O','I','N','S','R','H','D','L','U','C','M','F','Y','W','G','P','B','V','K','X','Q','J','Z']

doubleWords = ['OF','TO','IN','IT','IS','BE','AS','AT','SO','WE','HE','BY','OR','ON','DO','IF','ME','MY','UP','AN','GO','NO','US','AM']

triple = ['THE','AND','FOR','ARE','BUT','NOT','YOU','ALL','ANY','CAN','HAD','HER','WAS','ONE','OUR','OUT','DAY','GET','HAS','HIM','HIS','HOW','MAN','NEW','NOW','OLD',
          'SEE','TWO','WAY','WHO','BOY','DID','ITS','LET','PUT','SAY','SHE','TOO','USE']


class letterData:
    def __init__(self, letterUpper,letterLower, frequency,encryptedLetter,lettersBefore, set):
        self.letterUpper = letterUpper
        self.letterLower = letterLower
        self.frequency = frequency
        self.encryptedLetter = encryptedLetter
        self.lettersBefore = lettersBefore
        self.set = set

def tockenizeText(txt):
    tockens = re.split(' +', txt)
    return tockens

def tockenizeWord(txt):
    tockens = re.split('', txt)
    del tockens[0]
    del tockens[-1]
    return tockens

def main(argv):
    
    print("Opening file " ,argv)
    
    fileName = ""
    
    fileName = argv[0]
    
    file = open(fileName, "r")
    
    text = file.read()
    
    splitText = tockenizeText(text)
    
    letters = setLetterData()
    
    getFrequencyCount(splitText, letters)
    
    orderedLetters = orderByFrequency(letters)
    setEncryptedLetter(orderedLetters)
    printFrequency(orderedLetters)

    
    breakText = breakDownText(splitText)

    key = breakEncryption(orderedLetters, breakText)
    
    createFile = open("key.txt","w+")
   
    createFile.write(key)
    
    print("TEST")
    
    createFile.close
    #print(text)
    
def breakEncryption(orderedLetters, breakText):
    single = breakText[0]
    double = breakText[1]
    triple = breakText[2]
    four = breakText[3]
    more = breakText[4]
    
    key = getKey(orderedLetters)


    #Find THE to get 'H' and 'T' .......................................................
    
    findThe = deepcopy(triple)
    
    while(len(findThe) != 0):
        check = mode(findThe)
        checkCopy = check[:]
        de_check = decryptMessage(key, checkCopy)
        simple_de_Check = simple_decryptMessage(key, checkCopy)
        checkTokens = tockenizeWord(simple_de_Check)
        checkIndexTokens = tockenizeWord(de_check)
        #print(checkTokens)
        if(checkTokens[-1] == 'e'):
            t = checkIndexTokens[0]
            t_index = checkIndex(orderedLetters, t.upper())
            orderedLetters[t_index].encryptedLetter = 'T'
            h = checkIndexTokens[1]
            h_index = checkIndex(orderedLetters, h.upper())
            orderedLetters[h_index].encryptedLetter = 'H'
            removeElement(triple, check)
            break
        else:
            removeElement(findThe, check)
     
    printFrequency(orderedLetters)  
    key = getKey(orderedLetters)
    
    #Find THAT to get 'a'.................................................................
    
    findThat = deepcopy(four)
    
    while(len(findThat) != 0):
        check = mode(findThat)
        checkCopy = check[:]
        de_check = decryptMessage(key, checkCopy)
        simple_de_Check = simple_decryptMessage(key, checkCopy)
        checkTokens = tockenizeWord(simple_de_Check)
        checkIndexTokens = tockenizeWord(de_check)
        if(checkTokens[0] == 't' or checkTokens[0] == 'T'):
            if(checkTokens[1] == 'h' and checkTokens[-1] == 't'):
                a = checkIndexTokens[2]
                a_index = checkIndex(orderedLetters, a.upper())
                orderedLetters[a_index].encryptedLetter = 'A'
                removeElement(four, check)
                break
            else:
                removeElement(findThat, check)
        else: 
            removeElement(findThat, check)
    
    printFrequency(orderedLetters)  
    key = getKey(orderedLetters)
    
    #Find ARE to get 'r' ..................................................................
    
    findAre = deepcopy(triple)
    
    while(len(findAre) != 0):
        check = mode(findAre)
        checkCopy = check[:]
        de_check = decryptMessage(key, checkCopy)
        simple_de_Check = simple_decryptMessage(key, checkCopy)
        checkTokens = tockenizeWord(simple_de_Check)
        checkIndexTokens = tockenizeWord(de_check)
        if(checkTokens[0] == 'a' or checkTokens[0] == 'A'):
            if(checkTokens[2] == 'e'):
                r = checkIndexTokens[1]
                r_index = checkIndex(orderedLetters, r.upper())
                orderedLetters[r_index].encryptedLetter = 'R'
                removeElement(triple, check)
                break
            else:
                removeElement(findAre, check)
        else: 
            removeElement(findAre, check)
    
    printFrequency(orderedLetters)  
    key = getKey(orderedLetters)
    
    #Find and to get 'n' and 'd'...............................................................
    
    findAnd = deepcopy(triple)
    
    while(len(findAnd) != 0):
        check = mode(findAnd)
        checkCopy = check[:]
        de_check = decryptMessage(key, checkCopy)
        simple_de_Check = simple_decryptMessage(key, checkCopy)
        checkTokens = tockenizeWord(simple_de_Check)
        checkIndexTokens = tockenizeWord(de_check)
        if(checkTokens[0] == 'a' or checkTokens[0] == 'A'):
            if(checkTokens[1] != 'r' and checkTokens[2] != 'e' ):
                n = checkIndexTokens[1]
                n_index = checkIndex(orderedLetters, n.upper())
                orderedLetters[n_index].encryptedLetter = 'N'
                d = checkIndexTokens[2]
                d_index = checkIndex(orderedLetters, d.upper())
                orderedLetters[d_index].encryptedLetter = 'D'
                removeElement(triple, check)
                break
            else:
                removeElement(findAnd, check)
        else: 
            removeElement(findAnd, check)
   
    printFrequency(orderedLetters)  
    key = getKey(orderedLetters)
    
    #Find for to get 'f' and 'o' ............................................................
    
    findFor = deepcopy(triple)
    
    while(len(findFor) != 0):
        check = mode(findFor)
        checkCopy = check[:]
        de_check = decryptMessage(key, checkCopy)
        simple_de_Check = simple_decryptMessage(key, checkCopy)
        checkTokens = tockenizeWord(simple_de_Check)
        checkIndexTokens = tockenizeWord(de_check)
        if(checkTokens[2] == 'r' and checkTokens[1] != 'e'):
            f = checkIndexTokens[0]
            f_index = checkIndex(orderedLetters, f.upper())
            orderedLetters[f_index].encryptedLetter = 'F'
            o = checkIndexTokens[1]
            o_index = checkIndex(orderedLetters, o.upper())
            orderedLetters[o_index].encryptedLetter = 'O'
            removeElement(triple, check)
            break
        else: 
            removeElement(findFor, check)
            
    printFrequency(orderedLetters)  
    key = getKey(orderedLetters)
    
    #Find with to get 'w' and 'i'............................................................
    
    findWith = deepcopy(four)
    
    while(len(findWith) != 0):
        check = mode(findWith)
        checkCopy = check[:]
        de_check = decryptMessage(key, checkCopy)
        simple_de_Check = simple_decryptMessage(key, checkCopy)
        checkTokens = tockenizeWord(simple_de_Check)
        checkIndexTokens = tockenizeWord(de_check)
        if(checkTokens[2] == 't' and checkTokens[3] == 'h'):
            w = checkIndexTokens[0]
            w_index = checkIndex(orderedLetters, w.upper())
            orderedLetters[w_index].encryptedLetter = 'W'
            i = checkIndexTokens[1]
            i_index = checkIndex(orderedLetters, i.upper())
            orderedLetters[i_index].encryptedLetter = 'I'
            removeElement(four, check)
            break
        else: 
            removeElement(findWith, check)
            
    printFrequency(orderedLetters)  
    key = getKey(orderedLetters)
    
    #Fine be and is to get 's' and 'b'......................................................
    
    count = 0
    
    findBeIs = deepcopy(double)
    
    while(len(findBeIs) != 0):
        check = mode(findBeIs)
        checkCopy = check[:]
        de_check = decryptMessage(key, checkCopy)
        simple_de_Check = simple_decryptMessage(key, checkCopy)
        checkIndexTokens = tockenizeWord(de_check)
        checkTokens = tockenizeWord(simple_de_Check)
        if(checkTokens[0] == 'i' or checkTokens[0] == 'I'):
            if(checkTokens[1] != 'n' and checkTokens[1] != 't' and checkTokens[1] != 'f' ):
                s = checkIndexTokens[1]
                s_index = checkIndex(orderedLetters, s.upper())
                orderedLetters[s_index].encryptedLetter = 'S'
                count = count + 1
                removeElement(findBeIs, check)
                removeElement(double, check)
                if(count == 2):
                    break
        if(checkTokens[0] != 'w' and checkTokens[0] != 'W' and checkTokens[0] != 'h' and checkTokens[0] != 'H'):
            if(checkTokens[1] == 'e' ):
                b = checkIndexTokens[0]
                b_index = checkIndex(orderedLetters, b.upper())
                orderedLetters[b_index].encryptedLetter = 'B'
                count = count + 1
                removeElement(findBeIs, check)
                removeElement(double, check)
                if(count == 2):
                    break
            else:
                removeElement(findBeIs, check)
        else: 
            removeElement(findBeIs, check)
            
    printFrequency(orderedLetters)  
    key = getKey(orderedLetters)
    
    #Find can and but to get 'c' and 'u'...............................................
    
    count = 0
    
    findCanBut = deepcopy(triple)
    
    while(len(findCanBut) != 0):
        check = mode(findCanBut)
        checkCopy = check[:]
        checkCopy.lower()
        de_check = decryptMessage(key, checkCopy)
        simple_de_Check = simple_decryptMessage(key, checkCopy)
        checkIndexTokens = tockenizeWord(de_check)
        checkTokens = tockenizeWord(simple_de_Check)
        if(checkTokens[1] == 'a' and checkTokens[2] == 'n'):
            c = checkIndexTokens[0]
            c_index = checkIndex(orderedLetters, c.upper())
            orderedLetters[c_index].encryptedLetter = 'C'
            count = count + 1
            removeElement(findCanBut, check)
            removeElement(triple, check)
            if(count == 2):
                break
        if(checkTokens[0] == 'b' or checkTokens[0] == 'B'):
            if(checkTokens[2] == 't' and checkTokens[1] == '?' ):
                u = checkIndexTokens[1]
                u_index = checkIndex(orderedLetters, u.upper())
                orderedLetters[u_index].encryptedLetter = 'U'
                count = count + 1
                removeElement(findCanBut, check)
                removeElement(triple, check)
                if(count == 2):
                    break
            else:
                removeElement(findCanBut, check)
        else: 
            removeElement(findCanBut, check)
            
    printFrequency(orderedLetters)  
    key = getKey(orderedLetters)
    
    #Find by to get 'y'..................................................................
    
    findBy = deepcopy(double)
    
    while(len(findBy) != 0):
        check = mode(findBy)
        checkCopy = check[:]
        de_check = decryptMessage(key, checkCopy)
        simple_de_Check = simple_decryptMessage(key, checkCopy)
        checkTokens = tockenizeWord(simple_de_Check)
        checkIndexTokens = tockenizeWord(de_check)
        if(checkTokens[0] == 'b' or checkTokens[0] == 'B'):
            if(checkTokens[1] != 'i'):
                y = checkIndexTokens[1]
                y_index = checkIndex(orderedLetters, y.upper())
                orderedLetters[y_index].encryptedLetter = 'Y'
                removeElement(double, check)
                break
            else:
                removeElement(findBy, check)
        else: 
            removeElement(findBy, check)
    
    printFrequency(orderedLetters)  
    key = getKey(orderedLetters)
    
    #Find just , have, from to get 'j' , 'v', and 'm'
    
    count = 0
    
    findJVM = deepcopy(four)
    
    while(len(findJVM) != 0):
        check = mode(findJVM)
        checkCopy = check[:]
        de_check = decryptMessage(key, checkCopy)
        simple_de_Check = simple_decryptMessage(key, checkCopy)
        checkIndexTokens = tockenizeWord(de_check)
        checkTokens = tockenizeWord(simple_de_Check)
        if(checkTokens[0] != 'b' and checkTokens[0] != 'r' and checkTokens[0] != 'd'):
            if(checkTokens[1] == 'u' and checkTokens[2] == 's' and checkTokens[3] == 't'   ):
                j = checkIndexTokens[0]
                j_index = checkIndex(orderedLetters, j.upper())
                orderedLetters[j_index].encryptedLetter = 'J'
                count = count + 1
                removeElement(four, check)
                removeElement(findJVM, check)
                if(count == 3):
                    break
        if(checkTokens[0] == 'h' or checkTokens[0] == 'H'):
            if(checkTokens[1] == 'a' and checkTokens[3] == 'e' ):
                v = checkIndexTokens[2]
                v_index = checkIndex(orderedLetters, v.upper())
                orderedLetters[v_index].encryptedLetter = 'V'
                count = count + 1
                removeElement(four, check)
                removeElement(findJVM, check)
                if(count == 3):
                    break
        if(checkTokens[0] == 'F' or checkTokens[0] == 'f'):
            if(checkTokens[1] == 'r' and checkTokens[2] == 'o' ):
                m = checkIndexTokens[3]
                m_index = checkIndex(orderedLetters, m.upper())
                orderedLetters[m_index].encryptedLetter = 'M'
                count = count + 1
                removeElement(four, check)
                removeElement(findJVM, check)
                if(count == 3):
                    break
            else:
                removeElement(findJVM, check)
        else: 
            removeElement(findJVM, check)
            
    printFrequency(orderedLetters)  
    key = getKey(orderedLetters)
    
    #find words ending in ing to get 'g'.............................................................
    
    findG= deepcopy(more)
    
    while(len(findG) != 0):
        check = mode(findG)
        checkCopy = check[:]
        de_check = decryptMessage(key, checkCopy)
        simple_de_Check = simple_decryptMessage(key, checkCopy)
        checkTokens = tockenizeWord(simple_de_Check)
        checkIndexTokens = tockenizeWord(de_check)
        if(checkTokens[-2] == 'n' and checkTokens[-3] == 'i' and checkTokens[-1] == '?'):
            g = checkIndexTokens[-1]
            g_index = checkIndex(orderedLetters, g.upper())
            orderedLetters[g_index].encryptedLetter = 'G'
            break
        else: 
            removeElement(findG, check)
            
    printFrequency(orderedLetters)  
    key = getKey(orderedLetters)
    
    #find ll to get 'l'....................................................................
    
    findLL= deepcopy(more)
    
    doubleL = getdouble(findLL)
    
    while(len(doubleL) != 0):
        check = mode(doubleL)
        checkCopy = check[:]
        de_check = decryptMessage(key, checkCopy)
        simple_de_Check = simple_decryptMessage(key, checkCopy)
        if(simple_de_Check != 's' and simple_de_Check != 'e' and simple_de_Check != 't' and simple_de_Check != 'f' and simple_de_Check != 'm' and simple_de_Check != 'o'):
            l = de_check
            l_index = checkIndex(orderedLetters, l.upper())
            orderedLetters[l_index].encryptedLetter = 'L'
            break
        else: 
            removeElement(doubleL, check)
            
    printFrequency(orderedLetters)  
    key = getKey(orderedLetters)
    
    #find rest of unsolved letters..................................................
    
    unsolvedLetters = []
    for i in range(len(orderedLetters)):
        if(orderedLetters[i].encryptedLetter == '?'):
            unsolvedLetters.append(orderedLetters[i])
    
            
    beforeLetter(unsolvedLetters, more, key)
    
    #Find Q...........................
    
    for i in range(len(unsolvedLetters)):
        letter = unsolvedLetters[i]
        most = mode(letter.lettersBefore)
        most_de = simple_decryptMessage(key, most)
        if(most_de == 'u' or most_de == 'U'):
            q = letter.letterUpper
            q_index = checkIndex(orderedLetters, q.upper())
            orderedLetters[q_index].encryptedLetter = 'Q'
            break
   
    printFrequency(orderedLetters)  
    key = getKey(orderedLetters) 
    
    unsolvedLetters = []
    for i in range(len(orderedLetters)):
        if(orderedLetters[i].encryptedLetter == '?'):
            unsolvedLetters.append(orderedLetters[i])
            
    notUsed = getLettersNotUsed(orderedLetters)
    
    for i in range(len(unsolvedLetters)):
        unsolvedLetters[i].encryptedLetter = notUsed[i]
        
    printFrequency(orderedLetters)  
    key = getKey(orderedLetters)
    
    return key
    
     
def beforeLetter(letters, words, key):
    for k in range(len(letters)):
        letter = letters[k].letterLower
        for j in range(len(words)):
            holderWord = words[j]
            holderTockens = tockenizeWord(holderWord)                      
            for i in range(len(holderTockens)):
                if(holderTockens[i] == letter):
                    if(i != len(holderTockens) - 1):
                        letters[k].lettersBefore.append(holderTockens[i+1])
               
                
       
def getdouble(words):
    double = []
    for j in range(len(words)):
        holderWord = words[j]
        holderTockens = tockenizeWord(holderWord)                       
        for i in range(len(holderTockens)):
            if(holderTockens.count(holderTockens[i]) > 1):
                if(i+1 >= len(holderTockens)):
                    if(holderTockens[i-1] == holderTockens[i]):
                        double.append(holderTockens[i])
                elif(i-1 < 0):
                    if(holderTockens[i+1] == holderTockens[i]):
                        double.append(holderTockens[i])
                else:
                    if(holderTockens[i+1] == holderTockens[i] or holderTockens[i] == holderTockens[i-1]):
                        double.append(holderTockens[i])
    return double
    
def getLettersNotUsed(letters):
    notUsed = deepcopy(LetterFrequencyOrder)
    
    for i in range(len(LetterFrequencyOrder)):
        for j in range(len(letters)):
            if(LetterFrequencyOrder[i] == letters[j].encryptedLetter):
                notUsed.remove(LetterFrequencyOrder[i])
                break
    return notUsed
        
        
    
    
def removeElement(list, element):
    capElement = element[:]
    capToken = tockenizeWord(capElement)
    capToken[0] = capToken[0].upper()
    cap = "".join(capToken)
    lowerElement = element[:]
    lowerToken = tockenizeWord(lowerElement)
    lowerToken[0] = lowerToken[0].lower()
    lower = "".join(lowerToken)
    while list.count(lower) > 0:
        list.remove(lower)    
    while list.count(cap) > 0:
        list.remove(cap)
         
def checkIndex(orderedLetters, letter):
    for i in range(len(orderedLetters)):
        if(orderedLetters[i].letterUpper == letter):
            return i
    return None
        
            
    
def breakDownText(splitText):
    breakText = []
    single = []
    double = []
    triple = []
    four = []
    more = []
    for i in range(len(splitText)):
        holderWord = splitText[i]
        length = len(holderWord)
        if(length == 1):
            single.append(holderWord)
        elif(length == 2):
            double.append(holderWord)
        elif(length == 3):
            triple.append(holderWord)
        elif(length == 4):
            four.append(holderWord)
        else:
            more.append(holderWord)
    breakText.append(single)
    breakText.append(double)
    breakText.append(triple)
    breakText.append(four)
    breakText.append(more)
    return breakText
           
def getKey(orderedLetters):
    key = []
    for i in range(len(LETTERS)):
        found = 0
        for j in range(len(orderedLetters)):
            if(LETTERS[i] == orderedLetters[j].encryptedLetter):
                key.append(orderedLetters[j].letterUpper)
                found = 1
                break 
        if(found == 0):
            key.append('?')
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
        else:
            orderedLetters[i].encryptedLetter = '?'
        
    
def orderByFrequency(letters):
    sortedLetters = sorted(letters, key=operator.attrgetter("frequency")) 
    sortedLetters.reverse()   
    return sortedLetters 
                
 
def printFrequency(letters):
    print()
    for i in range(len(letters)):
        print(letters[i].letterUpper, " : ", letters[i].frequency, " ",letters[i].encryptedLetter )
    print()

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
                #symbol is not in LETTERS, just add it
                translated += symbol
    return translated

def simple_decryptMessage(key, message):
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
            if symbol.upper() in charsA:
                translated += '?'
            else:
                #symbol is not in LETTERS, just add it
                translated += symbol
    return translated

if __name__ == "__main__":
    main(sys.argv[1:])