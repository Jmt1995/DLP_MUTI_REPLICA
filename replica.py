class Replica:
    def __init__(self, replica_id, data_id):
        self.id = replica_id
        self.data_id = data_id
        #self.data_id = data_id
        self.disk_id = -1
        self.load = 0

    def __str__(self):
        return "Replica id = " + str(self.id)  + " , data_id = " + str(
            self.data_id) +  " | id=%d" % id(self)

    def set_disk_id(self, disk_id):
        self.disk_id = disk_id

    def set_load(self, load):
        self.load = load