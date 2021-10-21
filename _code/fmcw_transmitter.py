from numpy import tile, linspace, abs, exp, real, angle
from math import pi
from numpy.fft import fft, fftshift
import matplotlib.pyplot as plot
from test_config import RADAR

def chirpGenerator(RADAR, log):
    # Calculate the sampling frequency required
    maxSamplingTime = 1 / (2 * RADAR["Chirp Bandwidth"])
    # Create the time axis for the calculation of the signal
    time = linspace(0, RADAR["Chirp Time"], RADAR["Time Samples in Chirp"])
    # Check if nyguist criteria is met using the given time samples
    if time[1] > maxSamplingTime:
        raise ValueError("For the given chirp the smallest sampling time is " \
            + maxSamplingTime + ". Please configure the Chirp correctly")
    # Print the log if requested
    elif (log):
        print('Nyguist Sample time: {:.2e}'.format(maxSamplingTime))
        print('Radar Bandwidth: {:.2e}'.format(RADAR["Chirp Bandwidth"]))
        print('Current Sample Time: {:.2e}'.format(time[1]))
    # Calculate the instantaneous chirp frequency
    frequency = (time * RADAR["Chirp Bandwidth"]) / (2 * RADAR["Chirp Time"])
    # Creating the complex signal which can then be transformed
    chirpSignal = exp(-1j * 2 * pi * frequency * time)
    return chirpSignal

def test_chirpGenerator():
    # Generate the time axis for plotting the signal
    time = linspace(0, RADAR["Chirp Time"], RADAR["Time Samples in Chirp"])
    # Generating the frequency axis for plotting
    frequency = linspace(- 0.5 / time[1], 0.5 / time[1], time.size)

    # Generate the signal from the chirpGenerator function
    transmitChirp = real(chirpGenerator(RADAR, True))
    
    fig = plot.figure()
    title = "Transmit Chirp"
    fig.suptitle(title, fontsize=20, weight=50)

    timePlot = plot.subplot(211)
    timePlot.plot(time, transmitChirp)
    timePlot.title.set_text('Time Domain')
    timePlot.grid()

    frequencyPlot = plot.subplot(223)
    frequencyPlot.plot(frequency, abs(fftshift(fft(transmitChirp))))
    frequencyPlot.title.set_text('Frequency Domain: Amplitude')
    frequencyPlot.grid()

    anglePlot = plot.subplot(224)
    anglePlot.plot(frequency, (180 / pi) * angle(fftshift(fft(transmitChirp))))
    anglePlot.title.set_text('Frequency Domain: Phase')
    anglePlot.grid()

    plot.show()

def sequenceGenerator(radar, chirpSignal, log):
    # Returns the same input chirp signal repeated multiples times
    if log:
        print('Creating a chirp sequence of length: {}'.format(radar["Number of Chirps"]))
    return tile(chirpGenerator(radar, log), radar["Number of Chirps"])

def test_sequenceGenerator():
    print('Work to be done')

# test_chirpGenerator()