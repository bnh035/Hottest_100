from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt


def resistorBandToValue(bandList):
    resVal = [0]
    bandDict = {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'grey': 8,
        'white': 9,
        'gold': "+5%",
        'silver': "+10%"
    }
    resVal[0] = (10*bandDict[bandList[0]] + bandDict[bandList[1]]) * 10 ** bandDict[bandList[2]]
    resVal.append(bandDict[bandList[3]])
    resVal.append(bandList[4])
    return resVal


bands = ['brown', 'yellow', 'black', 'gold', 10]
inStock = [
    ['brown', 'black', 'blue', 'gold', 10],
    ['green', 'blue', 'black', 'gold', 10],
    ['orange', 'orange', 'black', 'gold', 10],
    ['yellow', 'violet', 'black', 'gold', 10],
    ['white', 'red', 'black', 'gold', 10],
    ['brown', 'red', 'black', 'gold', 10],
    ['orange', 'white', 'black', 'gold', 10],
    ['red', 'violet', 'black', 'gold', 10],
    ['orange', 'white', 'yellow', 'gold', 10],
    ['green', 'blue', 'yellow', 'gold', 10],
    ['red', 'violet', 'yellow', 'gold', 10],
    ['brown', 'violet', 'yellow', 'gold', 10],
    ['white', 'red', 'yellow', 'gold', 10],
    ['brown', 'white', 'yellow', 'gold', 10],
    ['red', 'violet', 'yellow', 'gold', 10],
    ['green', 'blue', 'yellow', 'gold', 10],
    ['orange', 'white', 'yellow', 'gold', 10]
]
availableResistors = []
for value in inStock:
    availableResistors.append(resistorBandToValue(value))
#resistor = resistorBandToValue(bands)
#pprint(availableResistors)


def freqCalc(R1, R2, C):
    val = 1.44/((R1 + 2 * R2) * C)
    return val


def dutyCalc(R1, R2):
    val = (R1 + R2)/(R1 + 2 * R2)
    return val

Res1, Res2, Cap = 1000, 10, 1500/1000000
xVals = []
yVals = []

for res2 in np.arange(1, 500, 1):
    xVals.append(res2)
    yVals.append(freqCalc(res2, Res2, Cap))
    print(freqCalc(res2, Res2, Cap))
plt.plot(xVals, yVals, label='{r1}, {r2}'.format(r1=Res1, r2=res2))

plt.legend()
plt.show()
