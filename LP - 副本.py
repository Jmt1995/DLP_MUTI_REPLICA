import  scipy.optimize
from scipy.optimize import linprog
import numpy as np
import gc
import time
def LP_solver(T, data):
    start = time.clock()
    disk = len(T)
    task = len(data)

    print("LP_solver-C-initing")
    c = [0] * disk * task
    # for i in range(0, disk * task):
    #     c.append(0)
    c.append(1)

    print("LP_solver-Aeq-initing")
    Aeq_li = list()
    d = 0
    for i in range(0, task):
        eq = list()
        for j in range(0, task):
            for k in range(0, disk):
                if j == d:
                    eq.append(1)
                else:
                    eq.append(0)
        eq.append(0)
        d = d + 1
        Aeq_li.append(eq)
        gc.collect()

    print("LP_solver-beq-initing")
    beq = [1]*task
    # for i in range(0, task):
    #     beq.append(1)

    print("LP_solver-A-initing")
    A_li = list()
    d = 0
    for i in range(0, disk):
        eq = list()
        for j in range(0, task):
            for k in range(0, disk):
                if k == d:
                    eq.append(T[k])
                else:
                    eq.append(0)
        eq.append(-1)
        d = d + 1
        A_li.append(eq)
        gc.collect()

    print("LP_solver-b-initing")
    b = list()
    for i in range(0, disk):
        b.append(0)

    print("LP_solver-bound-initing")
    bounds1 = list()
    for i in range(0, task):
        for j in range(0, disk):
            if j in data[i]:
                bounds1.append((0, 1))
            else:
                bounds1.append((0, 0))
    bounds1.append((0, None))

    init_end = time.clock()
    print(init_end - start, "seconds init time ")
    print("LP-SOLOING")
    res = linprog(c, A_ub=A_li, b_ub=b, A_eq=Aeq_li, b_eq=beq, bounds=tuple(bounds1),
                  options={"disp": False})

    # print(res)
    return res
