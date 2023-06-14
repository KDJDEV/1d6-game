from sympy import symbols, expand, Rational

x = symbols('x')

rollPolynomial = x**2 + x**3 + x**4 + x**5 + x**6 + x**7 #The polynomial we multiply P1Polynomial or P2Polynomial by to get all possible sums
P1Polynomial = 1
P2Polynomial = 1
P1WinProb = 0
P2WinProb = 0
probToGetToThisPoint = 1

def getPossibleSumsPolynomial(currentPolynomial):
    expanded = expand(currentPolynomial * rollPolynomial)
    return expanded

def getLosePolynomial(possibleSumsPolynomial): #gets the new possible sums polynomial
    terms = possibleSumsPolynomial.as_ordered_terms()
    filteredTerms = [term for term in terms if term.as_poly(x).degree() < 11]
    filteredPolynomial = sum(filteredTerms)
    return filteredPolynomial #returns 0 if there are no remaining terms

def getProbWin(possibleSumsPolynomial): #assumes we made it to this point
    numWinningRolls = 0
    totalRolls = 0

    for term in possibleSumsPolynomial.as_ordered_terms():
        exponent = term.as_expr().as_poly().degree()
        coefficient = term.coeff(x**exponent)
        if (exponent >= 11):
            numWinningRolls += coefficient
        totalRolls += coefficient
        #print(str(coefficient) + "x^" + str(exponent))
    return numWinningRolls / totalRolls

turn = 1

while True:
    possibleSumsPolynomial = getPossibleSumsPolynomial(P1Polynomial)
    turnWinProb = getProbWin(possibleSumsPolynomial)
    P1WinProb += probToGetToThisPoint * turnWinProb
    P1Polynomial = getLosePolynomial(possibleSumsPolynomial)
    probToGetToThisPoint = probToGetToThisPoint * (1 - turnWinProb)
    print(f"After player 1's turn #{turn}:")
    print(f"Probability that they won this turn: {turnWinProb}")
    print(f"Probability that they have actually gotten to this point: {probToGetToThisPoint}\n")

    possibleSumsPolynomial = getPossibleSumsPolynomial(P2Polynomial)
    turnWinProb = getProbWin(possibleSumsPolynomial)
    P2WinProb += probToGetToThisPoint * turnWinProb
    P2Polynomial = getLosePolynomial(possibleSumsPolynomial)
    probToGetToThisPoint = probToGetToThisPoint * (1 - turnWinProb)
    print(f"After player 2's turn #{turn}:")
    print(f"Probability that they won this turn: {turnWinProb}")
    print(f"Probability that they have actually gotten to this point: {probToGetToThisPoint}\n")

    if (P1Polynomial == 0 or P2Polynomial == 0):
        print(f"Final probability of win for P1: {P1WinProb} ≈ {float(P1WinProb)}")
        print(f"Final probability of win for P2: {P2WinProb} ≈ {float(P2WinProb)} \n")

        weightedProb = P1WinProb * Rational(3, 10) + P2WinProb * Rational(7,10)
        print(f"Final probability of winning if you have a 30% chance of going first: {weightedProb} ≈ {float(weightedProb)}")
        break
    turn += 1
