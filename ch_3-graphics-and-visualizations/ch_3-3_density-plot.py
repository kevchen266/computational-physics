from numpy import loadtxt
from pylab import imshow, gray, show, colorbar

heights = loadtxt('../cpresources/stm.txt', float)
imshow(heights, origin='lower')
gray()
colorbar()
show()
