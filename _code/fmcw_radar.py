from numpy import tile, max, linspace, abs, pad, zeros, copy, multiply, roll, exp
from math import floor, pi
from numpy.random import uniform
from numpy.fft import fft
from scipy.signal import chirp, spectrogram
from scipy.constants import c
import matplotlib.pyplot as plot
from scipy.signal.filter_design import normalize
from fmcw_transmitter import chirpGenerator

def sequenceGenerator(radar, chirpSignal):
    # Returns the same input chirp signal repeated multiples times
    return tile(chirpSignal, radar["Number of Chirps"])

class radarTarget():
    # The class is initialized with the range of the target
    # TODO: Add the target velocity as a parameters as well
    def __init__(self, range):
        self.range = range
        self.attenuation = 1 / self.range ** 4
    # The reflection currently only contains range information
    def reflect(self, radar, chirpSequence):
        # Calculate the delay based on the target distance
        timeDelay = (self.range * 2) / c
        # Find how many zeros need to be padded in the start
        time = linspace(0, radar["Chirp Time"], radar["Time Samples in Chirp"])
        closestIndex = (abs(time - timeDelay)).argmin()
        # Seperating the chirps for individual processing
        chirpBlock = copy(chirpSequence).reshape((radar["Time Samples in Chirp"], \
            radar["Number of Chirps"]))
        # Processing chirp by chirp
        for iSlow in range(radar["Number of Chirps"]):
            chirpSignal = chirpBlock[iSlow, :]
            # Pad the zeros and return the chirp signal back after cutting
            delayChirp = pad(chirpSignal, closestIndex)
            chirpBlock[iSlow, :] = delayChirp[0:chirpSignal.size]
        # Return the sequence back to the receiver
        return self.attenuation * chirpBlock.flatten()

def radarChannel(radar, environment, chirpSequence):
    # Creating an empty array where the return sequence is stored
    returnSequence = zeros(chirpSequence.size)
    # Creating the targets based on the class radarTarget
    targets = []
    for iTarget in range(environment["Total Targets"]):
        # targetDistance = 3000 * uniform(0, 1)
        targetDistance = environment["Target " + str(iTarget + 1)]
        print(targetDistance)
        targets.append(radarTarget(targetDistance))
        returnSequence += targets[iTarget].reflect(radar, chirpSequence)
    # Return back the sequence to the Receiver
    return returnSequence

def mixSingal(trasmitSequence, receiveSequence):
    return multiply(trasmitSequence, receiveSequence)

def rangeDopplerMap(radar, mixSequence):
    radarFrame = copy(mixSequence).reshape((radar["Time Samples in Chirp"], \
        radar["Number of Chirps"]))
    rangeDopplerMap = fft(radarFrame, axis=0)
    rangeDopplerMap = fft(rangeDopplerMap, axis=1)
    return roll(rangeDopplerMap, floor(radar["Number of Chirps"] / 2))

# Configuration variables
radar = {
    "Chirp Bandwidth" : 1e6,
    "Chirp Time" : 25.6e-6,
    "Time Samples in Chirp" : 256,
    "Number of Chirps" : 256
}

environment = {
    "Total Targets": 2,
    "Target 1" : 1000,
    "Target 2" : 3000
}

# Main code for the creation
transmitChirp = chirpGenerator(radar, False)
transmitSequence = sequenceGenerator(radar, transmitChirp.real)
receiveSequence = radarChannel(radar, environment, transmitSequence)
mixerOutput = mixSingal(transmitSequence, receiveSequence)
rdMap = rangeDopplerMap(radar, mixerOutput)

# Plotting the results below
fig = plot.figure()
title = "Radar Processing Chain"
fig.suptitle(title, fontsize=20, weight=50)

transmitPlot = plot.subplot(221)
transmitPlot.plot(transmitChirp.real)
transmitPlot.title.set_text('Transmit Chirp')
transmitPlot.grid()

receivePlot = plot.subplot(222)
receivePlot.plot(receiveSequence[0:radar["Time Samples in Chirp"]])
receivePlot.title.set_text('Received Chirp')
receivePlot.grid('both')

mixPlot = plot.subplot(223)
mixPlot.plot(mixerOutput[0:256])
mixPlot.title.set_text('Mixer Output')
mixPlot.grid('both')

rdPlot = plot.subplot(224)
rdPlot.plot(abs(roll(fft(mixerOutput[0:radar["Time Samples in Chirp"]]), 128)))
rdPlot.title.set_text('Range FFT')
rdPlot.grid('both')
# rdPlot.imshow(abs(rdMap), cmap='jet', vmin=0, vmax=1000)

plot.show()