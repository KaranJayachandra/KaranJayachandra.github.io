# Importing the required packages
from scipy.fft import fft, ifft
from scipy.signal import square
from matplotlib import pyplot
from numpy import linspace, sort, absolute, pi, copy

# Building the data in original domain

t = linspace(0, 1, 100, endpoint=True)
x = square(2 * pi * 5 * t)

# Calculating the different fourier representations
yFull = fft(x)
yInv = ifft(yFull)
values = sort(yFull)
yTop2 = copy(yFull)
yTop6 = copy(yFull)
yTop10 = copy(yFull)
yTop2[absolute(yTop2) < absolute(values[98])] = 0j
yTop6[absolute(yTop6) < absolute(values[94])] = 0j
yTop10[absolute(yTop10) < absolute(values[90])] = 0j
yInvTop2 = ifft(yTop2)
yInvTop6 = ifft(yTop6)
yInvTop10 = ifft(yTop10)

# Plotting the results
fig, (ax1, ax2, ax3) = pyplot.subplots(3, 1)
fig.suptitle('Fourier Transform')
ax1.plot(x, '.-')
ax1.set_ylabel('Original Domain')
ax2.plot(yFull, '.-')
ax2.set_ylabel('Frequency Domain')
ax3.plot(yInvTop2, '.-')
ax3.plot(yInvTop6, '.-')
ax3.plot(yInvTop10, '.-')
ax3.plot(yInv, '.-')
ax3.legend(['2 Frequencies', '6 Frequencies', '10 Frequencies', '100 Frequencies'])
ax3.set_ylabel('Original Domain')
pyplot.show()