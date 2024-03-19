class Bridge:
    max_num = 20
    max_weight = 30000
    vehicle_list = []

    def calc_total_weight(self):
        total_weight = 0
        for vehicle in self.vehicle_list:
            total_weight += vehicle.weight
        return total_weight