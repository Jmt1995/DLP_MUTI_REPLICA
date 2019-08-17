from LP import *
import random
from collections import OrderedDict
import json
import matplotlib.pyplot as plt


if __name__ == '__main__':
    with open("r_data_63", "r") as file:
        data = json.load(file, object_pairs_hook=OrderedDict)
    print(data)
    xli = list()
    yli = list()
    for item in data:
        xli.append(item["x"])
        yli.append(item["y"])

        # print(xli, yli)
    print(max(yli[0]), max(yli[1]), max(yli[2]))
    plt.figure()
    # plt.xlim([0, DISK_num-1])
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel("disk", fontsize=14)
    plt.ylabel("load (ms)", fontsize=14)
    plt.plot(xli[0], yli[0],  color="red", label="Hadoop-default")
    # plt.step(x2, y2, label="random", color="blue", where="post")
    plt.plot(xli[2], yli[2], color="black", label="HTS-greedy")
    plt.plot(xli[1], yli[1],  color="green", label="HTS-rdm")

    plt.legend(loc="upper right")

    # foo_fig = plt.gcf()  # 'get current figure'
    # foo_fig.savefig('instance.eps', format='eps', dpi=1000)
    # plt.savefig('./plteps.eps', format='eps', dpi=1000)
    file_name = "fig_instance3_3.eps"
    plt.savefig(file_name, bbox_inches='tight', format='eps', dpi=5000)
    plt.show()

#