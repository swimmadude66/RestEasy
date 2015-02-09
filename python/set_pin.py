import os
import sys
import json
from Pin import pin, pin_power

def set_pin_info(pin_obj):
    pin_id = pin_obj['ID']
    if not (os.path.isdir('/sys/class/gpio/gpio'+str(pin_id))):
        print('{\n\tsuccess: false, \n\tmessage: "pin ' + pin_id +' does not exist"\n}')
        exit(-1)
    pin_path = '/sys/class/gpio/gpio'+str(pin_id)+'/'
    open(pin_path+'active_low', 'w').write(str(pin_obj['active_low']))
    open(pin_path+'direction', 'w').write(str(pin_obj['direction']))
    open(pin_path+'edge', 'w').write(str(pin_obj['edge']))
    open(pin_path+'value', 'w').write(str(pin_obj['value']))
    pin_power_path = pin_path +'power/'
    open(pin_power_path+'async', 'w').write(str(pin_obj['power']['async']))
    open(pin_power_path+'control', 'w').write(str(pin_obj['power']['control']))
    open(pin_power_path+'runtime_enabled', 'w').write(str(pin_obj['power']['runtime_enabled']))
    open(pin_power_path+'runtime_status', 'w').write(str(pin_obj['power']['runtime_status']))
    open(pin_power_path+'runtime_active_kids', 'w').write(str(pin_obj['power']['runtime_active_kids']))
    open(pin_power_path+'runtime_active_time', 'w').write(str(pin_obj['power']['runtime_active_time']))
    open(pin_power_path+'runtime_suspended_time', 'w').write(str(pin_obj['power']['runtime_suspended_time']))
    open(pin_power_path+'runtime_usage', 'w').write(str(pin_obj['power']['runtime_usage']))
    print("{\"success\": true, \"message\": \"pin " + str(pin_id) + " updated!\"}")

if len(sys.argv) != 2:
    print('Usage: python set_pin.py <pin_data_json>')
    exit(1)
else:
    pin_string = (sys.argv[1])
    pin_data = json.loads(pin_string)
    if isinstance(pin_data, list):
        first = True
        print('[')
        for pin_dict in pin_data:
            if not first:
                print(',')
            set_pin_info(pin_dict)
            first = False
        print(']')
    elif isinstance(pin_data, dict):
        set_pin_info(pin_data)
    else:
        print('{\"success\": false, \"message\": \"Json data not properly formatted as object or array\"}')
        exit(1)
