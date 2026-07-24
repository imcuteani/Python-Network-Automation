# test-interface.py 
#---------------------------------------------------
# write the target verificatin functions starting with test_ prefix. 

import pytest 

def test_gigabit_ethernet_status(router_conn):
    """verifies that Gigabit ethernet1 is operationally up and active"""
    # send CLI command to the network device
    response = router_conn.send_command("show interface GigabitEthernet1")
    output = response.result 

    # Assert conditions to determine pass or fail status 
    assert "GigabitEthernet1 is up" in output, "Interface is down!"
    assert "line protocol is up" in output, "Line protocol match failed!"