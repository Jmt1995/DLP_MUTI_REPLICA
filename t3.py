from LP1 import *
import random
from collections import OrderedDict
import json
REP_FAC = 2
T = [0.3, 0.1, 0.2, 0.2] #Tj
data = [[0, 1], [2, 1], [0, 2], [1, 3]]
# REP_FAC = 3
# T= [3, 2, 2, 2, 4]
# data = [[1, 3, 0], [0, 1, 4], [0, 1, 2], [2, 3, 1], [4, 1, 2]]
print(LP_solver(T, data, 2))
ans, tasks = LP_solver(T, data, 2)
p = ans["x"]
q = list()
for i in range(0, len(data)):
    q.append(random.random())

results = list()
start = 0
end = start + len(T)
j = 0  # task
while end < len(p):
    pis = p[start:end]
    sum = 0
    i = 0
    for pi in pis:
        sum = sum + pi
        if q[j] <= sum:
            results.append([j, i])
            break
        i = i + 1
    j = j + 1
    start = start + len(T)
    end = end + len(T)

print(q)
print(results)

# ans, tasks = LP_solver(T, data, REP_FAC)

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
print(ans)
print(q)
print(results)








# 0.17142857
# ll = [0]*2 + [1] * 3
#
# print(ll)
# Aeq_li = list()
# d = 0
# T[0] = 1
# print(T)
# Aeq_li = list()
# task = 4
# disk = 3
# for i in range(0, task):
#     eq = [0]*disk*i + [1]*disk + [0]*disk * (task - i -1) + [0]
"""    for j in range(0, task):
    for k in range(0, disk):
        if j == d:
            eq.append(1)
        else:
            eq.append(0)
# eq.append(0)
d = d + 1
Aeq_li.append(eq)
gc.collect()
"""
    # d = d + 1
    # Aeq_li.append(eq)
# sum = 0
# for i in range(0, 100):
#     sum = sum + random.random()
#     print(sum/100)
# u_data = list()
# temp = dict()
# temp["x"] = [1, 2, 3]
# temp["y"] = [1, 2, 3]
# u_data.append(temp)
# u_data.append(temp)

# with open("u_t_qos_data_2", "w") as file:
#     json.dump(u_data, file)
#
# with open("u_t_qos_data_2", "r") as file:
#     data = json.load(file, object_pairs_hook=OrderedDict)
#     print(data)
#     for item in data:
#         xli = item["x"]
#         yli = item["y"]
#
#         print(xli, yli)
#
#