from equations import *
from lists import *

def equationPicker(input):
    match input:
        case input if input in addList:
            numList = userNumbers()
            addition(numList[0], numList[1])
        case input if input in subList:
            numList = userNumbers()
            subtraction(numList[0], numList[1])
        case input if input in divList:
            numList = userNumbers()
            divide(numList[0], numList[1])
        case input if input in multList:
            numList = userNumbers
            multiply(numList[0], numList[1])
