from lists import *
from equationPicker import *

def main():
    exitChoice = 0
    while exitChoice != 1:
        equationType = input("Input type of problem:\nAddition\nSubtraction\nMultiplication\nDivision\n")
        equationPicker(equationType)
        exitAttempt = input("Do you want to do another problem or exit (Y/N)\n")
        if exitAttempt in yesList:
            exitChoice = 1
        elif exitAttempt in noList:
            exitChoice = 0
        else:
            print("ERROR: Incorrect user choice")
            return
main()