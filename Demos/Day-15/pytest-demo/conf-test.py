# An advanced pytest framework for Netmiko utilizes the session-scoped connection features, 
# parameterization across the multiple disparate device types and text parsing via TextFSM library. 

import pytest 
from netmiko import ConnectHandler

@pytest.fixture(scope="session")
def net_device(request):
    # pass the router device parameters or default multi-vendor definition
    device = getattr(request, "param",{
        "device_type": "cisco_ios_telnet",
        "host": "192.168.80.128",
        "port": "5008",
        "username": "admin",
        "password": "cisco123",
    })
    net_connect = ConnectHandler(**device)
    yield net_connect
    net_connect.disconnect()