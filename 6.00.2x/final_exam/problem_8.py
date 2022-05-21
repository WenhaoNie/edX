import random
from numpy import polyval
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    if CURRENTRABBITPOP < 10:
        return
    pRepro = 1 - CURRENTRABBITPOP/MAXRABBITPOP
    if random.random() < pRepro:
        CURRENTRABBITPOP += 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    if CURRENTFOXPOP < 10 or CURRENTRABBITPOP < 10:
        return
    foxRepro = 1/3
    foxDie = 0.9
    pEat = CURRENTRABBITPOP/MAXRABBITPOP
    foxIncrease = 0
    for f in range(CURRENTFOXPOP):
        if random.random() < pEat:
            CURRENTRABBITPOP -= 1
            if CURRENTRABBITPOP < 10:
                CURRENTRABBITPOP = 10
            if random.random() < foxRepro:
                foxIncrease += 1
        else:
            if random.random() < foxDie:
                foxIncrease -= 1
    CURRENTFOXPOP += foxIncrease
    if CURRENTFOXPOP < 10:
        CURRENTFOXPOP = 10
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    rPop = []
    fPop = []
    for t in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rPop.append(CURRENTRABBITPOP)
        fPop.append(CURRENTFOXPOP)

    return (rPop, fPop)

MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 300
numSteps = 200

(x, y) = runSimulation(numSteps)
pylab.plot(range(numSteps),x)
pylab.plot(range(numSteps),y)

coeR = pylab.polyfit(range(len(x)),x,2)
pylab.plot(polyval(coeR,range(len(x))))

coeF = pylab.polyfit(range(len(y)),y,2)
pylab.plot(pylab.polyval(coeF,range(len(y))))