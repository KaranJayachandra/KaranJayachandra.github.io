from numpy import array, ones, abs, max, cumsum, log, linspace, pi, cos, exp
import matplotlib.pyplot as plot

mlaRefernce = {
     "2" : array([1]),
     "3" : array([1, 2]),
     "4" : array([1, 3, 2]),
     "5" : array([1, 3, 3, 2]),
     "6" : array([1, 5, 3, 2, 2]),
     "7" : array([1, 3, 6, 2, 3, 2]),
     "8" : array([1, 3, 6, 6, 2, 3, 2]),
     "9" : array([1, 3, 6, 6, 6, 2, 3, 2]),
    "10" : array([1, 2, 3, 7, 7, 7, 4, 4, 1]),
    "11" : array([1, 2, 3, 7, 7, 7, 7, 4, 4, 1])
}

def arrayFactor(spacing, angles):
    angleEffect = cos(angles)
    pattern = ones(angleEffect.size, dtype=complex)
    for elementSpacing in spacing:
        elementEffect = exp(1j*pi*elementSpacing*angleEffect)
        pattern += elementEffect
    pattern = abs(pattern)
    pattern /= max(pattern)
    pattern = 20 * log(pattern)
    return pattern

elements = 8
angles = linspace(-pi, pi, 1000)
uniformSpacing = ones(elements - 1)
uniformSpacing = cumsum(uniformSpacing)
mlaSpacing = cumsum(mlaRefernce[str(elements)])
uniformElementPattern = arrayFactor(uniformSpacing, angles)
mlaElementPattern = arrayFactor(mlaSpacing, angles)

fig = plot.figure()
title = "Minimum Redundancy Linear Array (" + str(elements) + " Elements)"
fig.suptitle(title, fontsize=20, weight=50)

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