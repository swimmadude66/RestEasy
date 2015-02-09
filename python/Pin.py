class pin_power:
    async = 'disabled'
    control = 'auto'
    runtime_enabled = 'disabled'
    runtime_status = 'Unsupported'
    runtime_active_kids = 0
    runtime_active_time = 0
    runtime_suspended_time = 0
    runtime_usage = 0

    def __str__(self):
        obj ="{\n"
        obj += "\t\t\"async\": \"" + self.async + "\",\n"
        obj += "\t\t\"control\": \"" + self.control + "\",\n"
        obj += "\t\t\"runtime_enabled\": \"" + self.runtime_enabled + "\",\n"
        obj += "\t\t\"runtime_status\": \"" + self.runtime_status + "\",\n"
        obj += "\t\t\"runtime_active_kids\": " + str(self.runtime_active_kids) + ",\n"
        obj += "\t\t\"runtime_active_time\": " + str(self.runtime_active_time) + ",\n"
        obj += "\t\t\"runtime_suspended_time\": " + str(self.runtime_suspended_time) + ",\n"
        obj += "\t\t\"runtime_usage\": " + str(self.runtime_usage) + "\n"
        obj += "\t}"
        return obj

class pin:
    def __init__(self, id_number):
        self.ID = id_number
    active_low = False
    direction = 'out'
    edge = 'None'
    value = 0
    power = pin_power()

    def __str__(self):
        obj ="{\n"
        obj += "\t\"ID\": " + str(self.ID) + ",\n"
        obj += "\t\"active_low\": " + str(self.active_low) + ",\n"
        obj += "\t\"direction\": \"" + self.direction + "\",\n"
        obj += "\t\"edge\": \"" + self.edge + "\",\n"
        obj += "\t\"value\": " + str(self.value) + ",\n"
        obj += "\t\"power\": " + str(self.power) + "\n"
        obj += "}"
        return obj
