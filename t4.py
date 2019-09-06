import random
import matplotlib.pyplot as plt
_min = 10
_max = 500
print("  min = " + str(_min) + ", max = " + str(_max))
aver = (_min + _max) / 2
sigma = (aver - _min) / 2  # 95% 的面积
xli = list()
yli = list()
for i in range(0,50):
    value = int(round(random.gauss(aver, sigma)))
    xli.append(i)
    yli.append(value)
    print(value)


plt.figure()
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel("disk", fontsize=14)
plt.ylabel("latency", fontsize=14)
plt.step(xli, yli, label="DISK-LATANCY", where="post")
plt.show()
# print(len(disks))