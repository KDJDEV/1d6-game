# 1d6 game using convolutions
The logic is the same as the main branch version. This code is just implemented using convolutions instead of polynomial multiplications. The output is therefore also the same as the code in the main branch, except this version doesn't show exact probability fractions.

I didn't know about convolutions when I first wrote this, but was inspired to create a version of this code using them after watching this video:
https://www.youtube.com/watch?v=KuXjwB4LzSA&t=485s&ab_channel=3Blue1Brown

This code will switch to using fftconvolve rather than the direct method if it thinks it will be more efficient (this is due to the scipy convolve function).