


class  Disk:
    def __init__(self, disk_id, read_latency):
        self.id = disk_id
        self.read_latency = read_latency
        self.rep_list = list()

        self.active_list = list()

    def __str__(self):
        return "node id = " + str(self.id) \
               + " , read_latency = " + str(self.read_latency) \
               + " | id=%d" % id(self)

    def add_rep(self, rep_id):
        self.rep_set.append(rep_id)
        return self
    def add_active(self, rep_id):
        self.active_list.append(rep_id)
        return self