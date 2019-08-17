import  scipy.optimize
from scipy.optimize import linprog
import numpy as np
import gc
import time
def LP_solver(T, data, replica_num):
    start = time.clock()
    disk = len(T)
    task = len(data)

    print("LP_solver-C-initing")
    c = [0] * task * replica_num
    # for i in range(0, disk * task):
    #     c.append(0)
    c.append(1)

    print("LP_solver-Aeq-initing")
    Aeq_li = list()
    d = 0
    for i in range(0, task):
        # eq = list()
        eq = [0] * replica_num * i + [1] * replica_num + [0] * replica_num * (task - i - 1) + [0]

        # print("Aeq:", i, eq)
        Aeq_li.append(eq)
        # gc.collect()

    print("LP_solver-beq-initing")
    beq = [1]*task

    tasks =list()
    index = 0
    for da in data:
        task_li = [0] * disk
        for its in da:
            if index != 0:
                task_li[its] = index
            else:
                task_li[its] = -1
            index = index + 1

        tasks.append(task_li)

    # print(tasks)
    print("LP_solver-A-initing")
    A_li = list()
    d = 0
    for i in range(0, disk):
        eq = [0]*task*replica_num + [-1]

        for ta in tasks:
            if ta[i] != 0 and ta[i] != -1:
                eq[ta[i]] = T[i]
            elif ta[i] == -1:
                eq[0] = T[i]

        A_li.append(eq)
        # print("A:", i, eq)
        # print("A:", i)
        # gc.collect()

    print("LP_solver-b-initing")
    b = list()
    for i in range(0, disk):
        b.append(0)

    print("LP_solver-bound-initing")
    bounds1 = [(0, 1)] * task * replica_num +[(0, None)]

    init_end = time.clock()
    print(init_end - start, "seconds init time ")
    print("LP-SOLOING")
    gc.collect()

    res = linprog(c, A_ub=A_li, b_ub=b, A_eq=Aeq_li, b_eq=beq, bounds=tuple(bounds1))
    end = time.clock()
    print(end - init_end, "seconds LP time ")
    # print(res)
    return res, tasks
# tasks 是二位数组 每一行为一个task的，参数的序号
