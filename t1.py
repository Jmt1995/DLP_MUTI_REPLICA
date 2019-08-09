import matplotlib.pyplot as plt
from math import sin

i = [x for x in xrange(-10, 10, 1)]
j = [x ** 2 for x in i]

plt.plot(i, j, linewidth=2.0, color='r')
# plt.show()
plt.savefig('./plteps.eps', format='eps', dpi=1000)