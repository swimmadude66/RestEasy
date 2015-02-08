import os
import sys
from subprocess import check_output


class pin_power:
    async = False
    control = 'auto'
    runtime_enabled = 'disabled'
    runtime_status = 'Unsupported'
    runtime_active_kids = 0
    runtime_active_time = 0
    runtime_suspended_time = 0
    runtime_usage = 0

    def __str__(self):
        obj ="{\n"
        obj += "\t\t'async': " + str(self.async) + ",\n"
        obj += "\t\t'control': '" + self.control + "',\n"
        obj += "\t\t'runtime_enabled': '" + self.runtime_enabled + "',\n"
        obj += "\t\t'runtime_status': '" + self.runtime_status + "',\n"
        obj += "\t\t'runtime_active_kids': " + str(self.runtime_active_kids) + ",\n"
        obj += "\t\t'runtime_active_time': " + str(self.runtime_active_time) + ",\n"
        obj += "\t\t'runtime_suspended_time': " + str(self.runtime_suspended_time) + ",\n"
        obj += "\t\t'runtime_usage': " + str(self.runtime_usage) + "\n"
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
        obj += "\t'ID': " + str(self.ID) + ",\n"
        obj += "\t'active_low': " + str(self.active_low) + ",\n"
        obj += "\t'direction': '" + self.direction + "',\n"
        obj += "\t'edge': '" + self.edge + "',\n"
        obj += "\t'value': " + str(self.value) + ",\n"
        obj += "\t'power': " + str(self.power) + "\n"
        obj += "}"
        return obj


def get_pin_info(pin_id):
    if not (os.path.isdir('/sys/class/gpio/gpio'+str(pin_id))):
        print('{\n\tsuccess: false, \n\tmessage: "pin ' + pin_id +' does not exist"\n}')
        exit(-1)
    pin_obj = pin(pin_id)
    pin_path = '/sys/class/gpio/gpio'+str(pin_id)+'/'
    pin.active_low = open(pin_path+'active_low', 'r').read().strip()
    pin.direction = open(pin_path+'direction', 'r').read().strip()
    pin.edge = open(pin_path+'edge', 'r').read().strip()
    pin.value = open(pin_path+'value', 'r').read().strip()
    pin.power = pin_power()
    pin_power_path = pin_path +'power/'
    pin.power.async = open(pin_power_path+'async').read().strip()
    pin.power.control = open(pin_power_path+'control').read().strip()
    pin.power.runtime_enabled = open(pin_power_path+'runtime_enabled').read().strip()
    pin.power.runtime_status = open(pin_power_path+'runtime_status').read().strip()
    pin.power.runtime_active_kids = open(pin_power_path+'runtime_active_kids').read().strip()
    pin.power.runtime_active_time = open(pin_power_path+'runtime_active_time').read().strip()
    pin.power.runtime_suspended_time = open(pin_power_path+'runtime_suspended_time').read().strip()
    pin.power.runtime_usage = open(pin_power_path+'runtime_usage').read().strip()
    print(pin_obj)

if len(sys.argv) != 2:
    print('Usage: python get_pin.py <pin_id>')
    exit(1)
elif '-a' in sys.argv[1] :
    all_pins = os.listdir('/sys/class/gpio/')
    print('[')
    for pin_name in all_pins:
        if 'gpio' in pin_name:
            if 'chip' not in pin_name:
                get_pin_info(pin_name[4:])
    print(']')
else:
    get_pin_info(sys.argv[1])
