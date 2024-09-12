from matplotlib import pyplot as plt

##plt.plot([1, 2, 3, 4, 5])
##plt.show()

##xs = [1, 2, 3, 4, 5]
##ys = [3, -1, 4, 0, 6]
##
##plt.plot(xs, ys, "g-o")
##plt.show()

##plt.plot([1, 2, 3, 4, 5], "g-o")
##plt.plot([1, 2, 4, 8, 16], "b-^")
##plt.show()

import numpy as np

##array = np.arange(1, 6)

##array = np.array([x**2 for x in range(1024)])
##plt.plot(array)
##plt.show()

ys = np.arange(1, 21).reshape(5,4)
xs = [x for x in range(1, 5)]
plt.plot(xs, ys.transpose())
plt.show()



