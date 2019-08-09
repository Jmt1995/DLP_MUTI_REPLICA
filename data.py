import math
from collections import OrderedDict


class Data:
    def __init__(self, data_id):
        self.id = data_id
        self.rep_set = list()




    def __str__(self):
        s = "Data id = " + str(self.id) \
            + ", len(Rep_set) = %d Degree = " % len(self.rep_set)
        return s


    def add_rep(self, replica):
        self.rep_set.append(replica)
        return self

    def del_rep(self, replica):
        self.rep_set.remove(replica)
        return self

    def get_data_rep_set(self):
        return self.rep_set
