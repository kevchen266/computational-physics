from numpy import loadtxt
from pylab import plot, show, xlabel, ylabel, title

sunspotData = loadtxt('../cpresources/sunspots.txt')
x = sunspotData[0:1001, 0]
y = sunspotData[0:1001, 1]
plot(x, y)
xlabel("months since Jan 1749")
ylabel("number of observed sunspots")
title("Number of sunspots since Jan 1749")
show()