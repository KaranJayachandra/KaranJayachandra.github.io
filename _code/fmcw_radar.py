from numpy import tile, max, linspace, abs, pad, zeros
from numpy.random import uniform
from scipy.signal import chirp, spectrogram
from scipy.constants import c
import matplotlib.pyplot as plot

def chirpGenerator(radar):
    # Create the time axis for the calculation of the signal
    time = linspace(0, radar["Chirp Time"], radar["Time Samples in Chirp"])
    # Create the chirp signal based on the inbuilt function
    # TODO: Change this to an inbuild function
    chirpSignal = chirp(time, 0, max(time), radar["Chirp Bandwidth"])
    return chirpSignal

def sequenceGenerator(radar, chirpSignal):
    # Returns the same input chirp signal repeated multiples times
    return tile(chirpSignal, radar["Number of Chirps"])

class radarTarget():
    # The class is initialized with the range of the target
    # TODO: Add the target velocity as a parameters as well
    def __init__(self, range):
        self.range = range
    # The reflection currently only contains range information
    def reflect(self, radar, chirpSequence):
        # Calculate the delay based on the target distance
        timeDelay = (self.range * 2) / c
        # Find how many zeros need to be padded in the start
        time = linspace(0, radar["Chirp Time"], radar["Time Samples in Chirp"])
        closestIndex = (abs(time - timeDelay)).argmin()
        # Seperating the chirps for individual processing
        chirpBlock = chirpSequence.reshape((radar["Time Samples in Chirp"], \
            radar["Number of Chirps"]))
        # Processing chirp by chirp
        for iSlow in range(radar["Number of Chirps"]):
            chirpSignal = chirpBlock[iSlow, :]
            # Pad the zeros and return the chirp signal back after cutting
            delayChirp = pad(chirpSignal, closestIndex)
            chirpBlock[iSlow, :] = delayChirp[0:chirpSignal.size]
        # Return the sequence back to the receiver
        return chirpBlock.flatten()

def radarChannel(radar, environment, chirpSequence):
    # Creating an empty array where the return sequence is stored
    returnSequence = zeros(chirpSequence.size)
    # Creating the targets based on the class radarTarget
    targets = []
    for iTarget in range(environment["Total Targets"]):
        targetDistance = 100 + 10 * uniform(-1, 1)
        targets.append(radarTarget(targetDistance))
        returnSequence += targets[iTarget].reflect(radar, chirpSequence)
    # Return back the sequence to the Receiver
    return returnSequence

radar = {
    "Chirp Bandwidth" : 1e6,
    "Chirp Time" : 25.6e-6,
    "Time Samples in Chirp" : 256,
    "Number of Chirps" : 256
}

environment = {
    "Total Targets": 2
}

chirpSignal = chirpGenerator(radar)
chirpSequence = sequenceGenerator(radar, chirpSignal)
receiveSequence = radarChannel(radar, environment, chirpSequence)

fig = plot.figure()
title = "Radar Processing Chain"
fig.suptitle(title, fontsize=20, weight=50)

transmitPlot = plot.subplot(121)
transmitPlot.plot(chirpSequence)
transmitPlot.grid('both')

receivePlot = plot.subplot(122)
receivePlot.plot(receiveSequence)
receivePlot.grid('both')

plot.show()