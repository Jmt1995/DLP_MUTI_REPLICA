
from readFile import readFile
from init1 import *
import copy
from collections import OrderedDict
import json
from collections import OrderedDict
# from init import *
# from printinfo import *
# from max_time import *
# from dlp_opt import *
def main():
    config_data = readFile()

    # HDD_size = config_data.get("HDD_size")  # TB
    Rep_num = config_data.get("R_number")
    DISK_num = config_data.get("DISK_num")
    Latency_range = config_data.get("Latency_range")

    REP_FAC = config_data.get("REP_FAC")
    DATA_NUM = config_data.get("DATA_NUM")


    print(config_data)

    r_data = list()
    x_y_temp = dict()
    batch = 10
    Result_data = list()

    for i in range(0, batch):

        '''
        Initialize
        '''
        print("--------------- Initialize ---------------")
        disks = init_disks(DISK_num, Latency_range)
        data_list, replica_list = init_datas(DATA_NUM, REP_FAC)

        deploy_replica(disks, replica_list)

        r_data = dict()
        print("--------------- hadoop ---------------")
        disk_cp1 = copy.deepcopy(disks)
        x1,y1, max_load = hadoop_naive(disk_cp1, data_list, replica_list)
        x_y_temp = dict()
        x_y_temp["x"] = x1
        x_y_temp["y"] = y1
        x_y_temp["maxload"] = max_load
        r_data["hadoop"] = x_y_temp
        r_data["DISK_num"] = DISK_num
        r_data["DISK_num"] = DISK_num

        # Result_data["hadoop"]
        #
        # print("--------------- random ---------------")
        # disk_cp2 = copy.deepcopy(disks)
        # x2,y2, max_load = random_naive(disk_cp2, data_list, replica_list)
        # x_y_temp = dict()
        # x_y_temp["x"] = x2
        # x_y_temp["y"] = y2
        # x_y_temp["maxload"] = max_load
        # r_data.append(x_y_temp)


        print("--------------- HTS-greedy ---------------")
        disk_cp3 = copy.deepcopy(disks)
        x3, y3, max_load = greedy(disk_cp3, data_list, replica_list)
        x_y_temp = dict()
        x_y_temp["x"] = x3
        x_y_temp["y"] = y3
        x_y_temp["maxload"] = max_load
        r_data["HTS-greedy"] = x_y_temp
        # r_data.append(x_y_temp)

        print("--------------- HTS-rdm ---------------")
        disk_cp4 = copy.deepcopy(disks)
        x4, y4, max_load = DLP_random(disk_cp4, data_list, replica_list, REP_FAC)

        x_y_temp = dict()
        x_y_temp["x"] = x4
        x_y_temp["y"] = y4
        x_y_temp["maxload"] = max_load
        r_data["HTS-rdm"] = x_y_temp
        # r_data.append(x_y_temp)

        Result_data.append(r_data)
    with open("Result_data", "w") as file:
        json.dump(Result_data, file)

    plt.figure()
    plt.xlim([0, DISK_num-1])
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel("disk", fontsize=14)
    plt.ylabel("latency", fontsize=14)
    plt.plot(x1, y1,  color="red", label="Hadoop")
    # plt.step(x2, y2, label="random", color="blue", where="post")
    plt.plot(x3, y3,  color="black", label="HTS-greedy", linestyle="-.")
    plt.plot(x4, y4, color="green", label="HTS-rdm",linestyle="--")
    plt.legend(loc="upper right")

    # foo_fig = plt.gcf()  # 'get current figure'
    # foo_fig.savefig('instance.eps', format='eps', dpi=1000)
    # plt.savefig('./plteps.eps', format='eps', dpi=1000)
    file_name = "fig3_6.eps"
    plt.savefig(file_name, bbox_inches='tight', format='eps', dpi=5000)
    plt.show()

if __name__ == '__main__':
    main()
