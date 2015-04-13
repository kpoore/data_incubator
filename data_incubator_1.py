import random
import numpy

M = 10000
avgAvg = []
avgStd = []
avgRolls = []
for i in range (100000):
    rolls = []
    dSum = 0
    ctr = 0
    while dSum < M:
        rolls.append(random.randint(1,6))
        dSum = dSum + rolls[ctr]
        ctr+=1

    avgRolls.append(ctr)
    temp = numpy.array(rolls)
    average = numpy.mean(temp)
    std = numpy.std(temp)
    avgAvg.append(average)
    avgStd.append (std)


average = numpy.mean(avgAvg)
std = numpy.mean(avgStd)
meanSum = average - M
stdM = std - M

##rolls
average = numpy.mean(avgRolls)
std = numpy.std(avgRolls)
rollsAvg = average
rollsStd = std
print meanSum
print stdM
print rollsAvg
print rollsStd

