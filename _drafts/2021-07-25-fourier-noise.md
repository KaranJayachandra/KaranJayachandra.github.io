---
layout: post
title:  "Fourier Transform of White Noise"
date:   2022-07-25 15:39:00 +0200
categories: signalprocessing
---

SOURCES: [DSP Stack Exchange](https://dsp.stackexchange.com/questions/8418/what-is-the-phase-and-magnitude-response-of-white-noise) [My Rank](https://blog.myrank.co.in/sum-of-sines-or-cosines-of-n-angles-in-a-p/)

**The Gist:** If you interested in understanding what happens to a Normal Random Variable after applyting a Fourier Transform to it, read on!

# The Fourier Tranform
The [Fourier Transform](https://www.karanjayachandra.com/signalprocessing/2021/10/02/fourier-transform.html) represents a signal in the frequency domain. There are multiple methods of performing this operation but the most commonly used one is the Discrete Fourier Transform. It adapts the Fourier Transform to time limited signals. Mathematically the operation is described as shown below:

$$\begin{aligned} S[k] &= \sum_{n=0}^{N-1} s[n] e^{\frac{-j2\pi nk}{N}} \\ &= \sum_{n=0}^{N-1} s[n]cos(\frac{2\pi nk}{N}) - j \sum_{n=0}^{N-1} s[n]sin(\frac{2\pi nk}{N})\end{aligned}$$

# The Random Signal
If the samples of $n[m]$ are normal disbributed with mean equal to 0 and variance equal to $\sigma^2$ which is the case for random noise, we would like to understand what happens to the distribution of $N[k]$. Mathematical this means that:

$$\begin{aligned} E[n[m]] &= 0 \\ E[(n[m])^2] &= \sigma^2\end{aligned}$$

# The Mean
If look at the expected value of the complex value $N[k]$ is defined below, which would be the mean of the samples in the frequency domain:

$$\begin{aligned}E[S[k]] &= E[\mathscr{R}(S[k])] + jE[\mathscr{I}(S[k])] \\ &= \sum_{n=0}^{N-1} E[s[n]\cos(\frac{2\pi nk}{N})] - j \sum_{n=0}^{N-1} E[s[n]\sin(\frac{2\pi nk}{N})] \\ &=\sum_{n=0}^{N-1} E[s[n]]\cos(\frac{2\pi nk}{N}) - j \sum_{n=0}^{N-1} E[s[n]]\sin(\frac{2\pi nk}{N}) \\ &=\sum_{n=0}^{N-1} 0 \; \cos(\frac{2\pi nk}{N}) - j \sum_{n=0}^{N-1} 0 \; \sin(\frac{2\pi nk}{N}) \\ &= 0\end{aligned}$$

# The Variance
The variances of the Fourier Tranform would be the expected value of the $N[k]^2$. It is calculated in the same way, therefore, let's concentrate on the real part for now:

$$\begin{aligned}E[\mathscr{R}(N[k])^2)] &= E[\mathscr{R}(N[k]) . \mathscr{R}(N[m])] \\ &= E[\sum_{n=0}^{N-1} s[n]cos(\frac{2\pi nk}{N}) . \sum_{p=0}^{N-1} s[p]cos(\frac{2\pi pk}{N})]\end{aligned}$$

To simplify this, we use some mathematical tricks to collapse the two summations into one. This enables us to move the expected value operation into the summation operation.

$$\begin{aligned}E[\mathscr{R}(N[k])^2)] &= E[\sum_{n=0}^{N-1} s[n]cos(\frac{2\pi nk}{N}) . \sum_{p=0}^{N-1} s[p]cos(\frac{2\pi pk}{N})] \\ &= \sum_{n=0}^{N-1} \sum_{p=0}^{N-1} s[n] s[p] \delta(n - p) cos(\frac{2\pi nk}{N}) cos(\frac{2\pi pk}{N})\end{aligned}$$

Now the summations can be collapsed because the limits are the same and the variables are the same as well. Most importantly, when $n \neq p$ the summation goes to zero.

$$\begin{aligned}E[\mathscr{R}(N[k])^2)] &= E[\sum_{n=0}^{N-1} s[n]^2 {cos}^2(\frac{2\pi nk}{N})] \\ &= \sum_{n=0}^{N-1} E[s[n]^2] {\cos}^2(\frac{2\pi nk}{N}) \\ &= \sum_{n=0}^{N-1} \sigma^2 {\cos}^2(\frac{2\pi nk}{N}) \\ &= \sigma^2 \sum_{n=0}^{N-1} {\cos}^2(\frac{2\pi nk}{N}) \\ &= \sigma^2 \sum_{n=0}^{N-1} \frac{1 + \cos(\frac{4\pi nk}{N})}{2} \\ &= \sigma^2 \left(\sum_{n=0}^{N-1} \frac{1}{2} + \sum_{n=0}^{N-1}\frac{\cos(\frac{4\pi nk}{N})}{2}\right) \\ &= \sigma^2 \left(\frac{N}{2} + \frac{1}{2}\sum_{n=0}^{N-1}cos(\frac{4\pi nk}{N})\right)\end{aligned}$$

Now, we look at the summation of cosine terms that stops us from simplyfing the above equation further. It is a summation of the terms as shown below:

$$\begin{aligned}S &= \sum_{x = 1}^{N} cos(kx) \\ &= 1 + cos(k) + ... + cos((N-1)k)\end{aligned}$$

Multiplying both sides by $\sin (\frac{k}{2})$ is:

$$\begin{aligned}\sin (\frac{k}{2}) S &= \sum_{x = 1}^{N} \sin (\frac{k}{2}) \cos(kx) \\ &= \sin (\frac{k}{2}) + \sin (\frac{k}{2}) \cos(k) + ... + \sin (\frac{k}{2}) \cos((N-1)k)\end{aligned}$$

We apply the identity below to cancel out the summation terms:

$$\sin (a) \cos (b) = \frac{1}{2} \left(\sin (a + b) + \sin (a - b) \right)$$

This simplifies the summation back into the original summation and it ends up as:

$$\begin{aligned}\sin (\frac{k}{2}) S &= \sin (\frac{k}{2}) + \frac{1}{2} (\cancel{\sin (\frac{3k}{2})} - \sin(\frac{k}{2})) + \frac{1}{2} (\cancel{\sin (\frac{5k}{2})} - \cancel{\sin(\frac{3k}{2})}) \\ & \qquad + ... + \frac{1}{2} (\sin ((N - \frac{1}{2})k) - \cancel{\sin((N - \frac{3}{2})k)}) \\ &= \frac{1}{2} \left(\sin ((N - \frac{1}{2})k) + \sin(\frac{k}{2})\right) \\ &= \sin(\frac{Nk}{2}) \cos(\frac{(N-1)k}{2}) \\ &= 0\end{aligned}$$

The above term equates to zero because $\sin$ terms always goes to zero because any integer multiple of $2\pi$ is zero. Seems like a long walk to nothing but it makes our life much easier.

# Probability Distribution of Real and Imaginary Parts

From the above we can say that for the real part of the FFT of Random Noise $n[m]$ with 0 mean and $\sigma^2$ variance, the probability distribution is:

$$\begin{aligned}E[\mathscr{R}(N[k])] &= 0 \\ E[(\mathscr{R}(N[k]))^2] &= \frac{N\sigma^2}{2}\end{aligned}$$

I expect that the same result can be expanded for the imaginary part of the FFT output.