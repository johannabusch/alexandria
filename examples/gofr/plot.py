#!/usr/bin/env python3.8

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

r, gofr = np.loadtxt('h_o.dat', unpack=True, usecols=(0,1))
gofrcms = np.loadtxt('cms_cms.dat', unpack=True, usecols=(1))
gofracms = np.loadtxt('h_cms.dat', unpack=True, usecols=(1))

plt.plot(r,gofr, color='firebrick', label="H$\cdots$O")
plt.plot(r,gofrcms, color='royalblue', label="cms$\cdots$cms")
plt.plot(r,gofracms, color='orange', label="H$\cdots$cms")

plt.axes().xaxis.set_minor_locator(MultipleLocator(0.25))
plt.axes().yaxis.set_minor_locator(MultipleLocator(0.25))
plt.axis([1, 6, 0.0, 4.0])
plt.xlabel(' $r$ / \\AA')
plt.ylabel('$g(r)$')
plt.legend(loc=0)
plt.tight_layout()
plt.savefig('gofr.pdf')#png, pdf, ps, eps and svg
plt.clf()
