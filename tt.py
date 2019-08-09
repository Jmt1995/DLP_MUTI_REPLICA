import  scipy.optimize
from scipy.optimize import linprog
import numpy as np

# a = [1,2,3,3]
# a.append(12)
# a.remove(3)
# a.remove(3)
# print(a)
disk = 4
T = [0.3, 0.1, 0.2, 0.2] #Tj
task = 4
# c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
c = list()
for i in range(0, disk*task):
    c.append(0)
c.append(1)
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
# Aeq = [[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0]]
# beq = [1, 1, 1, 1] #task num
beq = list()
for i in range(0, task):
    beq.append(1)
# A =   [[T[0], 0, 0, 0, T[0], 0, 0, 0, T[0], 0, 0, 0, T[0], 0, 0, 0, -1],
#        [0, T[1], 0, 0, 0, T[1], 0, 0, 0, T[1], 0, 0, 0, T[1], 0, 0, -1],
#        [0, 0, T[2], 0, 0, 0, T[2], 0, 0, 0, T[2], 0, 0, 0, T[2], 0, -1],
#        [0, 0, 0, T[3], 0, 0, 0, T[3], 0, 0, 0, T[3], 0, 0, 0, T[3], -1]]
# b = [0, 0, 0, 0] # disk num
A_li = list()
d = 0
for i in range(0, task):
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

b = list()
for i in range(0, disk):
    b.append(0)

data = [[0, 1], [1, 2], [0, 2], [1, 3]]
bounds = list()
bounds1 = list()
for i in range(0, task):
    for j in range(0, disk):
        if j in data[i]:
            bounds1.append((0,1))
        else:
            bounds1.append((0,0))
bounds1.append((0, None))

# x0_bounds = [0, 1]
# x1_bounds = [0, 1]
# x2_bounds = [0, 0]
# x3_bounds = [0, 0]
#
# x4_bounds = [0, 0]
# x5_bounds = [0, 1]
# x6_bounds = [0, 1]
# x7_bounds = [0, 0]
#
# x8_bounds = [0, 1]
# x9_bounds = [0, 0]
# x10_bounds = [0, 1]
# x11_bounds = [0, 0]
#
# x12_bounds = [0, 0]
# x13_bounds = [0, 1]
# x14_bounds = [0, 0]
# x15_bounds = [0, 1]
# x16_bounds = [0, None]
# bounds.append(tuple(x0_bounds))
# bounds.append(tuple(x1_bounds))
# bounds.append(tuple(x2_bounds))
# bounds.append(tuple(x3_bounds))
# bounds.append(tuple(x4_bounds))
# bounds.append(tuple(x5_bounds))
# bounds.append(tuple(x6_bounds))
# bounds.append(tuple(x7_bounds))
# bounds.append(tuple(x8_bounds))
# bounds.append(tuple(x9_bounds))
# bounds.append(tuple(x10_bounds))
# bounds.append(tuple(x11_bounds))
# bounds.append(tuple(x12_bounds))
# bounds.append(tuple(x13_bounds))
# bounds.append(tuple(x14_bounds))
# bounds.append(tuple(x15_bounds))
# bounds.append(tuple(x16_bounds))

res = linprog(c, A_ub=A_li, b_ub=b, A_eq = Aeq_li, b_eq = beq, bounds=tuple(bounds1),
              options={"disp": False})


print(res)