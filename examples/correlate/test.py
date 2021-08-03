#!/usr/bin/env python3.8

from alexandria import correlations

a = [1, 1, 1, 0, 0, 1]
b = [1, 1, 1, 0, 0, 1]
print(len(a))
res = correlations.correlate(a,b)
print(res)
