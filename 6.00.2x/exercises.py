import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    numSuc = 0
    for i in range(numTrials):
        balls = {0:'red',1:'red',2:'red',3:'green',4:'green',5:'green'}
        lastDraw = ''
        sameColor = True
        for j in range(3):
            draw = random.choice(list(balls.keys()))
            if lastDraw == '':
                lastDraw = balls[draw]
            elif balls[draw] != lastDraw:
                sameColor = False
                break
            balls.pop(draw)
        if sameColor:
            numSuc += 1
    return numSuc/numTrials

print(noReplacementSimulation(1000))