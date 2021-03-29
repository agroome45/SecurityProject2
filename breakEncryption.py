import sys
import os

import re

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



def tockenize(txt):
    tockens = re.split(' +', txt)
    return tockens

def main(argv):
    
    
    print("Opening file " ,argv)
    
    fileName = ""
    
    fileName = argv[0]
    
    file = open(fileName, "r")
    
    text = file.read()
    
    print(tockenize(text))
    
    
    
    print(text)
    
    







if __name__ == "__main__":
    main(sys.argv[1:])