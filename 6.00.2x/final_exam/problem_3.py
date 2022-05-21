import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here 
    threeDraws = 0
    for n in range(numTrials):
        numRed = 4
        numGreen = 4
        red = drawing(numRed,numGreen)
        if red:
            numRed -= 1
        else:
            numGreen -= 1
        secondDraw = drawing(numRed,numGreen)
        if secondDraw == red:
            if secondDraw:
                numRed -= 1
            else:
                numGreen -= 1
            
            thirdDraw = drawing(numRed, numGreen)
            if thirdDraw == red:
                threeDraws += 1
    return threeDraws/numTrials


def drawing(red, green):
    if random.random()>(red/(green+red)):
        return False
    else:
        return True

drawing_without_replacement_sim(3)