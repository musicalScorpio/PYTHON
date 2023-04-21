import pylab
import random

#Monte Carlo Simulation

def rollDie():
    return random.choice([1,2,3,4,5,6])

def testRollDie(n=10):
    for n in range(n):
        value = rollDie()
        print(str(value))

testRollDie()

def checkPascal(numTrials =10000):
    hit=0.0
    for i in range(numTrials):
        for j in range (24):
            d1 = rollDie()
            d2 = rollDie()
            if d1==6 and d2 ==6:
                hit +=1
                break;

    print ('Probability of losing is '+ str (1-hit/numTrials))
checkPascal()
# 13 because the total sum can be 6+6 =12 and lowest will be 1+1 =2
# So we are trying to build an array and then incrementing the postions 
def testRoll(numTrials):
    results = [0]*13
    print ('>>>>>>>>>>'+ str(results))
    for t in range(numTrials):
        roll = rollDie() + rollDie()
        results[roll] += 1
        print ('>>>>>>>>>> NOW FILLED '+ str(results))
    probs = pylab.array(results)/float(numTrials)
    pylab.plot(range(2,13), probs[2:13], 'go')
    pylab.title('Results of Rolling a Pair of Dice')
    pylab.xlabel('Sum of Pair')
    pylab.ylabel('Probability')
    #limits = pylab.axis()
    #limits = (1, 13, 0, limits[3])
    #pylab.axis(limits)

#testRoll(1000)
#pylab.show()

#Flip a coin and plot the prob of gettign a head

def flipPlot(minExp, maxExp):
    ratios = []
    diffs = []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.random() < 0.5:
                numHeads += 1
        numTails = numFlips - numHeads
        ratios.append(numHeads/float(numTails))
        diffs.append(abs(numHeads - numTails))
    pylab.title('Difference Between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(#Heads - #Tails')
    pylab.plot(xAxis, diffs)
    pylab.figure()
    pylab.plot(xAxis, ratios)
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Heads/Tails')
    pylab.figure()
    pylab.title('Difference Between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(#Heads - #Tails')
    pylab.plot(xAxis, diffs, 'bo')
    pylab.semilogx()
    pylab.semilogy()
    pylab.figure()
    pylab.plot(xAxis, ratios, 'bo')
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Heads/Tails')
    pylab.semilogx()

flipPlot(4, 20)
pylab.show()

def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return math.sqrt(tot/len(X))

    
