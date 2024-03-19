class Bridge:
    max_capacity = 20
    max_weight = 30000
    vehicle_list = []

    def calc_total_weight(self):
        total_weight = 0
        for vehicle in self.vehicle_list:
            total_weight += vehicle.weight
        return total_weight

    def add_vehicle(self, vehicle):
        if len(self.vehicle_list) >= self.max_capacity:
            return "Cannot add vehicle, bridge full"
        else:
            self.vehicle_list.append(vehicle)


    def remove_vehicle(self, vehicle):
        pass