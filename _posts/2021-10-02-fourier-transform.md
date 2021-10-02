# Fourier Transform
The Gist: If you would like to solve partial derivates easily or process data in the frequency domain, Fourier Transform is the tool you need. If you interested in reading more, please read more below where I also demonstrate with an example.

# The Basics
The Fourier Transform represents a sequence of numbers (which I will refer to as a signal henceforth) as a summation of sinusoidal waves. It terms of the mathematics, it finds the right combinations of sine waves that need to be added to create the original signal. A sine wave however has two defining properties, the amplitude and the phase. Therefore, the Fourier transform calculates not only the amplitudes of the individual sine waves that make up the signal but also the phase of the waves. This makes the result of the Fourier transform a complex valued result. The Fourier transform can be calculated with the output containing different number of sine waves. For a more accurate description, in most cases, more sine waves are necessary. In the below diagram, this is demonstrated. The original sequence is a square wave shown in the top graph. This seqeunce is approximated using the different number of sine waves shown in the middle graph. As you can see in the graph on the bottom, the more the number of sine waves, the closer it is to the original sequence.

<img src="{{site.url}}/assets/images/fourier_transform.png" alt="Fourier Transform Graph">

You can have a look at the python code used to generate the graph above [here](https://github.com/MrKaranJ/MrKaranJ.github.io/blob/gh-pages/_code/fouriertransform.py).

# The Application
Partial Derivatives are much easier to solve in the frequency domain because of certain properties. This means that instead of solving complex integrals and differentials, we can convert the entire equation to the fourier domain, simplify it and then convert it back the original domain. The fourier transform is the basis for any kind of Frequency Analysis. This can help us observe different phenomenon such as the chemical composition of the stars to which frequency channel to use to make sure our home wifi signal has adequate strength.

Although this was a basic introduction to the Fourier Transform, I will create more articles with the in-depth mathematics in the future. In the mean time you can refer to [this](https://www.pearson.com/us/higher-education/product/Proakis-Digital-Signal-Processing-Principles-Algorithms-and-Applications-RENTAL-EDITION-5th-Edition/9780137348244.html) text book if needed.