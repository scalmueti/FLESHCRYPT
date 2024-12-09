from lists import *
from equationPicker import *

def main():
    exitChoice = 0
    while exitChoice != 1:
        equationType = input("Input type of problem:\nAddition\nSubtraction\nMultiplication\nDivision\n")
        equationPicker(equationType)
        exitAttempt = input("Do you want to exit(Y) or do another problem(N)?\n")
        userChoices = {
            **{key: 1 for key in yesList},
            **{key: 0 for key in noList}
        }
        exitChoice = userChoices.get(exitAttempt, None)
        if exitChoice is None:
            print("ERROR: Incorrect user choice")
            return
main()