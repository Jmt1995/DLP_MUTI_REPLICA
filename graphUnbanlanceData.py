from LP import *
import random
from collections import OrderedDict
import json
import numpy as np
import matplotlib.pyplot as plt

def instance_graph():
    # plt.figure()

    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel("Disk ID", fontsize=14)
    plt.ylabel("Task reading time (ms)", fontsize=14)
    plt.plot(x1[0], y1_avg, color="red", label="Hadoop-default")
    # plt.step(xli[1], yli[1], label="random", color="blue")
    plt.plot(x2[0], y2_avg, color="black", label="WASH-greedy", linestyle="-.")
    plt.plot(x3[0], y3_avg, color="green", label="$r$WASH", linestyle="--")
    plt.legend(loc="upper right")

    file_name = "fig_unbanlancedata3_1.eps"
    plt.savefig(file_name, bbox_inches='tight', format='eps', dpi=5000)
    plt.show()

# Result_data1_9
# Result_data1_4
# Result_data1_10

if __name__ == '__main__':
    with open("Result_data1_16", "r") as file:
        batchs = json.load(file, object_pairs_hook=OrderedDict)
    print(batchs)
    x1 = list()
    y1= list()
    load1 = list()
    x2 = list()
    y2 = list()
    load2 = list()
    x3 = list()
    y3= list()
    load3 = list()
    for batch in batchs:

        x1.append(batch["hadoop"]["x"])
        y1.append(batch["hadoop"]["y"])
        load1.append(batch["hadoop"]["maxload"])

        x2.append(batch["HTS-greedy"]["x"])
        y2.append(batch["HTS-greedy"]["y"])
        load2.append(batch["HTS-greedy"]["maxload"])

        x3.append(batch["HTS-rdm"]["x"])
        y3.append(batch["HTS-rdm"]["y"])
        load3.append(batch["HTS-rdm"]["maxload"])

    y_sum = np.array(y1[0])
    load_sum = load1[0][0]
    i = 0
    for i in range(1, len(y1)):
        y_sum = y_sum + np.array(y1[i])
        load_sum = load_sum + load1[i][0]
    y1_avg = y_sum/(i + 1)
    load1_avg = load_sum/(i + 1)
    y1_avg = list(y1_avg)
    print(y1)
    print(y1_avg)

    y_sum = np.array(y2[0])
    load_sum = load2[0][0]
    for i in range(1, len(y2)):
        y_sum = y_sum + np.array(y2[i])
        load_sum = load_sum + load2[i][0]
        print(load2[i][0])
    y2_avg = y_sum/(i + 1)

    load2_avg = load_sum/(i + 1)
    y2_avg = list(y2_avg)
    print(y2)
    print(y2_avg)

    y_sum = np.array(y3[0])
    load_sum = load3[0][0]
    for i in range(1, len(y3)):
        y_sum = y_sum + np.array(y3[i])
        load_sum = load_sum + load3[i][0]
        print(load3[i][0])
    y3_avg = y_sum/(i + 1)
    load3_avg = load_sum/(i + 1)
    y3_avg = list(y3_avg)
    print( y3)
    print(y3_avg)

    # instance_graph()

    instance_graph()
    print(load1_avg, load2_avg, load3_avg)



#