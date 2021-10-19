---
layout: post
title:  "Sierpiński triangle"
date:   2021-10-26 13:14:00 +0200
categories: python
---
I came across this YouTube [video](https://www.youtube.com/watch?v=kbKtFN71Lfs) where the concept of a [Sierpiński triangle](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle) was explained in layman's terms. I became interested and wanted to test it out myself. I quickly wrote a python script as shown below and lo and behold, I could replicate what was explained in the video as shown in the diagram at the end of this post.

{% highlight python %}
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
{% endhighlight %}

