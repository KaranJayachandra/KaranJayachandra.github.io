---
layout: post
title:  "Fourier Transform of Noise"
date:   2022-07-25 15:39:00 +0200
categories: signalprocessing
---

SOURCES: [DSP Stack Exchange](https://dsp.stackexchange.com/questions/8418/what-is-the-phase-and-magnitude-response-of-white-noise) [My Rank](https://blog.myrank.co.in/sum-of-sines-or-cosines-of-n-angles-in-a-p/)

**The Gist:** If you interested in understanding what happens to a Normal Random Variable after applyting a Fourier Transform to it, read on!

# The Fourier Tranform
The [Fourier Transform](https://www.karanjayachandra.com/signalprocessing/2021/10/02/fourier-transform.html) represents a signal in the frequency domain. There are multiple methods of performing this operation but the most commonly used one is the Discrete Fourier Transform. It adapts the Fourier Transform to time limited signals. Mathematically the operation is described as shown below:

$$\begin{aligned} S[k] &= \sum_{n=0}^{N-1} s[n] e^{\frac{-j2\pi nk}{M}} \\ &= \sum_{n=0}^{N-1} s[n]cos(\frac{2\pi nk}{M}) - j \sum_{n=0}^{N-1} s[n]sin(\frac{2\pi nk}{M})\end{aligned}$$

# The Random Signal
If the samples of $n[m]$ are normal disbributed with mean equal to 0 and variance equal to $\sigma^2$ which is the case for random noise, we would like to understand what happens to the distribution of $N[k]$. Mathematical this means that:

$$\begin{aligned} E[n[m]] &= 0 \\ E[(n[m])^2] &= \sigma^2\end{aligned}$$

# The Mean

If look at the expected value of the $N[k]$, which would be the mean of the samples in the frequency domain:

$$\begin{aligned}E[N[k]] &= E[\sum_{n=0}^{N-1} s[n]cos(\frac{2\pi nk}{M}) - j \sum_{n=0}^{N-1} s[n]sin(\frac{2\pi nk}{M})] \\ &=\sum_{n=0}^{N-1} E[s[n]]cos(\frac{2\pi nk}{M}) - j \sum_{n=0}^{N-1} E[s[n]]sin(\frac{2\pi nk}{M}) \\ &=\sum_{n=0}^{N-1} 0 \; cos(\frac{2\pi nk}{M}) - j \sum_{n=0}^{N-1} 0 \; sin(\frac{2\pi nk}{M}) \\ &= 0\end{aligned}$$

The variances of the Fourier Tranform would be the expected value of the $N[k]^2$. This equates to:

$$\begin{aligned}E[N[k]^2] &= E[N[k] N[m]] \\ &= E[]\end{aligned}$$