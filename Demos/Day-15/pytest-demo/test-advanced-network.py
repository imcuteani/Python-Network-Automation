# parameterized test execution for network device automation with pytest 
# -------------------------------------------------------------------------------

import pytest 

@pytest.mark.parametrize("net_device",[
    {"device_type": "cisco_ios_telnet", "host": "192.168.80.128", "port": "5008", "username": "admin", "password": "cisco123"},
    {"device_type": "cisco_ios_telnet","host": "192.168.80.128", "port":"5009", "username": "admin", "password": "cisco123"}
], indirect=True)

# check the device connectivity commands 
def test_interface_status(net_device):
    output = net_device.send_command("show ip interface brief", use_textfsm=True)
    assert isinstance(output, list), "TextFSM did not return structured data"
    for intf in output: 
        assert intf["status"] != "disabled", f"interface {intf['interface']} is unpectedly disabled"