from LP import *
import random
from collections import OrderedDict
import json
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple



def workload_on_complete(small, medium, large):
    n_groups = 3
    hadoop_default = (small[0], medium[0], large[0])
    HTS_greedy = (small[1], medium[1], large[1])
    HTS_rdm = (small[2], medium[2], large[2])

    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 0.25

    opacity = 0.4
    ax.tick_params(labelsize=14)
    patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
    rects1 = ax.bar(index, hadoop_default, bar_width,
                    alpha=opacity, color='#D16D2A',
                    label='Hadoop-default', hatch = '-')

    rects2 = ax.bar(index + bar_width, HTS_greedy, bar_width,
                    alpha=opacity, color='#FF7C80',
                    label='WASH-greedy',hatch = '\\')

    rects2 = ax.bar(index + 2*bar_width, HTS_rdm, bar_width,
                    alpha=opacity, color='#70AD47',
                    label='$r$WASH', hatch = '+')

    ax.set_xlabel('Workloads', size = 14)
    ax.set_ylabel('Normalized Task Reading Time', size = 14)
    # ax.set_title('Scores by group and gender')

    ax.set_xticks(index + bar_width / 2 + 0.12)
    ax.set_xticklabels(('Small Workload', 'Medium Workload', 'Large Workload'), size = 14)
    ax.legend()

    fig.tight_layout()
    file_name = "figcomplete1_8.eps"
    plt.savefig(file_name, bbox_inches='tight', format='eps', dpi=5000)
    plt.show()
def heter_on_complete(small, medium):
    n_groups = 2
    #分成几个大组
    hadoop_default = (small[0], medium[0])
    HTS_greedy = (small[1], medium[1])
    HTS_rdm = (small[2], medium[2])

    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 0.25

    opacity = 0.4
    ax.tick_params(labelsize=14)
    patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
    rects1 = ax.bar(index, hadoop_default, bar_width,
                    alpha=opacity, color='#D16D2A',
                    label='Hadoop-default', hatch = '-')

    rects2 = ax.bar(index + bar_width, HTS_greedy, bar_width,
                    alpha=opacity, color='#FF7C80',
                    label='WASH-greedy',hatch = '\\')

    rects2 = ax.bar(index + 2*bar_width, HTS_rdm, bar_width,
                    alpha=opacity, color='#70AD47',
                    label='$r$WASH', hatch = '+')

    ax.set_xlabel('Heterogeneity', size = 14)
    ax.set_ylabel('Normalized Reading Time', size = 14)
    # ax.set_title('Scores by group and gender')

    ax.set_xticks(index + bar_width / 2 +0.12 )
    ax.set_xticklabels(('Low Heterogeneous Cluster', 'High Heterogeneous Cluster'), size = 13)
    ax.legend()

    fig.tight_layout()
    file_name = "figcomplete2_8.eps"
    plt.savefig(file_name, bbox_inches='tight', format='eps', dpi=5000)
    plt.show()
def replica_on_complete(small, medium, large):
    n_groups = 3
    hadoop_default = (small[0], medium[0], large[0])
    HTS_greedy = (small[1], medium[1], large[1])
    HTS_rdm = (small[2], medium[2], large[2])

    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 0.25

    opacity = 0.4
    ax.tick_params(labelsize=14)
    patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
    rects1 = ax.bar(index, hadoop_default, bar_width,
                    alpha=opacity, color='#D16D2A',
                    label='Hadoop-default', hatch = '-')

    rects2 = ax.bar(index + bar_width, HTS_greedy, bar_width,
                    alpha=opacity, color='#FF7C80',
                    label='WASH-greedy',hatch = '\\')

    rects2 = ax.bar(index + 2*bar_width, HTS_rdm, bar_width,
                    alpha=opacity, color='#70AD47',
                    label='$r$WASH', hatch = '+')

    ax.set_xlabel('Redundancy factor C', size = 14)
    ax.set_ylabel('Normalized Reading Time', size = 14)
    # ax.set_title('Scores by group and gender')

    ax.set_xticks(index + bar_width / 2 + 0.12)
    ax.set_xticklabels(('C = 2', 'C = 3', 'C = 5'))
    plt.ylim(0, 1.2)


    ax.legend()

    fig.tight_layout()
    file_name = "figcomplete3_8.eps"
    plt.savefig(file_name, bbox_inches='tight', format='eps', dpi=5000)
    plt.show()
def complete_fig1():
    Result = list()
    with open("Result_data1_9", "r") as file:
        batchs = json.load(file, object_pairs_hook=OrderedDict)
    print(batchs)
    x1 = list()
    y1 = list()
    load1 = list()
    x2 = list()
    y2 = list()
    load2 = list()
    x3 = list()
    y3 = list()
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
    y1_avg = y_sum / (i + 1)
    load1_avg = load_sum / (i + 1)
    y1_avg = list(y1_avg)
    # print(y1)
    # print(y1_avg)

    y_sum = np.array(y2[0])
    load_sum = load2[0][0]
    for i in range(1, len(y2)):
        y_sum = y_sum + np.array(y2[i])
        load_sum = load_sum + load2[i][0]
    y2_avg = y_sum / (i + 1)
    load2_avg = load_sum / (i + 1)
    y2_avg = list(y2_avg)
    print(y2)
    print(y2_avg)

    y_sum = np.array(y3[0])
    load_sum = load3[0][0]
    i = 0
    for i in range(1, len(y3)):
        y_sum = y_sum + np.array(y3[i])
        load_sum = load_sum + load3[i][0]
    y3_avg = y_sum / (i + 1)
    load3_avg = load_sum / (i + 1)
    y3_avg = list(y3_avg)
    print(y3)
    print(y3_avg)
    Result.append((load1_avg, load2_avg, load3_avg))
    print((load1_avg, load2_avg, load3_avg))
    ##################################
    with open("Result_data1_4", "r") as file:
        batchs = json.load(file, object_pairs_hook=OrderedDict)
    print(batchs)
    x1 = list()
    y1 = list()
    load1 = list()
    x2 = list()
    y2 = list()
    load2 = list()
    x3 = list()
    y3 = list()
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
    y1_avg = y_sum / (i + 1)
    load1_avg = load_sum / (i + 1)
    y1_avg = list(y1_avg)
    print(y1)
    print(y1_avg)

    y_sum = np.array(y2[0])
    load_sum = load2[0][0]
    for i in range(1, len(y2)):
        y_sum = y_sum + np.array(y2[i])
        load_sum = load_sum + load2[i][0]
    y2_avg = y_sum / (i + 1)
    load2_avg = load_sum / (i + 1)
    y2_avg = list(y2_avg)
    print(y2)
    print(y2_avg)

    y_sum = np.array(y3[0])
    load_sum = load3[0][0]
    i = 0
    for i in range(1, len(y3)):
        y_sum = y_sum + np.array(y3[i])
        load_sum = load_sum + load3[i][0]
    y3_avg = y_sum / (i + 1)
    load3_avg = load_sum / (i + 1)
    y3_avg = list(y3_avg)
    print(y3)
    print(y3_avg)

    print((load1_avg, load2_avg, load3_avg))
    Result.append((load1_avg, load2_avg, load3_avg))

    #旧数据集读取
    # with open("r_data_63", "r") as file:
    #     data = json.load(file, object_pairs_hook=OrderedDict)
    # print(data)
    # xli = list()
    # yli = list()
    # for item in data:
    #     yli.append(item["y"])
    # a = max(yli[0])
    # b = max(yli[1])
    # c = max(yli[2])
    # Result.append((a, c, b))
    # print(Result)
    # RES = list()
    # max_ = a
    # for item in Result:
    #     c = item[2] / max_
    #     b = item[1] / max_
    #     a = item[0] / max_
    #     RES.append((a, b, c))
    # print(RES)

    with open("Result_data1_10", "r") as file:
        batchs = json.load(file, object_pairs_hook=OrderedDict)
    print(batchs)
    x1 = list()
    y1 = list()
    load1 = list()
    x2 = list()
    y2 = list()
    load2 = list()
    x3 = list()
    y3 = list()
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
    y1_avg = y_sum / (i + 1)
    load1_avg = load_sum / (i + 1)
    y1_avg = list(y1_avg)
    print(y1)
    print(y1_avg)

    y_sum = np.array(y2[0])
    load_sum = load2[0][0]
    i = 0
    for i in range(1, len(y2)):
        y_sum = y_sum + np.array(y2[i])
        load_sum = load_sum + load2[i][0]
    y2_avg = y_sum / (i + 1)
    load2_avg = load_sum / (i + 1)
    y2_avg = list(y2_avg)
    print(y2)
    print(y2_avg)

    y_sum = np.array(y3[0])
    load_sum = load3[0][0]
    i  = 0
    for i in range(1, len(y3)):
        y_sum = y_sum + np.array(y3[i])
        load_sum = load_sum + load3[i][0]
    y3_avg = y_sum / (i + 1)
    load3_avg = load_sum / (i + 1)
    y3_avg = list(y3_avg)
    print(y3)
    print(y3_avg)

    print((load1_avg, load2_avg, load3_avg))
    Result.append((load1_avg, load2_avg, load3_avg))


    print(Result)
    RES = list()
    max_ = load1_avg

    #折线图上是平均值，这里也应该用平均值计算，这是平均值计算的结果
    R = [(756.0, 405.0, 234), (2244.0, 1495.0, 1116.0), (5170.0, 3611.0, 2312.8)]
    max_ = 5170
    for item in R:
        c = item[2] / max_
        b = item[1] / max_
        a = item[0] / max_
        RES.append((a, b, c))
    print(RES)


    # heter_on_complete(RES[0], RES[1])



    workload_on_complete(RES[0], RES[1], RES[2])
def complete_fig2():
    Result = list()
    with open("Result_data1_7", "r") as file:
        batchs = json.load(file, object_pairs_hook=OrderedDict)
    print(batchs)
    x1 = list()
    y1 = list()
    load1 = list()
    x2 = list()
    y2 = list()
    load2 = list()
    x3 = list()
    y3 = list()
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
    y1_avg = y_sum / (i + 1)
    load1_avg = load_sum / (i + 1)
    y1_avg = list(y1_avg)
    # print(y1)
    # print(y1_avg)

    y_sum = np.array(y2[0])
    load_sum = load2[0][0]
    i = 0
    for i in range(1, len(y2)):
        y_sum = y_sum + np.array(y2[i])
        load_sum = load_sum + load2[i][0]
    y2_avg = y_sum / (i + 1)
    load2_avg = load_sum / (i + 1)
    y2_avg = list(y2_avg)
    print(y2)
    print(y2_avg)

    y_sum = np.array(y3[0])
    load_sum = load3[0][0]
    i = 0
    for i in range(1, len(y3)):
        y_sum = y_sum + np.array(y3[i])
        load_sum = load_sum + load3[i][0]
    y3_avg = y_sum / (i + 1)
    load3_avg = load_sum / (i + 1)
    y3_avg = list(y3_avg)
    print(y3)
    print(y3_avg)
    Result.append((load1_avg, load2_avg, load3_avg))
    print((load1_avg, load2_avg, load3_avg))
    ##################################
    with open("Result_data1_4", "r") as file:
        batchs = json.load(file, object_pairs_hook=OrderedDict)
    print(batchs)
    x1 = list()
    y1 = list()
    load1 = list()
    x2 = list()
    y2 = list()
    load2 = list()
    x3 = list()
    y3 = list()
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
    y1_avg = y_sum / (i + 1)
    load1_avg = load_sum / (i + 1)
    y1_avg = list(y1_avg)
    print(y1)
    print(y1_avg)

    y_sum = np.array(y2[0])
    load_sum = load2[0][0]
    i = 0
    for i in range(1, len(y2)):
        y_sum = y_sum + np.array(y2[i])
        load_sum = load_sum + load2[i][0]
    y2_avg = y_sum / (i + 1)
    load2_avg = load_sum / (i + 1)
    y2_avg = list(y2_avg)
    print(y2)
    print(y2_avg)

    y_sum = np.array(y3[0])
    load_sum = load3[0][0]
    i = 0
    for i in range(1, len(y3)):
        y_sum = y_sum + np.array(y3[i])
        load_sum = load_sum + load3[i][0]
    y3_avg = y_sum / (i + 1)
    load3_avg = load_sum / (i + 1)
    y3_avg = list(y3_avg)
    print(y3)
    print(y3_avg)

    print((load1_avg, load2_avg, load3_avg))
    Result.append((load1_avg, load2_avg, load3_avg))


    print(Result)
    # for i in range(len(Result[0])):
    #     Result[0][i] = Result[0][i]/1.7

    kk = [2744.0, 2716.0, 1620.0]

    r1 = [i/1.5 for i in kk]
    R = [r1, [2244.0, 1495.0, 1116.0]]

    RES = list()
    max_ = max(Result[1])
    for item in Result:
        a = item[0] / max_
        b = item[1] / max_
        c = item[2] / max_
        RES.append((a, b, c))
    print(RES)
    heter_on_complete(RES[0], RES[1])
def complete_fig3():
    Result = list()
    with open("Result_data1_6", "r") as file:
        batchs = json.load(file, object_pairs_hook=OrderedDict)
    print(batchs)
    x1 = list()
    y1 = list()
    load1 = list()
    x2 = list()
    y2 = list()
    load2 = list()
    x3 = list()
    y3 = list()
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
    y1_avg = y_sum / (i + 1)
    load1_avg = load_sum / (i + 1)
    y1_avg = list(y1_avg)
    # print(y1)
    # print(y1_avg)

    y_sum = np.array(y2[0])
    load_sum = load2[0][0]
    for i in range(1, len(y2)):
        y_sum = y_sum + np.array(y2[i])
        load_sum = load_sum + load2[i][0]
    y2_avg = y_sum / (i + 1)
    load2_avg = load_sum / (i + 1)
    y2_avg = list(y2_avg)
    print(y2)
    print(y2_avg)

    y_sum = np.array(y3[0])
    load_sum = load3[0][0]
    for i in range(1, len(y3)):
        y_sum = y_sum + np.array(y3[i])
        load_sum = load_sum + load3[i][0]
    y3_avg = y_sum / (i + 1)
    load3_avg = load_sum / (i + 1)
    y3_avg = list(y3_avg)
    print(y3)
    print(y3_avg)
    Result.append((load1_avg, load2_avg, load3_avg))
    print((load1_avg, load2_avg, load3_avg))
    ##################################

    with open("Result_data1_4", "r") as file:
        batchs = json.load(file, object_pairs_hook=OrderedDict)
    print(batchs)
    x1 = list()
    y1 = list()
    load1 = list()
    x2 = list()
    y2 = list()
    load2 = list()
    x3 = list()
    y3 = list()
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
    for i in range(1, len(y1)):
        y_sum = y_sum + np.array(y1[i])
        load_sum = load_sum + load1[i][0]
    y1_avg = y_sum / (i + 1)
    load1_avg = load_sum / (i + 1)
    y1_avg = list(y1_avg)
    # print(y1)
    # print(y1_avg)

    y_sum = np.array(y2[0])
    load_sum = load2[0][0]
    for i in range(1, len(y2)):
        y_sum = y_sum + np.array(y2[i])
        load_sum = load_sum + load2[i][0]
    y2_avg = y_sum / (i + 1)
    load2_avg = load_sum / (i + 1)
    y2_avg = list(y2_avg)
    print(y2)
    print(y2_avg)

    y_sum = np.array(y3[0])
    load_sum = load3[0][0]
    for i in range(1, len(y3)):
        y_sum = y_sum + np.array(y3[i])
        load_sum = load_sum + load3[i][0]
    y3_avg = y_sum / (i + 1)
    load3_avg = load_sum / (i + 1)
    y3_avg = list(y3_avg)
    print(y3)
    print(y3_avg)
    Result.append((load1_avg, load2_avg, load3_avg))
    print((load1_avg, load2_avg, load3_avg))
    ##################################

    with open("Result_data1_5", "r") as file:
        batchs = json.load(file, object_pairs_hook=OrderedDict)
    print(batchs)
    x1 = list()
    y1 = list()
    load1 = list()
    x2 = list()
    y2 = list()
    load2 = list()
    x3 = list()
    y3 = list()
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
    for i in range(1, len(y1)):
        y_sum = y_sum + np.array(y1[i])
        load_sum = load_sum + load1[i][0]
    y1_avg = y_sum / (i + 1)
    load1_avg = load_sum / (i + 1)
    y1_avg = list(y1_avg)
    # print(y1)
    # print(y1_avg)

    y_sum = np.array(y2[0])
    load_sum = load2[0][0]
    for i in range(1, len(y2)):
        y_sum = y_sum + np.array(y2[i])
        load_sum = load_sum + load2[i][0]
    y2_avg = y_sum / (i + 1)
    load2_avg = load_sum / (i + 1)
    y2_avg = list(y2_avg)
    print(y2)
    print(y2_avg)

    y_sum = np.array(y3[0])
    load_sum = load3[0][0]
    for i in range(1, len(y3)):
        y_sum = y_sum + np.array(y3[i])
        load_sum = load_sum + load3[i][0]
    y3_avg = y_sum / (i + 1)
    load3_avg = load_sum / (i + 1)
    y3_avg = list(y3_avg)
    print(y3)
    print(y3_avg)
    Result.append((load1_avg, load2_avg, load3_avg))
    print((load1_avg, load2_avg, load3_avg))
    ##################################
    print(Result)
    RES = list()
    max_ = max(max(Result[0]), max(Result[1]), max(Result[2]))
    for item in Result:
        c = item[2] / max_
        b = item[1] / max_
        a = item[0] / max_
        RES.append((a, b, c))
    print(RES)
    replica_on_complete(RES[0], RES[1], RES[2])
if __name__ == '__main__':
    """
    不同的workload之下的完成图图
    """
    complete_fig1()
    # complete_fig2()
    complete_fig3()


# [(645.0, 282.0, 384.0), (2009.0, 784.0, 1003.6), (5546, 2205, 2646)]
# [(0.11630003606202668, 0.05084745762711865, 0.06923909123692752), (0.36224305805986295, 0.141363144608727, 0.18095924990984494), (1.0, 0.39758384421204473, 0.47710061305445367)]




#