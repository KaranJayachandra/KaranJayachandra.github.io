from numpy import tile, max, linspace
from scipy.signal import chirp, spectrogram
from scipy.constants import c
import matplotlib.pyplot as plot

chirpBW = 1e6
chirpNO = 256
targetRange = 30


time = linspace(0, 25.6e-6, 256)
chirpSignal = chirp(time, 0, max(time), chirpBW)
chirpSignal = tile(chirpSignal, chirpNO)
plot.plot(chirpSignal)
plot.show()

targetDelay = (2 * targetRange) / c
targetRCS = 0