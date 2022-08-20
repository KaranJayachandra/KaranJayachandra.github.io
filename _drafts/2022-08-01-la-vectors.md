---
layout: post
title:  "Linear Algebra - Vectors"
date:   2022-08-01 14:58:00 +0200
categories: mathematics
---

# Points in Space

Points in an $N$-dimensional space denoted by $\mathbb{R}^N$ can be represented by $N$ numbers, each called a coordinate, denoted by the variables:

$$(x_1, x_2, x_3, ..., x_n)$$

An $n$ dimentional space $\mathbb{R}^n$ can be represented as product of lower dimensional spaces. The intuition behind this being that a 2D surface is made of infinite 1D lines and so on. Mathematical this means that:

$$\begin{align}\mathbb{R}^N = \mathbb{R}^{N-k} \times \mathbb{R}^k\end{align} \qquad \forall \; k \; \in (1, N-1)$$

Summation in an $N$ dimentional space of two points:

$$A = (a_1, a_2, ..., a_n) \qquad B = (b_1, b_2, ..., b_n)$$

is defined as the summation of the coordinates:

$$A + B = (a_1 + b_1, \; a_2 + b_2, \; ..., \; a_n + b_n)$$

Under the above condition, we can clearly see that:

$$\begin{align}(A + B) + C &= A + (B + C) \\ A + B &= B + A \\ A + 0 &= 0 + A = A \\ A + (-A) &= 0\end{align}$$

Where $0$ refers to the $n$-tuple $(0, 0, ..., 0)$.

The summation of two vectors $A + B$ can be viewed as the diagonal of a **parallelogram** as you can see in the figure below. This is also translated to moving to the point A from the origin and then to point B considering point A as the origin. The negation of a vector $A$ can be seen as the reflection across the origin and the multiplication with a scalar can be seen as an compressing or streching of the vector. Multiplication with a negative number reverses the direction of the vector.

**NOTE: Add a image here**

# Located Vectors

A **Located Vector** is an ordered pair of points written as $\vec{AB}$ with the vector starting at $A$ and ending at $B$.