import json

import napalm

driver = napalm.get_network_driver("ios")

device = driver(hostname="192.168.80.128", username="admin", password="cisco123")

device.open()

device_facts = device.get_facts()

print(json.dumps(device_facts, indent = 4))

device.close()

