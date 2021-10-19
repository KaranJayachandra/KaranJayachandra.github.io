import numpy
import matplotlib.pyplot as plot

mlaRefernce = {
     "2" : numpy.array([1]),
     "3" : numpy.array([1, 2]),
     "4" : numpy.array([1, 3, 2]),
     "5" : numpy.array([1, 3, 3, 2]),
     "6" : numpy.array([1, 5, 3, 2, 2]),
     "7" : numpy.array([1, 3, 6, 2, 3, 2]),
     "8" : numpy.array([1, 3, 6, 6, 2, 3, 2]),
     "9" : numpy.array([1, 3, 6, 6, 6, 2, 3, 2]),
    "10" : numpy.array([1, 2, 3, 7, 7, 7, 4, 4, 1]),
    "11" : numpy.array([1, 2, 3, 7, 7, 7, 7, 4, 4, 1])
}

def arrayFactor(spacing, angles):
    angleEffect = numpy.cos(angles)
    pattern = numpy.ones(angleEffect.size, dtype=numpy.complex)
    for elementSpacing in spacing:
        elementEffect = numpy.exp(1j*numpy.pi*elementSpacing*angleEffect)
        pattern += elementEffect
    pattern = numpy.abs(pattern)
    pattern /= numpy.max(pattern)
    pattern = 20 * numpy.log(pattern)
    return pattern

elements = 8
angles = numpy.linspace(-numpy.pi, numpy.pi, 1000)
uniformSpacing = numpy.ones(elements - 1)
uniformSpacing = numpy.cumsum(uniformSpacing)
mlaSpacing = numpy.cumsum(mlaRefernce[str(elements)])
uniformElementPattern = arrayFactor(uniformSpacing, angles)
mlaElementPattern = arrayFactor(mlaSpacing, angles)

fig = plot.figure()
fig.suptitle("Minimum Redundancy Linear Array (" + str(elements) + " Elements)", fontsize=20, weight=50)

cartPlot = plot.subplot(121)
cartPlot.plot(angles, uniformElementPattern)
cartPlot.plot(angles, mlaElementPattern)
cartPlot.legend(['Uniform', 'MLA'])
cartPlot.set_xlim([0, max(angles)])
cartPlot.set_ylim([-100, 0])
cartPlot.set_xlabel(r"$\theta$")
cartPlot.set_ylabel("Array Factor")
cartPlot.grid('both')

polarPlot = plot.subplot(122, projection='polar')
polarPlot.plot(angles, uniformElementPattern)
polarPlot.plot(angles, mlaElementPattern)
polarPlot.legend(['Uniform', 'MLA'])
polarPlot.set_thetalim([0, max(angles)])
polarPlot.set_rmax(0)
polarPlot.set_rmin(-100)

plot.show()