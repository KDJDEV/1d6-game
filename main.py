
from scipy.signal import convolve
import numpy as np

P1RollList = [0,0,1,1,1,1,1,1] #The list we convolve P1List with get all possible sums (in this case, numbers 2-7, because of the positions in the list that are 1s)
P2RollList = [0,1,1,1,1,1,1] #The list we convolve P2List with get all possible sums (in this case, numbers 1-6, because of the positions in the list that are 1s)
P1List = [1]
P2List = [1]
P1WinProb = 0
P2WinProb = 0
probToGetToThisPoint = 1

def makeListsEqualLength(list1, list2):
    lenDiff = len(list1) - len(list2)
    if lenDiff > 0:
        list2.extend([0] * lenDiff)
    elif lenDiff < 0:
        list1.extend([0] * abs(lenDiff))

    return list1, list2

def getPossibleSumsList(currentList, rollList):
    currentList, rollList = makeListsEqualLength(currentList, rollList)
    convolution = np.round(convolve(currentList, rollList)) #I round because all numbers in list should be ints, but fftconvolve approximates
    return convolution

def getLoseList(possibleSumsList):
    filteredList = possibleSumsList[:11]
    return filteredList

def getProbWin(possibleSumsList):
    numWinningRolls = 0
    totalRolls = sum(possibleSumsList)
    for num in possibleSumsList[11:]:
            numWinningRolls += num
    return numWinningRolls / totalRolls

turn = 1

while True:
    possibleSumsList = getPossibleSumsList(P1List, P1RollList)
    turnWinProb = getProbWin(possibleSumsList)
    P1WinProb += probToGetToThisPoint * turnWinProb
    P1List = getLoseList(possibleSumsList)
    probToGetToThisPoint = probToGetToThisPoint * (1 - turnWinProb)
    print(f"After player 1's turn #{turn}:")
    print(f"Probability that they won this turn: {turnWinProb}")
    print(f"Probability that they have actually gotten to this point: {probToGetToThisPoint}\n")

    possibleSumsList = getPossibleSumsList(P2List, P2RollList)
    turnWinProb = getProbWin(possibleSumsList)
    P2WinProb += probToGetToThisPoint * turnWinProb
    P2List = getLoseList(possibleSumsList)
    probToGetToThisPoint = probToGetToThisPoint * (1 - turnWinProb)
    print(f"After player 2's turn #{turn}:")
    print(f"Probability that they won this turn: {turnWinProb}")
    print(f"Probability that they have actually gotten to this point: {probToGetToThisPoint}\n")

    if (turn != 1 and (all(e == 0 for e in P1List) or all(e == 0 for e in P2List))):
        print(f"Final probability of win for P1 ≈ {P1WinProb}")
        print(f"Final probability of win for P2 ≈ {P2WinProb} \n")
        break
    turn += 1