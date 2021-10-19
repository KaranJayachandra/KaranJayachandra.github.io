import numpy as numpy
import matplotlib.pyplot as plot

simulationLength = 100000

trainglePoints = numpy.array([[ 0, 10],
                              [ 10, 0],
                              [-10, 0]])

startLocation = numpy.random.uniform(-10, 10, 2)
dataPoints = numpy.zeros(shape=(simulationLength, 2))

currentPoint = startLocation

for index in range(simulationLength):
    dataPoints[index, :] = currentPoint
    random = int(numpy.floor(trainglePoints.shape[0] * numpy.random.uniform()))
    currentPoint = (currentPoint + trainglePoints[random])/2

plot.scatter(dataPoints[:, 0], dataPoints[:, 1])
plot.ylim(-2, 12)
plot.xlim(-12, 12)
plot.show()