from LP import *
import random
from collections import OrderedDict
import json
T = [0.3, 0.1, 0.2, 0.2] #Tj
data = [[0, 1], [1, 2], [0, 2], [1, 3]]

print(LP_solver(T, data))
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
with open("u_t_qos_data_2", "r") as file:
    data = json.load(file, object_pairs_hook=OrderedDict)
    print(data)
    for item in data:
        xli = item["x"]
        yli = item["y"]

        print(xli, yli)

