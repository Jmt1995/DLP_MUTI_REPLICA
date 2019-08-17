import random
from disk import Disk
from data import Data
from replica import Replica
from nodeheapbig import *
from LP1 import *
import time
# import global_vars as gl
import matplotlib.pyplot as plt
import copy
#init2.py 将贪心算法进行了弱化， LP-rdm为优化，选择了两次
def init_disks(DISK_num, Latency_range):
    disk_id = 0
    disks = list()
    _min = Latency_range.get("min")
    _max = Latency_range.get("max")
    print("  min = "+str(_min)+", max = "+ str(_max))
    aver = (_min + _max) / 2
    sigma = (aver - _min) / 2  # 95% 的面积

    xli = list()
    yli = list()
    while disk_id < DISK_num:
        latency = int(round(random.gauss(aver, sigma)))
        if latency > 0 and latency < DISK_num:
            xli.append(disk_id)
            yli.append(latency)
            # print(latency)
            disk = Disk(disk_id, latency)
            disks.append(disk)
            disk_id = disk_id + 1

    # plt.figure()
    # plt.xticks(fontsize=14)
    # plt.yticks(fontsize=14)
    # plt.xlabel("disk", fontsize=14)
    # plt.ylabel("latency", fontsize=14)
    # plt.step(xli, yli, label="DISK-LATANCY", where="post")
    # plt.show()
    # print(len(disks))
    return disks

def init_datas(DATA_NUM, REP_FAC):
    print("--------------- Init_datas ---------------")
    data_list = list()
    replica_list = list()
    k = 0
    for i in range(0, DATA_NUM):
        data = Data(i)
        for j in range(0, REP_FAC):
            replica = Replica(k, i)
            data.rep_set.append(k)
            replica_list.append(replica)
            k = k + 1
        # print(len(data.rep_set))
        data_list.append(data)
    # print(len(data_list))
    return data_list, replica_list


def deploy_replica(disks, replica_list):
    print("--------------- deploy_replica ---------------")
    for replica in replica_list:

        while True:
            disk_id = random.randint(0, int(len(disks))-1)
            flag = False
            for rep in disks[disk_id].rep_list:
                if replica_list[rep].get_data_id() == replica.data_id:
                    flag = True
                    break
            if flag == False:
                # print("diskid:",disk_id)
                break
        # print(disk_id)

        replica.set_disk_id(disk_id)
        disks[disk_id].rep_list.append(replica.id)



def hadoop_naive(disks, data_list, replica_list):
    for data in data_list:
        disks[replica_list[data.rep_set[0]].disk_id].add_active(data.rep_set[0])

    heapbig = HeapPriorityQueueBig()#大顶堆
    for disk in disks:
        heapbig.add(len(disk.active_list)*disk.read_latency, disk.id)

    print("hadoop_naive max (load , id)  = ", heapbig.max())


    xli = list()
    yli = list()
    sum = 0
    for disk in disks:
        xli.append(disk.id)
        # sum = sum + len(disk.active_list)
        yli.append(len(disk.active_list)*disk.read_latency)

    # print("sum:", sum)
    # print(xli)
    # plt.figure()
    # plt.xticks(fontsize=14)
    # plt.yticks(fontsize=14)
    # plt.xlabel("disk", fontsize=14)
    # plt.ylabel("latency", fontsize=14)
    # plt.step(xli, yli, label="DISK-load", where="post")
    # plt.show()
    return xli, yli, heapbig.max()
def random_naive(disks, data_list, replica_list):
    for data in data_list:
        replica_id = random.randint(0, int(len(data.rep_set))-1)
        disks[replica_list[data.rep_set[replica_id]].disk_id].add_active(data.rep_set[0])

    xli = list()
    yli = list()
    heapbig = HeapPriorityQueueBig()  # 大顶堆
    # sum = 0
    for disk in disks:
        # sum = sum + len(disk.active_list)
        xli.append(disk.id)
        yli.append(len(disk.active_list) * disk.read_latency)
        heapbig.add(len(disk.active_list) * disk.read_latency, disk.id)

    # print("sum:", sum)
    # plt.figure()
    # plt.xticks(fontsize=14)
    # plt.yticks(fontsize=14)
    # plt.xlabel("disk", fontsize=14)
    # plt.ylabel("latency", fontsize=14)
    # plt.step(xli, yli, label="DISK-load", where="post")
    # plt.show()

    print("random max (load , id)  = ", heapbig.max())
    return xli, yli, heapbig.max()

def greedy(disks, data_list, replica_list):

    for data in data_list:
        pre = 100000000
        index = 0
        for i in range(0, len(data.rep_set)):
            if pre > disks[replica_list[data.rep_set[i]].disk_id].read_latency:
                pre = disks[replica_list[data.rep_set[i]].disk_id].read_latency
                # index = i
                replica_id = i
        disks[replica_list[data.rep_set[replica_id]].disk_id].add_active(data.rep_set[0])
    xli = list()
    yli = list()
    sum = 0
    heapbig = HeapPriorityQueueBig()  # 大顶堆
    for disk in disks:
        # sum = sum + len(disk.active_list)
        xli.append(disk.id)
        yli.append(len(disk.active_list) * disk.read_latency)
        heapbig.add(len(disk.active_list) * disk.read_latency, disk.id)
    # plt.figure()
    # plt.xticks(fontsize=14)
    # plt.yticks(fontsize=14)
    # plt.xlabel("disk", fontsize=14)
    # plt.ylabel("latency", fontsize=14)
    # plt.step(xli, yli, label="DISK-load", where="post")
    # plt.show()
    # print("sum:", sum)
    print("greedy max (load , id)  = ", heapbig.max())
    return xli, yli, heapbig.max()

def round1(REP_FAC, ans, tasks, data, disks):
    p = ans["x"]
    q = list()
    for i in range(0, len(data)):
        q.append(random.random())

    results = list()
    start = 0
    end = start + REP_FAC
    j = 0  # task
    while end < len(p):
        pis = p[start:end]
        sum = 0
        i = 0
        for pi in pis:
            sum = sum + pi
            if q[j] <= sum:
                if start + i != 0:
                    d_i = tasks[j].index(start + i)
                    results.append([j, d_i])
                    break
                else:
                    d_i = tasks[j].index(-1)
                    results.append([j, d_i])
                    break

            i = i + 1
        j = j + 1
        start = start + REP_FAC
        end = end + REP_FAC

    for result in results:
        disks[result[1]].add_active(result[0])
    xli = list()
    yli = list()
    sum = 0
    heapbig = HeapPriorityQueueBig()  # 大顶堆
    for disk in disks:
        # sum = sum + len(disk.active_list)
        xli.append(disk.id)
        yli.append(len(disk.active_list) * disk.read_latency)
        heapbig.add(len(disk.active_list) * disk.read_latency, disk.id)
    print("HTS-rdm max (load , id)  = ", heapbig.max())
    return xli, yli, heapbig.max()
def round2(REP_FAC, ans, tasks, data, disks):

    p = ans["x"]
    q = list()
    for i in range(0, len(data)):
        q.append(random.random())

    results = list()
    start = 0
    end = start + REP_FAC
    j = 0 # task
    while end < len(p):
        pis = p[start:end]
        sum = 0
        i = 0
        for pi in pis:
            sum = sum + pi
            if q[j] <= sum:
                if start + i != 0:
                    d_i = tasks[j].index(start + i)
                    results.append([j, d_i])
                    break
                else:
                    d_i = tasks[j].index(-1)
                    results.append([j, d_i])
                    break

            i = i + 1
        j = j + 1
        start = start + REP_FAC
        end = end + REP_FAC

    for result in results:
        disks[result[1]].add_active(result[0])
    xli = list()
    yli = list()
    sum = 0
    heapbig = HeapPriorityQueueBig()  # 大顶堆
    for disk in disks:
        # sum = sum + len(disk.active_list)
        xli.append(disk.id)
        yli.append(len(disk.active_list) * disk.read_latency)
        heapbig.add(len(disk.active_list) * disk.read_latency, disk.id)
    print("HTS-rdm max (load , id)  = ", heapbig.max())
    return xli, yli, heapbig.max()

def DLP_random(disks, data_list, replica_list, REP_FAC):
    T = list()
    for di in disks:
        T.append(di.read_latency)
    #data 也就是task数量
    data = list()
    for dat in data_list:
        data_disk = list()
        for i in range(0, len(dat.rep_set)):
            data_disk.append(replica_list[dat.rep_set[i]].disk_id)
        data_disk.sort()
        data.append(data_disk)



    ans, tasks = LP_solver(T, data, REP_FAC)

    end = time.clock()

    disks1 = copy.deepcopy(disks)
    disks2 = copy.deepcopy(disks)
    xli1, yli1, max1 = round1(REP_FAC, ans, tasks, data, disks1)
    xli2, yli2, max2 = round2(REP_FAC, ans, tasks, data, disks2)

    if max1[0] > max2[0]:
        return xli2, yli2, max2
    else:
        return  xli1, yli1, max1

    # return xli, yli, heapbig.max()
